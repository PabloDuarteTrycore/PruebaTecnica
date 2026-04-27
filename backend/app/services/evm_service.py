"""
EVM Service Module.

This module implements the Earned Value Management (EVM) methodology,
a PMI standard for measuring project performance in terms of schedule
and cost variance.

The module contains pure business logic with no dependencies on HTTP,
Flask, or database operations.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


class EVM_CONSTANTS:
    """Constants for EVM calculations."""

    # Divisor to convert percentage to decimal (50% → 0.50)
    PERCENT_DIVISOR = Decimal("100")

    # Threshold that defines if an index is efficient or not
    PERFORMANCE_THRESHOLD = Decimal("1")

    # Interpretations of results — avoid scattered string literals
    INTERPRETATION_EFFICIENT = "efficient"
    INTERPRETATION_INEFFICIENT = "inefficient"
    INTERPRETATION_ON_TRACK = "on_track"
    INTERPRETATION_INSUFFICIENT_DATA = "insufficient_data"


@dataclass
class ActivityEVMResult:
    """Result object containing EVM metrics for a single activity."""

    pv: Decimal  # Planned Value
    ev: Decimal  # Earned Value
    cv: Decimal  # Cost Variance
    sv: Decimal  # Schedule Variance
    cpi: Optional[Decimal]  # Cost Performance Index
    spi: Optional[Decimal]  # Schedule Performance Index
    eac: Optional[Decimal]  # Estimate at Completion
    vac: Optional[Decimal]  # Variance at Completion
    cpi_interpretation: str  # Textual interpretation of CPI
    spi_interpretation: str  # Textual interpretation of SPI


@dataclass
class ProjectEVMResult:
    """Result object containing consolidated EVM metrics for a project."""

    total_bac: Decimal  # Total Budget at Completion
    total_pv: Decimal  # Total Planned Value
    total_ev: Decimal  # Total Earned Value
    total_ac: Decimal  # Total Actual Cost
    cv: Decimal  # Cost Variance (EV - AC)
    sv: Decimal  # Schedule Variance (EV - PV)
    cpi: Optional[Decimal]  # Cost Performance Index
    spi: Optional[Decimal]  # Schedule Performance Index
    eac: Optional[Decimal]  # Estimate at Completion
    vac: Optional[Decimal]  # Variance at Completion
    cpi_interpretation: str  # Textual interpretation of CPI
    spi_interpretation: str  # Textual interpretation of SPI


# ============================================================================
# Primitive Functions - Basic EVM Calculations
# ============================================================================


def calculate_pv(bac: Decimal, planned_progress: Decimal) -> Decimal:
    """
    Calculate Planned Value.

    PV = (planned_progress / 100) × BAC

    The value of work that should be completed according to the original plan.

    Args:
        bac: Budget at Completion (total budgeted cost). Always ≥ 0.
        planned_progress: Planned percentage completion (0-100).

    Returns:
        Planned Value as Decimal. Never None — all inputs are valid states.
    """
    progress_ratio = planned_progress / EVM_CONSTANTS.PERCENT_DIVISOR
    return progress_ratio * bac


def calculate_ev(bac: Decimal, actual_progress: Decimal) -> Decimal:
    """
    Calculate Earned Value.

    EV = (actual_progress / 100) × BAC

    The value of work actually completed, expressed in terms of budget.

    Args:
        bac: Budget at Completion (total budgeted cost).
        actual_progress: Actual percentage completion (0-100).

    Returns:
        Earned Value as Decimal. Never None — all inputs are valid states.
    """
    progress_ratio = actual_progress / EVM_CONSTANTS.PERCENT_DIVISOR
    return progress_ratio * bac


def calculate_cv(ev: Decimal, actual_cost: Decimal) -> Decimal:
    """
    Calculate Cost Variance.

    CV = EV - AC

    Measures cost efficiency. Positive = under budget (efficient).
    Negative = over budget (inefficient).

    Args:
        ev: Earned Value.
        actual_cost: Actual Cost incurred.

    Returns:
        Cost Variance as Decimal. Never None.
    """
    return ev - actual_cost


def calculate_sv(ev: Decimal, pv: Decimal) -> Decimal:
    """
    Calculate Schedule Variance.

    SV = EV - PV

    Measures schedule efficiency. Positive = ahead of schedule.
    Negative = behind schedule.

    Args:
        ev: Earned Value.
        pv: Planned Value.

    Returns:
        Schedule Variance as Decimal. Never None.
    """
    return ev - pv


# ============================================================================
# Index Functions - Performance Indices with Edge Cases
# ============================================================================


def calculate_cpi(ev: Decimal, actual_cost: Decimal) -> Optional[Decimal]:
    """
    Calculate Cost Performance Index.

    CPI = EV / AC

    Measures cost efficiency. For every peso spent, how many pesos of value
    are obtained. CPI > 1 is efficient. CPI < 1 is inefficient.

    Critical edge case: Division by zero occurs when actual_cost == 0
    (activity planned but no costs incurred yet). This is valid — return None.

    Args:
        ev: Earned Value.
        actual_cost: Actual Cost incurred.

    Returns:
        Cost Performance Index as Decimal, or None if actual_cost is zero.
    """
    if actual_cost == Decimal("0"):
        return None
    return ev / actual_cost


def calculate_spi(ev: Decimal, pv: Decimal) -> Optional[Decimal]:
    """
    Calculate Schedule Performance Index.

    SPI = EV / PV

    Measures schedule efficiency. SPI > 1 is ahead of schedule.
    SPI < 1 is behind schedule.

    Critical edge case: Division by zero when pv == 0 (activity not yet
    started according to plan). This is valid — return None.

    Args:
        ev: Earned Value.
        pv: Planned Value.

    Returns:
        Schedule Performance Index as Decimal, or None if pv is zero.
    """
    if pv == Decimal("0"):
        return None
    return ev / pv


def calculate_eac(bac: Decimal, cpi: Optional[Decimal]) -> Optional[Decimal]:
    """
    Calculate Estimate at Completion.

    EAC = BAC / CPI

    Estimates the total cost when the project is complete, based on
    current cost performance.

    Args:
        bac: Budget at Completion.
        cpi: Cost Performance Index (may be None).

    Returns:
        Estimate at Completion as Decimal, or None if CPI is None or zero.
    """
    if cpi is None or cpi == Decimal("0"):
        return None
    return bac / cpi


def calculate_vac(bac: Decimal, eac: Optional[Decimal]) -> Optional[Decimal]:
    """
    Calculate Variance at Completion.

    VAC = BAC - EAC

    The difference between the original budget and estimated final cost.
    Negative means project is expected to exceed budget.

    Args:
        bac: Budget at Completion.
        eac: Estimate at Completion (may be None).

    Returns:
        Variance at Completion as Decimal, or None if EAC is None.
    """
    if eac is None:
        return None
    return bac - eac


# ============================================================================
# Interpretation Function
# ============================================================================


def interpret_performance_index(value: Optional[Decimal]) -> str:
    """
    Interpret a performance index (CPI or SPI) as a human-readable status.

    This function is used by the frontend to determine the color of status
    badges in the UI.

    Rules:
    - value is None: insufficient_data
    - value > 1: efficient
    - value == 1: on_track
    - value < 1: inefficient

    Args:
        value: The performance index value (CPI or SPI), or None.

    Returns:
        Interpretation string using EVM_CONSTANTS values.
    """
    if value is None:
        return EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA
    if value > EVM_CONSTANTS.PERFORMANCE_THRESHOLD:
        return EVM_CONSTANTS.INTERPRETATION_EFFICIENT
    if value == EVM_CONSTANTS.PERFORMANCE_THRESHOLD:
        return EVM_CONSTANTS.INTERPRETATION_ON_TRACK
    # value < PERFORMANCE_THRESHOLD
    return EVM_CONSTANTS.INTERPRETATION_INEFFICIENT


# ============================================================================
# Orchestrator Functions
# ============================================================================


def calculate_activity_evm(
    bac: Decimal,
    planned_progress: Decimal,
    actual_progress: Decimal,
    actual_cost: Decimal,
) -> ActivityEVMResult:
    """
    Calculate complete EVM metrics for a single activity.

    This function orchestrates all primitive calculation functions and
    returns a complete ActivityEVMResult object. It performs no direct
    calculations — only coordination.

    Args:
        bac: Budget at Completion.
        planned_progress: Planned progress percentage (0-100).
        actual_progress: Actual progress percentage (0-100).
        actual_cost: Actual cost incurred.

    Returns:
        ActivityEVMResult containing all 8 EVM metrics and interpretations.
    """
    pv = calculate_pv(bac, planned_progress)
    ev = calculate_ev(bac, actual_progress)
    cv = calculate_cv(ev, actual_cost)
    sv = calculate_sv(ev, pv)
    cpi = calculate_cpi(ev, actual_cost)
    spi = calculate_spi(ev, pv)
    eac = calculate_eac(bac, cpi)
    vac = calculate_vac(bac, eac)
    cpi_interpretation = interpret_performance_index(cpi)
    spi_interpretation = interpret_performance_index(spi)

    return ActivityEVMResult(
        pv=pv,
        ev=ev,
        cv=cv,
        sv=sv,
        cpi=cpi,
        spi=spi,
        eac=eac,
        vac=vac,
        cpi_interpretation=cpi_interpretation,
        spi_interpretation=spi_interpretation,
    )


def calculate_project_evm(activities: list) -> ProjectEVMResult:
    """
    Calculate consolidated EVM metrics for a project from its activities.

    Aggregates EVM metrics by summing the individual activity metrics.
    Larger activities (higher BAC) have proportionally greater impact.

    Edge case: Empty activity list returns a ProjectEVMResult with all
    numeric values as zero and indices as None (insufficient data).

    Args:
        activities: List of Activity objects with attributes:
                   bac, planned_progress, actual_progress, actual_cost

    Returns:
        ProjectEVMResult with consolidated metrics.
    """
    if not activities:
        return ProjectEVMResult(
            total_bac=Decimal("0"),
            total_pv=Decimal("0"),
            total_ev=Decimal("0"),
            total_ac=Decimal("0"),
            cv=Decimal("0"),
            sv=Decimal("0"),
            cpi=None,
            spi=None,
            eac=None,
            vac=None,
            cpi_interpretation=EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA,
            spi_interpretation=EVM_CONSTANTS.INTERPRETATION_INSUFFICIENT_DATA,
        )

    # Aggregate metrics from all activities
    total_bac = Decimal("0")
    total_pv = Decimal("0")
    total_ev = Decimal("0")
    total_ac = Decimal("0")

    for activity in activities:
        # Convert to Decimal to avoid precision loss
        activity_bac = Decimal(str(activity.bac))
        activity_planned_progress = Decimal(str(activity.planned_progress))
        activity_actual_progress = Decimal(str(activity.actual_progress))
        activity_actual_cost = Decimal(str(activity.actual_cost))

        # Calculate individual activity metrics
        activity_pv = calculate_pv(activity_bac, activity_planned_progress)
        activity_ev = calculate_ev(activity_bac, activity_actual_progress)

        # Accumulate totals
        total_bac += activity_bac
        total_pv += activity_pv
        total_ev += activity_ev
        total_ac += activity_actual_cost

    # Calculate consolidated indices using totals
    total_cv = calculate_cv(total_ev, total_ac)
    total_sv = calculate_sv(total_ev, total_pv)
    total_cpi = calculate_cpi(total_ev, total_ac)
    total_spi = calculate_spi(total_ev, total_pv)
    total_eac = calculate_eac(total_bac, total_cpi)
    total_vac = calculate_vac(total_bac, total_eac)
    cpi_interpretation = interpret_performance_index(total_cpi)
    spi_interpretation = interpret_performance_index(total_spi)

    return ProjectEVMResult(
        total_bac=total_bac,
        total_pv=total_pv,
        total_ev=total_ev,
        total_ac=total_ac,
        cv=total_cv,
        sv=total_sv,
        cpi=total_cpi,
        spi=total_spi,
        eac=total_eac,
        vac=total_vac,
        cpi_interpretation=cpi_interpretation,
        spi_interpretation=spi_interpretation,
    )
