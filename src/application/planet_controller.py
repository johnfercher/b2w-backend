from flask import Blueprint
from src.application.filters.error_handler import error_handler
planet_controller = Blueprint('planet', __name__, template_folder='templates')


@planet_controller.route('/planet', methods=['POST'])
@error_handler
def post():
    return "post"


@planet_controller.route('/planet', methods=['GET'])
@error_handler
def get():
    return "get"


@planet_controller.route('/planet/id', methods=['GET'])
@error_handler
def get_id():
    return "get_id"


@planet_controller.route('/planet/name', methods=['GET'])
@error_handler
def get_name():
    return "get_name"


@planet_controller.route('/planet', methods=['DELETE'])
@error_handler
def delete():
    return "delete"
