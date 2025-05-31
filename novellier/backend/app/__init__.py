from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Placeholder for AI services initialization if needed
    # from .services.ai_module import init_ai_services
    # init_ai_services(app)

    return app
