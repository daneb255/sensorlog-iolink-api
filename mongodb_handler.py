import urllib.parse
from pymongo import MongoClient
from core.config import MONGODB_DB, MONGODB_HOST, MONGODB_USER, MONGODB_PASSWORD

username = urllib.parse.quote_plus(MONGODB_USER)
password = urllib.parse.quote_plus(MONGODB_PASSWORD)

MongoClient(f'mongodb://{username}:{password}@{MONGODB_HOST}')
