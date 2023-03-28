from app import app
from flask import make_response, jsonify, request, json
from app.models import models
from app.schemas import CarSchema

# Index

def index():
    return '<h1>Inicio da aplicação flask!!</h1>'


# List Cars

def listCars():
    cars_list = models.CarsModel.query.all()
    cars_schema = CarSchema(many=True)
    cars = cars_schema.dump(cars_list)

    if cars:
        return make_response(
            jsonify(
                message='Car list!',
                data=cars
            )
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cars not found!'}
            )
        ), 404

# Add New Car

def newItem():
    car = request.json
    item = models.CarsModel(**car)
    
    models.db.session.add(item)
    models.db.session.commit()

    return make_response(
        jsonify(
            message='Car Added!',
            data=car)
    ), 201
    
# Edit Car

def editCar():
    car = request.json

    search = models.CarsModel.query.get(car['id'])
    
    print(search)

    if search:
        result = models.CarsModel.query.filter(models.CarsModel.id==car['id']).update(dict(make=car['make'],
        model=car['model'],
        year=car['year'],
        value=car['value']
        ))
        models.db.session.commit()

        return make_response(
            jsonify(
                message='Car',
                data=car)
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Car not found!'}
            )
        ), 404

# Delete Car

def deleteCar(id):
    car_id = id

    car = models.CarsModel.query.get(car_id)
    cars_schema = CarSchema()
    check_car = cars_schema.dump(car)

    print(check_car)

    if check_car:
        car = models.CarsModel.query.get(car_id)
        models.db.session.delete(car)
        models.db.session.commit()

        return make_response(
            {'message': 'Car deleted!'}
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Car not found!'}
            )
        ), 404