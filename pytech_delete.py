import pymongo
from pymongo import MongoClient




cluster = MongoClient("mongodb+srv://johnr:admin@cluster0.isvrbfp.mongodb.net/?retryWrites=true&w=majority")
db = cluster["pytech"]
collection = db["student"]

post1 = {"student_id": 1007, "firstname": "john", "lastname": "rosales"}
post2 = {"student_id": 1008, "firstname": "james", "lastname": "smith"}
post3 = {"student_id": 1009, "firstname": "david", "lastname": "jones"}


results = collection.delete_one({"student_id": 1007})




