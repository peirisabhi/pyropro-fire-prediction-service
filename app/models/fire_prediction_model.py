from pymongo import MongoClient


class database:
    def __init__(self):
        try:
            self.db_client = MongoClient(host='localhost', port=27017)
            self.db = self.db_client.pyropro_fire_prediction_db  # your database name
            self.mongo_col = self.db.fire_predictions  # your collection/table name
            print('database connected')
        except Exception as e:
            print(e)

    def insert(self, document):
        self.mongo_col.insert_one(document)

    def findAll(self):
        result = self.mongo_col.find()
        return result
