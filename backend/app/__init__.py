"""
Flask application factory.
"""

from flask import Flask
from app.config import config
from app.extensions import db
from app.controllers import activity_blueprint, project_blueprint


def create_app(config_name: str = "development") -> Flask:
    """
    Create and configure the Flask application.

    Args:
        config_name: Configuration environment (development, testing, production).

    Returns:
        Configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(activity_blueprint.bp)
    app.register_blueprint(project_blueprint.bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app
