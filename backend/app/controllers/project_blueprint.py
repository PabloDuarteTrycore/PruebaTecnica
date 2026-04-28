"""
Flask-smorest Blueprint for project endpoints.
"""

from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from app.schemas.project_schema import (
    ProjectCreateSchema,
    ProjectResponseSchema,
    ProjectUpdateSchema,
)
from app.services.project_service import (
    create_project_service,
    delete_project_service,
    get_project_detail_service,
    list_projects_service,
    update_project_service,
)

blp = Blueprint(
    "projects",
    __name__,
    url_prefix="/api/v1/projects",
    description="Gestion de proyectos y sus indicadores EVM consolidados",
)


@blp.route("/")
class ProjectList(MethodView):
    """Project collection endpoints."""

    @blp.response(200, ProjectResponseSchema(many=True))
    def get(self):
        """List all projects with consolidated EVM indicators."""
        projects = list_projects_service()
        return projects, 200

    @blp.arguments(ProjectCreateSchema)
    @blp.response(201, ProjectResponseSchema)
    def post(self, payload):
        """Create a new project."""
        project = create_project_service(
            name=payload["name"],
            description=payload.get("description"),
        )
        return project, 201


@blp.route("/<uuid:project_id>")
class ProjectDetail(MethodView):
    """Project detail endpoints."""

    @blp.response(200, ProjectResponseSchema)
    def get(self, project_id):
        """Return a project with its activities and consolidated EVM."""
        project = get_project_detail_service(project_id)
        if project is None:
            abort(404, description="Project not found")
        return project, 200

    @blp.arguments(ProjectUpdateSchema)
    @blp.response(200, ProjectResponseSchema)
    def put(self, payload, project_id):
        """Update project fields."""
        project = update_project_service(project_id, payload)
        if project is None:
            abort(404, description="Project not found")
        return project, 200

    @blp.response(204)
    def delete(self, project_id):
        """Delete a project and its activities."""
        deleted = delete_project_service(project_id)
        if not deleted:
            abort(404, description="Project not found")
        return "", 204
