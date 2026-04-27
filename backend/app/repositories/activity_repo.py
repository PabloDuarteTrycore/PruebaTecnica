"""
Repository for Activity model data access.
"""

from app.extensions import db
from app.models.activity import Activity


class ActivityRepository:
    """Encapsulates all database access for Activity."""

    def fetch_activities_by_project(self, project_id) -> list[Activity]:
        """Fetch all activities for a given project."""
        return (
            db.session.execute(
                db.select(Activity)
                .where(Activity.project_id == project_id)
                .order_by(Activity.created_at.desc())
            )
            .scalars()
            .all()
        )

    def fetch_activity_by_id(self, activity_id) -> Activity | None:
        """Fetch an activity by its ID."""
        return db.session.get(Activity, activity_id)

    def save_activity(self, project_id, data: dict) -> Activity:
        """Create and save a new activity."""
        activity = Activity(project_id=project_id, **data)
        db.session.add(activity)
        db.session.commit()
        db.session.refresh(activity)
        return activity

    def update_activity_fields(self, activity: Activity, fields: dict) -> Activity:
        """Update specified fields on an activity."""
        for field, value in fields.items():
            setattr(activity, field, value)
        db.session.commit()
        db.session.refresh(activity)
        return activity

    def remove_activity(self, activity: Activity) -> None:
        """Delete an activity."""
        db.session.delete(activity)
        db.session.commit()
