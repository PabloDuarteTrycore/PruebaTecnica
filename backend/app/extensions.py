"""
Flask extensions initialization.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api

# Database extension
db = SQLAlchemy()

# Migration extension
migrate = Migrate()

# API extension (flask-smorest for OpenAPI/Swagger)
api = Api()
