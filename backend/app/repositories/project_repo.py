"""
Repository for Project model data access.
"""

from app.extensions import db
from app.models.project import Project


class ProjectRepository:
    """Encapsulates all database access for Project."""

    def fetch_all_projects(self) -> list[Project]:
        """Fetch all projects ordered by creation date descending."""
        return (
            db.session.execute(db.select(Project).order_by(Project.created_at.desc()))
            .scalars()
            .all()
        )

    def fetch_project_by_id(self, project_id) -> Project | None:
        """Fetch a project by its ID."""
        return db.session.get(Project, project_id)

    def save_project(self, name: str, description: str | None) -> Project:
        """Create and save a new project."""
        project = Project(name=name, description=description)
        db.session.add(project)
        db.session.commit()
        db.session.refresh(project)
        return project

    def update_project_fields(self, project: Project, fields: dict) -> Project:
        """Update specified fields on a project."""
        for field, value in fields.items():
            setattr(project, field, value)
        db.session.commit()
        db.session.refresh(project)
        return project

    def remove_project(self, project: Project) -> None:
        """Delete a project."""
        db.session.delete(project)
        db.session.commit()
