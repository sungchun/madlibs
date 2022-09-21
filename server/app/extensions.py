from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
