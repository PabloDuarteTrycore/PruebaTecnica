"""
Flask-smorest Blueprint for activity endpoints.
"""

from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from app.schemas.activity_schema import (
    ActivityCreateSchema,
    ActivityResponseSchema,
    ActivityUpdateSchema,
)
from app.services.activity_service import (
    create_activity_service,
    delete_activity_service,
    list_activities_service,
    update_activity_service,
)

blp = Blueprint(
    "activities",
    __name__,
    url_prefix="/api/v1",
    description="Gestion de actividades y sus indicadores EVM individuales",
)


@blp.route("/projects/<uuid:project_id>/activities")
class ActivityList(MethodView):
    """Activity collection endpoints for a project."""

    @blp.response(200, ActivityResponseSchema(many=True))
    def get(self, project_id):
        """List all activities for a project."""
        activities = list_activities_service(project_id)
        if activities is None:
            abort(404, description="Project not found")
        return activities, 200

    @blp.arguments(ActivityCreateSchema)
    @blp.response(201, ActivityResponseSchema)
    def post(self, payload, project_id):
        """Create a new activity in a project."""
        activity = create_activity_service(project_id=project_id, data=payload)
        if activity is None:
            abort(404, description="Project not found")
        return activity, 201


@blp.route("/activities/<uuid:activity_id>")
class ActivityDetail(MethodView):
    """Activity detail endpoints."""

    @blp.arguments(ActivityUpdateSchema)
    @blp.response(200, ActivityResponseSchema)
    def put(self, payload, activity_id):
        """Update an activity and recalculate its EVM."""
        activity = update_activity_service(activity_id=activity_id, fields=payload)
        if activity is None:
            abort(404, description="Activity not found")
        return activity, 200

    @blp.response(204)
    def delete(self, activity_id):
        """Delete an activity."""
        deleted = delete_activity_service(activity_id)
        if not deleted:
            abort(404, description="Activity not found")
        return "", 204
