from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from .config import Config
from .models.base import Base
from .models.user import User, Organization
from .models.assessment import Assessment

jwt = JWTManager()
db_engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}}, supports_credentials=True)
    jwt.init_app(app)

    Base.metadata.create_all(db_engine)

    from .api.auth import bp as auth_bp
    from .api.users import bp as users_bp
    from .api.items import bp as items_bp
    from .api.reports import bp as reports_bp
    from .api.org import bp as org_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(org_bp)

    @app.get("/health")
    def health():
        return {"status":"ok"}

    return app

app = create_app()
