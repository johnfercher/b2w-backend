import uuid
from src.infrastructure.json_parser import JsonParser
from src.infrastructure.serializable_object import SerializableObject


class Planet(SerializableObject):

    def __init__(self, name: str, climate: str, terrain: str, id: str = None):
        self.name = name
        self.climate = climate
        self.terrain = terrain
        self.id = id

    @classmethod
    def random(cls):
        name = str(uuid.uuid4())
        climate = str(uuid.uuid4())
        terrain = str(uuid.uuid4())
        id = str(uuid.uuid4())

        return cls(name=name, climate=climate, terrain=terrain, id=id)

    @classmethod
    def from_json(cls, json):
        name = JsonParser.try_get_parameter(json, "name")
        climate = JsonParser.try_get_parameter(json, "climate")
        terrain = JsonParser.try_get_parameter(json, "terrain")
        id = JsonParser.try_get_parameter(json, "id")

        return cls(name=name, climate=climate, terrain=terrain, id=id)
