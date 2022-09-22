import os

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://madlibs_dev:madlibs_dev@db/madlibs_dev'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from app.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)

    from app import models

    from .routes import routes

    app.register_blueprint(routes.api)

    return app

