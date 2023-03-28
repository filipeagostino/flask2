from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer(), nullable=False)
    value = db.Column(db.Float(precision=2), unique=False, nullable=False)