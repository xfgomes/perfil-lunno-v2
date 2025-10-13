from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import Session
from ..models.user import User
from ..app import db_engine

bp = Blueprint("auth", __name__, url_prefix="/api/auth")
bcrypt = Bcrypt()

@bp.post("/register")
def register():
    data = request.json or {}
    with Session(db_engine) as s:
        if s.query(User).filter_by(email=data.get("email")).first():
            return jsonify({"error":"Email já cadastrado"}), 400
        u = User(email=data["email"], name=data.get("name",""), password_hash=bcrypt.generate_password_hash(data["password"]).decode())
        s.add(u); s.commit()
        return jsonify({"id": u.id, "email": u.email})

@bp.post("/login")
def login():
    data = request.json or {}
    with Session(db_engine) as s:
        u = s.query(User).filter_by(email=data.get("email")).first()
        if not u or not bcrypt.check_password_hash(u.password_hash, data.get("password","")):
            return jsonify({"error":"Credenciais inválidas"}), 401
        token = create_access_token(identity={"user_id": u.id, "role": "user"})
        return jsonify({"access_token": token})
