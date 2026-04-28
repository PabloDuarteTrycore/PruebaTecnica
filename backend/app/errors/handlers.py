"""
Centralized error handlers for Flask application.
"""

from flask import jsonify


def register_error_handlers(app):
    """Register all error handlers with the Flask application."""

    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify(
                {
                    "error": "not_found",
                    "message": str(error.description)
                    if hasattr(error, "description")
                    else "Resource not found",
                }
            ),
            404,
        )

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (
            jsonify(
                {
                    "error": "method_not_allowed",
                    "message": "HTTP method not allowed for this endpoint",
                }
            ),
            405,
        )

    @app.errorhandler(422)
    def unprocessable_entity(error):
        messages = error.data.get("messages", {}) if hasattr(error, "data") else {}
        return (
            jsonify(
                {
                    "error": "validation_error",
                    "message": "Invalid input data",
                    "details": messages,
                }
            ),
            422,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify(
                {
                    "error": "internal_server_error",
                    "message": "An unexpected error occurred",
                }
            ),
            500,
        )
