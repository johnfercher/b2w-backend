import uuid
from src.infrastructure.json_parser import JsonParser
from src.infrastructure.serializable_object import SerializableObject


class Planet(SerializableObject):

    def __init__(self, name: str, climate: str, terrain: str):
        self.name = name
        self.climate = climate
        self.terrain = terrain

    @classmethod
    def random(cls):
        name = str(uuid.uuid4())
        climate = str(uuid.uuid4())
        terrain = str(uuid.uuid4())

        return cls(name=name, climate=climate, terrain=terrain)

    @classmethod
    def from_json(cls, json):
        name = JsonParser.try_get_parameter(json, "name")
        climate = JsonParser.try_get_parameter(json, "climate")
        terrain = JsonParser.try_get_parameter(json, "terrain")

        return cls(name=name, climate=climate, terrain=terrain)
