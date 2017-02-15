import pymongo
from pymongo import MongoClient

client = MongoClient('10.125.194.46', 30000)

social = client.social
print(social)
t = social.socialTopic
a = t.find(_id: ObjectId('56de57c86af1481b7ebce8e7'))
print(a)
