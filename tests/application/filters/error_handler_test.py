from flask import Response

from src.application.filters.error_handler import error_handler


def test_when_raise_error_should_return_500():

    @error_handler
    def raise_error():
        raise ValueError('A very specific bad thing happened.')

    error_handled_result = raise_error()
    response = Response(status=500)

    assert error_handled_result.status == response.status


def test_when_not_raise_error_should_return_200():

    @error_handler
    def return_ok():
        return "ok"

    result = return_ok()

    assert result == "ok"
