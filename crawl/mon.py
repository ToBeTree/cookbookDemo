import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from random import randint
# 命令行启动mongo
# mongod --config "D:Program Files (x86)\MongoDB\bin\mongodb.config
# https://www.zybuluo.com/hwk603/note/208284
# 数据库链接方式
# client = MongoClient()
# client = MongoClient('mongodb://127.0.0.1:27017')
client = MongoClient('localhost', 27017)
# 得到数据库实例
# 就算数据库不存在也不要紧，只要你插入数据就会自动创建
db = client.test_database
# 先要启动数据库和客户端
#cd /Users/wangpegnfei/Desktop/mongodb-osx-x86_64-2.4.6/bin
#./mongoexport -d 数据库名 -c 表名 --csv -f 要导出的字段名，每个字段名以逗号隔开 -o 具体地址(如果不加具体地址，则默认为导出到bin目录下)/要导出的文件名.csv deprecated
#./mongoexport -d 数据库名 -c 表名 --type=csv -f 要导出的字段名，每个字段名以逗号隔开 -o 具体地址(如果不加具体地址，则默认为导出到bin目录下)/要导出的文件名.csv
#mongoexport -d douban -c movie_250 --csv -f title,url,rating_num -o E://douban.csv
print(db)
print(client.database_names())
data = {
    'name': 'tobetree',
    'url': 'tobetree/people',
    'profile': 'github.com/tobetree',
    'password': randint(0, 10)
}
# 得到集合实例（相当于sql里面的表）
# psot = db['posts']
post = db.posts
# id = post.insert_one(data)
# print(id)
# id_1 = post.insert_one(data).inserted_id()
# print(id_1)

# a = post.find({'_id': ObjectId("58a2d85c74cf3028dc45e533")})
a = post.find({'password': {'$lt': 6}}).sort('password')
c = post.find_one({'profie': 'github.com/tobetree'})
print(c)
# print(len(a))
i = 0
for b in a:
    i += 1
    print(b)
    print(b['_id'])
a.close()
print(i)
