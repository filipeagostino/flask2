from app import app
from app.controllers import default


app.add_url_rule('/', 'index', default.index)
app.add_url_rule('/read_all', 'readAll', default.listCars, methods=['GET'])
app.add_url_rule('/newcar', 'newItem', default.newItem, methods=['POST'])
app.add_url_rule('/editcar', 'editCar', default.editCar, methods=['PUT'])
app.add_url_rule('/deletecar/<id>', 'deleteCar', default.deleteCar, methods=['DELETE'])