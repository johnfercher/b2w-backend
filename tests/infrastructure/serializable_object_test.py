from src.infrastructure.serializable_object import SerializableObject


def test_to_json_should_performly_properly():
    class Test(SerializableObject):

        def __init__(self):
            self.any1 = "123"
            self.any2 = "abc"

    # arrange
    test = Test()

    # act
    json = test.to_json()

    # assert
    assert json == "{\n    \"any1\": \"123\",\n    \"any2\": \"abc\"\n}"
