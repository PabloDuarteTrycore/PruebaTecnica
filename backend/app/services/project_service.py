"""
Service layer for project operations and EVM calculations.
"""

from decimal import Decimal

from app.repositories.activity_repo import ActivityRepository
from app.repositories.project_repo import ProjectRepository
from app.services.evm_service import calculate_activity_evm, calculate_project_evm

project_repo = ProjectRepository()
activity_repo = ActivityRepository()

MONEY_PRECISION = Decimal("0.01")


def _format_money(value: Decimal) -> str:
    """Format monetary EVM values with two decimal places."""
    return str(value.quantize(MONEY_PRECISION))


def _format_project_money(value: Decimal) -> str:
    """Keep plain zero for empty projects and two decimals otherwise."""
    if value == 0 and value.as_tuple().exponent == 0:
        return "0"
    return _format_money(value)


def _serialize_evm_activity(evm_result) -> dict:
    """Convert an ActivityEVMResult to a serializable dictionary."""
    return {
        "pv": _format_money(evm_result.pv),
        "ev": _format_money(evm_result.ev),
        "cv": _format_money(evm_result.cv),
        "sv": _format_money(evm_result.sv),
        "cpi": str(evm_result.cpi) if evm_result.cpi is not None else None,
        "spi": str(evm_result.spi) if evm_result.spi is not None else None,
        "eac": _format_money(evm_result.eac) if evm_result.eac is not None else None,
        "vac": _format_money(evm_result.vac) if evm_result.vac is not None else None,
        "cpi_interpretation": evm_result.cpi_interpretation,
        "spi_interpretation": evm_result.spi_interpretation,
    }


def _serialize_evm_project(evm_result) -> dict:
    """Convert a ProjectEVMResult to a serializable dictionary."""
    return {
        "total_bac": _format_project_money(evm_result.total_bac),
        "total_pv": _format_project_money(evm_result.total_pv),
        "total_ev": _format_project_money(evm_result.total_ev),
        "total_ac": _format_project_money(evm_result.total_ac),
        "cv": _format_project_money(evm_result.cv),
        "sv": _format_project_money(evm_result.sv),
        "cpi": str(evm_result.cpi) if evm_result.cpi is not None else None,
        "spi": str(evm_result.spi) if evm_result.spi is not None else None,
        "eac": _format_project_money(evm_result.eac) if evm_result.eac is not None else None,
        "vac": _format_project_money(evm_result.vac) if evm_result.vac is not None else None,
        "cpi_interpretation": evm_result.cpi_interpretation,
        "spi_interpretation": evm_result.spi_interpretation,
    }


def _build_activity_dict(activity) -> dict:
    """Build a complete activity dictionary with its EVM indicators."""
    evm = calculate_activity_evm(
        bac=Decimal(str(activity.bac)),
        planned_progress=Decimal(str(activity.planned_progress)),
        actual_progress=Decimal(str(activity.actual_progress)),
        actual_cost=Decimal(str(activity.actual_cost)),
    )
    return {
        "id": str(activity.id),
        "project_id": str(activity.project_id),
        "name": activity.name,
        "bac": str(activity.bac),
        "planned_progress": str(activity.planned_progress),
        "actual_progress": str(activity.actual_progress),
        "actual_cost": str(activity.actual_cost),
        "created_at": activity.created_at.isoformat() if activity.created_at else None,
        "updated_at": activity.updated_at.isoformat() if activity.updated_at else None,
        "evm": _serialize_evm_activity(evm),
    }


def _build_project_dict(project, include_activities: bool = True) -> dict:
    """Build a complete project dictionary with consolidated EVM indicators."""
    activities = activity_repo.fetch_activities_by_project(project.id)
    project_evm = calculate_project_evm(activities)

    result = {
        "id": str(project.id),
        "name": project.name,
        "description": project.description,
        "created_at": project.created_at.isoformat() if project.created_at else None,
        "updated_at": project.updated_at.isoformat() if project.updated_at else None,
        "evm": _serialize_evm_project(project_evm),
    }

    if include_activities:
        result["activities"] = [_build_activity_dict(activity) for activity in activities]

    return result


def list_projects_service() -> list[dict]:
    """List all projects with consolidated EVM indicators."""
    projects = project_repo.fetch_all_projects()
    return [_build_project_dict(project, include_activities=False) for project in projects]


def create_project_service(name: str, description: str | None) -> dict:
    """Create a new project."""
    project = project_repo.save_project(name=name, description=description)
    return _build_project_dict(project)


def get_project_detail_service(project_id) -> dict | None:
    """Get the complete detail of a project with all its activities."""
    project = project_repo.fetch_project_by_id(str(project_id))
    if project is None:
        return None
    return _build_project_dict(project)


def update_project_service(project_id, fields: dict) -> dict | None:
    """Update project fields."""
    project = project_repo.fetch_project_by_id(str(project_id))
    if project is None:
        return None
    updated_project = project_repo.update_project_fields(project, fields)
    return _build_project_dict(updated_project)


def delete_project_service(project_id) -> bool:
    """Delete a project and all its activities."""
    project = project_repo.fetch_project_by_id(str(project_id))
    if project is None:
        return False
    project_repo.remove_project(project)
    return True
