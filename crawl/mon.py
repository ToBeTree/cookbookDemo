import pymongo
from pymongo import MongoClient
# 命令行启动mongo
# mongod --config "D:Program Files (x86)\MongoDB\bin\mongodb.config
# https://www.zybuluo.com/hwk603/note/208284
# 数据库链接方式
# client = MongoClient()
# client = MongoClient('mongodb://127.0.0.1:27017')
client = MongoClient('localhost', '27017')
db = client.test_database
print(db)
print(client.database_names())
data = {
    'name': 'tobetree',
    'url': 'tobetree/people'
}
post = db.posts
post.insert_one(data)

a = post.find_one('name', 'tobetree')
print(a)
