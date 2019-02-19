from random import randint

from flask import Response

from src.application.filters.response_data_validator import has_valid_data_in_response
from src.domain.entities.planet import Planet


def test_when_return_is_none_should_return_404():

    @has_valid_data_in_response
    def return_none():
        return None

    result = return_none()
    response = Response(status=404)

    assert result.status == response.status


def test_when_return_is_object_should_return_200():

    @has_valid_data_in_response
    def return_object():
        return Planet.random()

    result = return_object()
    response = Response(status=200)

    assert result.status == response.status
    assert result.json is not None


def test_when_return_is_list_should_return_200():

    @has_valid_data_in_response
    def return_list():
        return [Planet.random() for i in range(1, randint(2, 10))]

    result = return_list()
    response = Response(status=200)

    assert result.status == response.status
    assert result.json is not None
