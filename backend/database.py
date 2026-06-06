from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vssharsha88_db_user:ylPXORSSxLZYiqkj@cluster0.ba7eymv.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["ai_recruitment"]

reports_collection = db["candidate_reports"]