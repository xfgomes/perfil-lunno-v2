from flask import Blueprint, request, jsonify
from sqlalchemy.orm import Session
from ..models.assessment import Assessment
from ..app import db_engine

bp = Blueprint("org", __name__, url_prefix="/api/org")

@bp.get("/dashboard")
def org_dash():
    with Session(db_engine) as s:
        rows = s.query(Assessment).all()
        count = len(rows)
        return jsonify({"count": count})
