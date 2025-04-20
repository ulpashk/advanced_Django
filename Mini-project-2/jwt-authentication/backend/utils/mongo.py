from pymongo import MongoClient

MONGO_DB = {
    'host': 'localhost',
    'port': 27017,
    'db_name': 'resume_ai',
}

client = MongoClient(MONGO_DB['host'], MONGO_DB['port'])
mongo_db = client[MONGO_DB['db_name']]