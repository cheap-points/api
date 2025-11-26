# import json, requests
from pymongo import MongoClient     # type: ignore

class ConnectionHandler:

    def __init__(self,
                    mongodb_host: str,
                    username: str,
                    password: str,
                    database: str,
                    collection: str
    ):
        self.connection_string = f'mongodb+srv://{username}:{password}@{mongodb_host}'
        self.client = MongoClient(self.connection_string)
        self.db_connection = self.client[database]
        self.collection = self.db_connection.get_collection(collection)