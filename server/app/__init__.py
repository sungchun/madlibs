import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://madlibs_dev:madlibs_dev@localhost:5432/madlibs_dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .routes import routes
    app.register_blueprint(routes.api)

    return app

def register_extensions(app: Flask) -> None:
    from app import models
    from app.extensions import db, migrate

    db.init_app(app)
    with app.app.context():
        db.create_all()
    migrate.init_app(app, db=db)


