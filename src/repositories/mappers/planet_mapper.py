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
                    "climate": domain.climate
                }
            else:
                return {
                    "_id": ObjectId(),
                    "name": domain.name,
                    "terrain": domain.terrain,
                    "climate": domain.climate
                }

    @classmethod
    def data_to_domain(cls, data):
        if data:
            return Domain(data["name"], data["terrain"], data["climate"], str(data["_id"]))
