from pymongo import MongoClient

# uri = "mongodb+srv://m220-user:m220-pass@m220-lessons-mcxlm.mongodb.net/test"
uri = "mongodb+srv://m220student:m220password@mflix-8cfzz.mongodb.net/test"

mc = MongoClient(uri)

print (mc.stats)