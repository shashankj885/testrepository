import pymongo
client = pymongo.MongoClient("mongodb+srv://shashankj885:Covid2019@shashank.qoojyid.mongodb.net/?retryWrit es=true&w=majority")
db = client.test
print(db)
d={
    "name":"shashank",
    "email_id" : "shahnwbhbavmc",
    "surname":"jaiswal"
}
db1=client['mongotest']
coll =db1['test']
coll.insert_one(d)