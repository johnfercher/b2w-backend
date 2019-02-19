from bson import ObjectId

from src.domain.entities.planet import Planet
from src.repositories.mappers.planet_mapper import PlanetMapper
from src.repositories.planet_collection import PlanetCollection


class PlanetRepository(object):

    def insert_list(self, planets: list):
        collection = PlanetCollection.get_collection()

        for planet in planets:
            self.insert(planet, collection)

    def insert(self, planet: Planet, collection: PlanetCollection = None):
        if collection is None:
            collection = PlanetCollection.get_collection()

        data = PlanetMapper.domain_to_data(planet)

        data["_id"] = collection.insert_one(data).inserted_id

        return PlanetMapper.data_to_domain(data)

    def list(self):
        collection = PlanetCollection.get_collection()

        datas = collection.find()

        return [PlanetMapper.data_to_domain(data) for data in datas]

    def get_by_id(self, id):
        collection = PlanetCollection.get_collection()

        data = collection.find_one({'_id': ObjectId(id)})

        return PlanetMapper.data_to_domain(data)

    def get_by_name(self, name):
        collection = PlanetCollection.get_collection()

        data = collection.find_one({'name': name})

        return PlanetMapper.data_to_domain(data)

    def delete_by_id(self, id):
        collection = PlanetCollection.get_collection()

        data = collection.find_one({'_id': ObjectId(id)})

        collection.delete_one({'_id': ObjectId(id)})

        return PlanetMapper.data_to_domain(data)
