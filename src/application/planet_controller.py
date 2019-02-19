from flask import Blueprint, request
from src.application.filters.error_handler import error_handler
from src.application.filters.response_data_validator import has_valid_data_in_response
from src.domain.entities.planet import Planet
from src.repositories.planet_repository import PlanetRepository

planet_controller = Blueprint('planet', __name__, template_folder='templates')


@planet_controller.route('/planet', methods=['POST'])
@error_handler
@has_valid_data_in_response
def post():
    repository = PlanetRepository()

    planet = Planet.from_json(request.get_json())

    return repository.insert(planet)


@planet_controller.route('/planet', methods=['GET'])
@error_handler
@has_valid_data_in_response
def get():
    repository = PlanetRepository()

    id = request.args.get('id')
    name = request.args.get('name')

    if id:
        return repository.get_by_id(id)
    elif name:
        return repository.get_by_name(name)
    else:
        return repository.list()


@planet_controller.route('/planet', methods=['DELETE'])
@error_handler
@has_valid_data_in_response
def delete():
    repository = PlanetRepository()

    id = request.args.get('id')

    if id:
        return repository.delete_by_id(id)
    else:
        return None
