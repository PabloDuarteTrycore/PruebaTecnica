"""
Unit tests for evm_service module.

Tests cover all EVM calculation functions with focus on edge cases,
boundary conditions, and integration scenarios.

Pytest Coverage Target: 80% of app/services/
"""

from decimal import Decimal
import pytest
from app.services.evm_service import (
    calculate_pv,
    calculate_ev,
    calculate_cv,
    calculate_sv,
    calculate_cpi,
    calculate_spi,
    calculate_eac,
    calculate_vac,
    interpret_performance_index,
    calculate_activity_evm,
    calculate_project_evm,
    ActivityEVMResult,
    ProjectEVMResult,
    EVM_CONSTANTS,
)


# ============================================================================
# Test Fixtures
# ============================================================================


class MockActivity:
    """Mock Activity model for testing calculate_project_evm."""

    def __init__(
        self,
        bac: float,
        planned_progress: float,
        actual_progress: float,
        actual_cost: float,
    ):
        self.bac = bac
        self.planned_progress = planned_progress
        self.actual_progress = actual_progress
        self.actual_cost = actual_cost


# ============================================================================
# Test: calculate_pv
# ============================================================================


class TestCalculatePV:
    """Test cases for calculate_pv function."""

    def test_standard_case(self):
        """Test standard calculation: 50% of 1000 should be 500."""
        result = calculate_pv(bac=Decimal("1000"), planned_progress=Decimal("50"))
        assert result == Decimal("500")

    def test_zero_progress(self):
        """Test zero progress: should return 0 regardless of BAC."""
        result = calculate_pv(bac=Decimal("1000"), planned_progress=Decimal("0"))
        assert result == Decimal("0")

    def test_complete_progress(self):
        """Test 100% progress: should return full BAC."""
        result = calculate_pv(bac=Decimal("1000"), planned_progress=Decimal("100"))
        assert result == Decimal("1000")

    def test_zero_bac(self):
        """Test zero BAC: should return 0 regardless of progress."""
        result = calculate_pv(bac=Decimal("0"), planned_progress=Decimal("50"))
        assert result == Decimal("0")

    def test_partial_progress_with_decimals(self):
        """Test with decimal progress: 33.33% of 3000."""
        result = calculate_pv(bac=Decimal("3000"), planned_progress=Decimal("33.33"))
        # 33.33 / 100 * 3000 = 999.90
        assert result == Decimal("999.90")


# ============================================================================
# Test: calculate_ev
# ============================================================================


class TestCalculateEV:
    """Test cases for calculate_ev function."""

    def test_standard_case(self):
        """Test standard calculation: 40% of 1000 should be 400."""
        result = calculate_ev(bac=Decimal("1000"), actual_progress=Decimal("40"))
        assert result == Decimal("400")

    def test_zero_progress(self):
        """Test zero progress: should return 0 (no work completed)."""
        result = calculate_ev(bac=Decimal("1000"), actual_progress=Decimal("0"))
        assert result == Decimal("0")

    def test_complete_progress(self):
        """Test 100% progress: should return full BAC."""
        result = calculate_ev(bac=Decimal("1000"), actual_progress=Decimal("100"))
        assert result == Decimal("1000")


# ============================================================================
# Test: calculate_cv
# ============================================================================


class TestCalculateCV:
    """Test cases for calculate_cv function."""

    def test_efficient_under_budget(self):
        """Test efficient case: EV > AC (positive variance)."""
        result = calculate_cv(ev=Decimal("800"), actual_cost=Decimal("600"))
        assert result == Decimal("200")
        assert result > Decimal("0")

    def test_inefficient_over_budget(self):
        """Test inefficient case: EV < AC (negative variance)."""
        result = calculate_cv(ev=Decimal("400"), actual_cost=Decimal("600"))
        assert result == Decimal("-200")
        assert result < Decimal("0")

    def test_actual_cost_zero(self):
        """Test when no cost incurred yet: CV should equal EV."""
        result = calculate_cv(ev=Decimal("500"), actual_cost=Decimal("0"))
        assert result == Decimal("500")

    def test_earned_value_zero_positive_cost(self):
        """Test when work is zero but cost is positive (waste)."""
        result = calculate_cv(ev=Decimal("0"), actual_cost=Decimal("200"))
        assert result == Decimal("-200")


