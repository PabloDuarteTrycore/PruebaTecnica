"""
Flask application factory.
"""

from flask import Flask

from app.config import Config, config
from app.extensions import api, db, migrate


def create_app(config_name: str | type[Config] = "development") -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name: Configuration environment name or config class.

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)

    if isinstance(config_name, str):
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from app.errors.handlers import register_error_handlers

    register_error_handlers(app)

    from app.controllers.activity_blueprint import blp as activity_blp
    from app.controllers.project_blueprint import blp as project_blp

    api.register_blueprint(project_blp)
    api.register_blueprint(activity_blp)

    return app
