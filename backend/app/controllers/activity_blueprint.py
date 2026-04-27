"""
Activity blueprint routes.
"""

from flask import Blueprint, jsonify

bp = Blueprint("activity", __name__, url_prefix="/activities")


@bp.get("")
def list_activities():
    """
    Temporary activities endpoint used to keep the backend bootable.
    """
    return jsonify([])