# ============================================================================
# Test: calculate_sv
# ============================================================================


class TestCalculateSV:
    """Test cases for calculate_sv function."""

    def test_ahead_of_schedule(self):
        """Test when actual work > planned work (positive variance)."""
        result = calculate_sv(ev=Decimal("800"), pv=Decimal("600"))
        assert result == Decimal("200")
        assert result > Decimal("0")

    def test_behind_schedule(self):
        """Test when actual work < planned work (negative variance)."""
        result = calculate_sv(ev=Decimal("400"), pv=Decimal("600"))
        assert result == Decimal("-200")
        assert result < Decimal("0")

    def test_planned_value_zero(self):
        """Test when nothing should be planned yet."""
        result = calculate_sv(ev=Decimal("500"), pv=Decimal("0"))
        assert result == Decimal("500")

    def test_earned_value_zero(self):
        """Test when no progress but work was planned."""
        result = calculate_sv(ev=Decimal("0"), pv=Decimal("300"))
        assert result == Decimal("-300")


# ============================================================================
# Test: calculate_cpi (CRITICAL EDGE CASES)
# ============================================================================


class TestCalculateCPI:
    """Test cases for calculate_cpi function."""

    def test_returns_none_when_actual_cost_is_zero(self):
        """Critical edge case: AC = 0 should return None (not raise exception)."""
        result = calculate_cpi(ev=Decimal("500"), actual_cost=Decimal("0"))
        assert result is None

    def test_efficient_cost_performance(self):
        """Test efficient case: CPI > 1 (good value for money)."""
        result = calculate_cpi(ev=Decimal("800"), actual_cost=Decimal("600"))
        assert result is not None
        assert result > EVM_CONSTANTS.PERFORMANCE_THRESHOLD
        assert result == Decimal("800") / Decimal("600")

    def test_inefficient_cost_performance(self):
        """Test inefficient case: CPI < 1 (poor value for money)."""
        result = calculate_cpi(ev=Decimal("400"), actual_cost=Decimal("600"))
        assert result is not None
        assert result < EVM_CONSTANTS.PERFORMANCE_THRESHOLD

    def test_zero_earned_value_with_positive_cost(self):
        """Test when nothing earned but cost incurred: CPI = 0."""
        result = calculate_cpi(ev=Decimal("0"), actual_cost=Decimal("200"))
        assert result is not None
        assert result == Decimal("0")

    def test_equal_earned_value_and_cost(self):
        """Test when CPI = 1 (perfectly on budget)."""
        result = calculate_cpi(ev=Decimal("1000"), actual_cost=Decimal("1000"))
        assert result is not None
        assert result == EVM_CONSTANTS.PERFORMANCE_THRESHOLD


# ============================================================================
# Test: calculate_spi (CRITICAL EDGE CASES)
# ============================================================================


class TestCalculateSPI:
    """Test cases for calculate_spi function."""

    def test_returns_none_when_planned_value_is_zero(self):
        """Critical edge case: PV = 0 should return None (not raise exception)."""
        result = calculate_spi(ev=Decimal("500"), pv=Decimal("0"))
        assert result is None

    def test_ahead_of_schedule_performance(self):
        """Test efficient case: SPI > 1 (ahead of schedule)."""
        result = calculate_spi(ev=Decimal("800"), pv=Decimal("600"))
        assert result is not None
        assert result > EVM_CONSTANTS.PERFORMANCE_THRESHOLD

    def test_behind_schedule_performance(self):
        """Test inefficient case: SPI < 1 (behind schedule)."""
        result = calculate_spi(ev=Decimal("400"), pv=Decimal("600"))
        assert result is not None
        assert result < EVM_CONSTANTS.PERFORMANCE_THRESHOLD

    def test_zero_earned_value_with_positive_planned(self):
        """Test when nothing earned but work was planned: SPI = 0."""
        result = calculate_spi(ev=Decimal("0"), pv=Decimal("200"))
        assert result is not None
        assert result == Decimal("0")

    def test_equal_earned_and_planned_value(self):
        """Test when SPI = 1 (perfectly on schedule)."""
        result = calculate_spi(ev=Decimal("1000"), pv=Decimal("1000"))
        assert result is not None
        assert result == EVM_CONSTANTS.PERFORMANCE_THRESHOLD


