from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("users", __name__, url_prefix="/api/users")

@bp.get("/profile")
@jwt_required()
def profile():
    return jsonify({"user": get_jwt_identity()})
