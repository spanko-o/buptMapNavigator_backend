from flask import Flask
from .routes import main as main_blueprint
from config import Config
from flask_migrate import Migrate
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(main_blueprint)
    return app
