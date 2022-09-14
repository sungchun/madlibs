import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:banana@localhost:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import routes
    app.register_blueprint(routes.api)

    return app

def register_extensions(app: Flask) -> None:
    from app import models
    from app.extensions import db, migrate, ma

    db.init_app(app)
    migrate.init_app(app, db=db)
    kip_auth.init_app(app)

