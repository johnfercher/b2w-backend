from src.infrastructure.json_parser import JsonParser


def test_try_get_parameter_when_exists_should_not_return_none():
    # arrage
    json = { "key": "value"}

    # act
    result = JsonParser.try_get_parameter(json, "key")

    # assert
    assert result is not None
    assert result is "value"


def test_try_get_parameter_when_doesnt_exists_should_return_none():
    # arrage
    json = { "key": "value"}

    # act
    result = JsonParser.try_get_parameter(json, "key2")

    # assert
    assert result is None
