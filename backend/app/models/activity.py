"""
Activity model definition.
"""

import uuid
from decimal import Decimal
from datetime import datetime
from app.extensions import db


class Activity(db.Model):
    """Activity model for EVM Project Tracker."""

    __tablename__ = "activities"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    project_id = db.Column(
        db.String(36), db.ForeignKey("projects.id", ondelete="CASCADE"), nullable=False
    )
    name = db.Column(db.String(255), nullable=False)
    bac = db.Column(db.Numeric(15, 2), nullable=False)  # Budget at Completion
    planned_progress = db.Column(db.Numeric(5, 2), nullable=False)  # 0-100
    actual_progress = db.Column(db.Numeric(5, 2), nullable=False)  # 0-100
    actual_cost = db.Column(db.Numeric(15, 2), nullable=False)  # AC
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationship
    project = db.relationship("Project", back_populates="activities")

    def __repr__(self):
        return f"<Activity {self.name}>"