# ============================================================================
# Test: calculate_eac
# ============================================================================


class TestCalculateEAC:
    """Test cases for calculate_eac function."""

    def test_standard_calculation(self):
        """Test normal case: EAC = BAC / CPI."""
        result = calculate_eac(bac=Decimal("1000"), cpi=Decimal("0.8"))
        assert result is not None
        assert result == Decimal("1250")

    def test_returns_none_when_cpi_is_none(self):
        """Test when CPI is None (insufficient data)."""
        result = calculate_eac(bac=Decimal("1000"), cpi=None)
        assert result is None

    def test_returns_none_when_cpi_is_zero(self):
        """Test when CPI is zero (division by zero)."""
        result = calculate_eac(bac=Decimal("1000"), cpi=Decimal("0"))
        assert result is None

    def test_cpi_equals_one(self):
        """Test when CPI = 1 (on budget): EAC should equal BAC."""
        result = calculate_eac(bac=Decimal("1000"), cpi=Decimal("1"))
        assert result is not None
        assert result == Decimal("1000")


# ============================================================================
# Test: calculate_vac
# ============================================================================


class TestCalculateVAC:
    """Test cases for calculate_vac function."""

    def test_standard_calculation_over_budget(self):
        """Test normal case: VAC = BAC - EAC (negative = over budget)."""
        result = calculate_vac(bac=Decimal("1000"), eac=Decimal("1250"))
        assert result is not None
        assert result == Decimal("-250")

    def test_returns_none_when_eac_is_none(self):
        """Test when EAC is None (insufficient data)."""
        result = calculate_vac(bac=Decimal("1000"), eac=None)
        assert result is None

    def test_eac_equals_bac(self):
        """Test when EAC = BAC (perfect): VAC should be zero."""
        result = calculate_vac(bac=Decimal("1000"), eac=Decimal("1000"))
        assert result is not None
        assert result == Decimal("0")


# ============================================================================
# Test: interpret_performance_index
# ============================================================================


class TestInterpretPerformanceIndex:
    """Test cases for interpret_performance_index function."""

    def test_value_greater_than_one_is_efficient(self):
        """Test that value > 1 returns 'efficient'."""
        result = interpret_performance_index(Decimal("1.5"))
        assert result == EVM_CONSTANTS.INTERPRETATION_EFFICIENT

    def test_value_equal_to_one_is_on_track(self):
        """Test that value == 1 returns 'on_track'."""
        result = interpret_performance_index(Decimal("1"))
        assert result == EVM_CONSTANTS.INTERPRETATION_ON_TRACK

    def test_value_less_than_one_is_inefficient(self):
        """Test that value < 1 returns 'inefficient'."""
        result = interpret_performance_index(Decimal("0.7"))
        assert result == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT

    def test_none_value_is_insufficient_data(self):
        """Test that None returns 'insufficient_data'."""
        result = interpret_performance_index(None)
        assert result == EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA


# ============================================================================
# Test: calculate_activity_evm (INTEGRATION TEST)
# ============================================================================


