"""
Project blueprint routes.
"""

from flask import Blueprint, jsonify

bp = Blueprint("project", __name__, url_prefix="/projects")


@bp.get("")
def list_projects():
    """
    Temporary projects endpoint used to keep the backend bootable.
    """
    return jsonify([])
