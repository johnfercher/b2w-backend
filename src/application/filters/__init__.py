from flask import Blueprint, request
from src.application.filters.error_handler import error_handler

bird_controller = Blueprint('bird', __name__, template_folder='templates')




@bird_controller.route('/bird', methods=['POST'])
@error_handler
def post():
    bird = Bird()
    bird.from_json(request.get_json())

    repository = BirdRepository()

    return repository.save(bird)
