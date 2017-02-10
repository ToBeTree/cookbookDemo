import pymongo
from pymongo import MongoClient

# 数据库链接方式
client = MongoClient()
# client = MongoClient('mongodb://127.0.0.1:27017')
# client = MongoClient('localhost','27017')
db = client.test_database
print(db)
print(client.database_names())
