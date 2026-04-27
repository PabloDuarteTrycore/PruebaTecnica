"""
Service layer for activity operations.
"""

from app.repositories.project_repo import ProjectRepository
from app.repositories.activity_repo import ActivityRepository
from app.services.project_service import _build_activity_dict

project_repo = ProjectRepository()
activity_repo = ActivityRepository()


def list_activities_service(project_id) -> list[dict] | None:
    """List all activities for a project."""
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    activities = activity_repo.fetch_activities_by_project(project_id)
    return [_build_activity_dict(a) for a in activities]


def create_activity_service(project_id, data: dict) -> dict | None:
    """Create a new activity in a project."""
    project = project_repo.fetch_project_by_id(project_id)
    if project is None:
        return None
    activity = activity_repo.save_activity(project_id=project_id, data=data)
    return _build_activity_dict(activity)


def update_activity_service(activity_id, fields: dict) -> dict | None:
    """Update activity fields."""
    activity = activity_repo.fetch_activity_by_id(activity_id)
    if activity is None:
        return None
    updated = activity_repo.update_activity_fields(activity, fields)
    return _build_activity_dict(updated)


def delete_activity_service(activity_id) -> bool:
    """Delete an activity."""
    activity = activity_repo.fetch_activity_by_id(activity_id)
    if activity is None:
        return False
    activity_repo.remove_activity(activity)
    return True
