from bson import ObjectId

from src.domain.entities.planet import Planet as Domain


class PlanetMapper(object):

    @classmethod
    def domain_to_data(cls, domain: Domain):
        if domain:
            if domain.id:
                return {
                    "_id": domain.id,
                    "name": domain.name,
                    "terrain": domain.terrain,
                    "climate": domain.climate,
                    "qtd_movies": domain.qtd_movies
                }
            else:
                return {
                    "_id": ObjectId(),
                    "name": domain.name,
                    "terrain": domain.terrain,
                    "climate": domain.climate,
                    "qtd_movies": domain.qtd_movies
                }

    @classmethod
    def data_to_domain(cls, data):
        if data:
            return Domain(name=data["name"], terrain=data["terrain"], climate=data["climate"], qtd_movies=int(data["qtd_movies"]), id=str(data["_id"]))
