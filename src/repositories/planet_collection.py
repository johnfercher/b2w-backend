from pymongo import MongoClient


class PlanetCollection(object):

    @classmethod
    def get_collection(self):
        client = MongoClient('mongodb://localhost:27017/')
        database = client['b2w-database']
        collection = database['pĺanet-collection']

        return collection