class TestCalculateActivityEVM:
    """Integration tests for calculate_activity_evm function."""

    def test_returns_activity_evm_result(self):
        """Test that function returns ActivityEVMResult dataclass."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("50"),
            actual_progress=Decimal("40"),
            actual_cost=Decimal("600"),
        )
        assert isinstance(result, ActivityEVMResult)

    def test_standard_scenario_with_all_fields(self):
        """Test complete calculation of all 10 fields."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("50"),
            actual_progress=Decimal("40"),
            actual_cost=Decimal("600"),
        )
        # Verify all fields are populated
        assert result.pv == Decimal("500")  # 50% of 1000
        assert result.ev == Decimal("400")  # 40% of 1000
        assert result.cv == Decimal("-200")  # 400 - 600
        assert result.sv == Decimal("-100")  # 400 - 500
        assert result.cpi == Decimal("400") / Decimal("600")
        assert result.spi == Decimal("400") / Decimal("500")
        assert result.eac is not None
        assert result.vac is not None
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT

    def test_actual_cost_zero_results_in_none_indices(self):
        """Test that AC=0 produces None CPI, EAC, VAC and insufficient_data."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("50"),
            actual_progress=Decimal("40"),
            actual_cost=Decimal("0"),
        )
        assert result.cpi is None
        assert result.eac is None
        assert result.vac is None
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA

    def test_zero_actual_progress(self):
        """Test activity with no progress: EV=0, CV and SV should be negative."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("50"),
            actual_progress=Decimal("0"),
            actual_cost=Decimal("100"),
        )
        assert result.ev == Decimal("0")
        assert result.cv == Decimal("-100")  # 0 - 100
        assert result.sv == Decimal("-500")  # 0 - 500
        assert result.cpi == Decimal("0")

    def test_completed_at_budget_scenario(self):
        """Test ideal scenario: 100% complete, on budget."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("100"),
            actual_progress=Decimal("100"),
            actual_cost=Decimal("1000"),
        )
        assert result.pv == Decimal("1000")
        assert result.ev == Decimal("1000")
        assert result.cv == Decimal("0")
        assert result.sv == Decimal("0")
        assert result.cpi == Decimal("1")
        assert result.spi == Decimal("1")
        assert result.eac == Decimal("1000")
        assert result.vac == Decimal("0")
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_ON_TRACK
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_ON_TRACK

    def test_ahead_and_under_budget(self):
        """Test scenario: project ahead of schedule and under budget."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("40"),
            actual_progress=Decimal("60"),  # Ahead
            actual_cost=Decimal("400"),  # Under
        )
        assert result.cpi > Decimal("1")  # 600/400 = 1.5
        assert result.spi > Decimal("1")  # 600/400 = 1.5
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_EFFICIENT
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_EFFICIENT

    def test_behind_and_over_budget(self):
        """Test scenario: project behind schedule and over budget."""
        result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("60"),
            actual_progress=Decimal("40"),  # Behind
            actual_cost=Decimal("700"),  # Over
        )
        assert result.cpi < Decimal("1")  # 400/700 < 1
        assert result.spi < Decimal("1")  # 400/600 < 1
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT


# ============================================================================
# Test: calculate_project_evm (CONSOLIDATION TEST)
# ============================================================================


