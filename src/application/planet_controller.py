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
    return Planet.from_json(request.get_json())


@planet_controller.route('/planet', methods=['GET'])
@error_handler
@has_valid_data_in_response
def get():
    repository = PlanetRepository()

    return repository.list()


@planet_controller.route('/planet/id', methods=['GET'])
@error_handler
@has_valid_data_in_response
def get_id():
    repository = PlanetRepository()

    return repository.get_by_id("5c6c58558b11406e424cf011")


@planet_controller.route('/planet/name', methods=['GET'])
@error_handler
@has_valid_data_in_response
def get_name():
    repository = PlanetRepository()

    return repository.get_by_name("Alderaan")


@planet_controller.route('/planet', methods=['DELETE'])
@error_handler
def delete():
    return "delete"
