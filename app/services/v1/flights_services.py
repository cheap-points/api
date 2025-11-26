from fastapi import Response
from mongo_handler import ConnectionHandler
import os, json
from dotenv import load_dotenv
load_dotenv()

db_host       = os.getenv("MONGO_HOST")
db_username   = os.getenv("MONGO_USERNAME")
db_password   = os.getenv("MONGO_PASSWORD")
db_database   = os.getenv("MONGO_DATABASE")
db_collection = os.getenv("MONGO_COLLECTION")

db = ConnectionHandler(db_host, db_username, db_password, db_database, db_collection)

#def search(origin: str = None, destination: str = None, day: int = None, month: int = None, year: int = None, price: int = None):
def search(**kwargs):
    
    sort={
        'price': 1
    }.items()
    max_time_ms = 60000
    #results = db.collection.find(filter=filter, sort=sort, max_time_ms=max_time_ms)
    
    filter = {k: v for k, v in kwargs.items() if v is not None}
    
    raw = db.collection.find(filter, {'_id': 0})
    results = list(raw)
    print (results)
    data = {"flights":results}
    return data