class TestCalculateProjectEVM:
    """Test cases for calculate_project_evm function."""

    def test_returns_project_evm_result(self):
        """Test that function returns ProjectEVMResult dataclass."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=50,
                actual_progress=40,
                actual_cost=600,
            )
        ]
        result = calculate_project_evm(activities)
        assert isinstance(result, ProjectEVMResult)

    def test_empty_activities_list(self):
        """Test with empty list: should return zero totals and None indices."""
        result = calculate_project_evm([])
        assert result.total_bac == Decimal("0")
        assert result.total_pv == Decimal("0")
        assert result.total_ev == Decimal("0")
        assert result.total_ac == Decimal("0")
        assert result.cv == Decimal("0")
        assert result.sv == Decimal("0")
        assert result.cpi is None
        assert result.spi is None
        assert result.eac is None
        assert result.vac is None
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA

    def test_single_activity_matches_activity_calculation(self):
        """Test that single activity project equals activity EVM calculation."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=50,
                actual_progress=40,
                actual_cost=600,
            )
        ]
        project_result = calculate_project_evm(activities)
        activity_result = calculate_activity_evm(
            bac=Decimal("1000"),
            planned_progress=Decimal("50"),
            actual_progress=Decimal("40"),
            actual_cost=Decimal("600"),
        )
        # Verify key consolidated metrics match single activity
        assert project_result.total_bac == activity_result.pv + activity_result.sv
        assert project_result.total_ev == activity_result.ev
        assert project_result.total_ac == Decimal("600")

    def test_multiple_activities_consolidation(self):
        """Test consolidation of multiple activities."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=50,
                actual_progress=40,
                actual_cost=600,
            ),
            MockActivity(
                bac=2000,
                planned_progress=60,
                actual_progress=70,
                actual_cost=1200,
            ),
        ]
        result = calculate_project_evm(activities)
        # Verify aggregation
        assert result.total_bac == Decimal("3000")  # 1000 + 2000
        assert result.total_pv == Decimal("1700")  # 500 + 1200
        assert result.total_ev == Decimal("1800")  # 400 + 1400
        assert result.total_ac == Decimal("1800")  # 600 + 1200
        # Verify derived metrics
        assert result.cv == Decimal("0")  # 1800 - 1800
        assert result.sv == Decimal("100")  # 1800 - 1700
        # Verify indices are calculated on totals
        assert result.cpi == Decimal("1")  # 1800 / 1800
        assert result.spi is not None

    def test_activity_with_zero_cost_in_project(self):
        """Test project consolidation when one activity has AC=0."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=50,
                actual_progress=40,
                actual_cost=600,
            ),
            MockActivity(
                bac=1000,
                planned_progress=50,
                actual_progress=40,
                actual_cost=0,  # Not yet started cost-wise
            ),
        ]
        result = calculate_project_evm(activities)
        # CPI should still be calculable from total_ac
        assert result.total_ac == Decimal("600")
        assert result.cpi is not None

    def test_float_input_conversion_to_decimal(self):
        """Test that float inputs from DB are converted to Decimal correctly."""
        # Mock activity with float values (from database)
        activities = [MockActivity(bac=1000.5, planned_progress=50.25, actual_progress=40.75, actual_cost=600.99)]
        result = calculate_project_evm(activities)
        # Should handle conversion without precision loss
        assert result.total_bac == Decimal("1000.5")
        assert result.total_ac == Decimal("600.99")
        # Verify CPI is not None and is reasonable
        assert result.cpi is not None
        assert result.cpi > Decimal("0")

    def test_project_ahead_and_under_budget(self):
        """Test project consolidation in ideal scenario."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=40,
                actual_progress=60,  # Ahead
                actual_cost=400,  # Under
            ),
            MockActivity(
                bac=1000,
                planned_progress=40,
                actual_progress=60,  # Ahead
                actual_cost=400,  # Under
            ),
        ]
        result = calculate_project_evm(activities)
        assert result.cpi > Decimal("1")  # Should be efficient
        assert result.spi > Decimal("1")  # Should be ahead
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_EFFICIENT
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_EFFICIENT

    def test_project_behind_and_over_budget(self):
        """Test project consolidation in problematic scenario."""
        activities = [
            MockActivity(
                bac=1000,
                planned_progress=60,
                actual_progress=40,  # Behind
                actual_cost=700,  # Over
            ),
            MockActivity(
                bac=1000,
                planned_progress=60,
                actual_progress=40,  # Behind
                actual_cost=700,  # Over
            ),
        ]
        result = calculate_project_evm(activities)
        assert result.cpi < Decimal("1")  # Should be inefficient
        assert result.spi < Decimal("1")  # Should be behind
        assert result.cpi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT
        assert result.spi_interpretation == EVM_CONSTANTS.INTERPRETATION_INEFFICIENT
