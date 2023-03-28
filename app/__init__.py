from flask import Flask
from app.models import models
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:toor@localhost/cars"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


models.db.init_app(app)

with app.app_context():
    models.db.create_all()

from app.routes import routes