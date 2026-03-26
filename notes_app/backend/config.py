from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# create database
db = client["notes_db"]