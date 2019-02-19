from src.domain.entities.planet import Planet
from src.repositories.mappers.planet_mapper import PlanetMapper
from src.repositories.planet_collection import PlanetCollection


class PlanetRepository(object):

    def insert_list(self, planets: list):
        collection = PlanetCollection.get_collection()

        for planet in planets:
            self.insert(planet, collection)

    def insert(self, planet: Planet, collection):
        data = PlanetMapper.domain_to_data(planet)

        collection.insert_one(data)

    def list(self):
        collection = PlanetCollection.get_collection()

        datas = collection.find()

        return [PlanetMapper.data_to_domain(data) for data in datas]
