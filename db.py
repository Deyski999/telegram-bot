from pymongo import MongoClient
import certifi

MONGODB_URI = "mongodb+srv://ghaithalrahi:Searchersof99!@deyski999.j1l0sp5.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(
    MONGODB_URI,
    tls=True,
    tlsAllowInvalidCertificates=True,
    tlsCAFile=certifi.where()
)

db = client["telegram_bot"]
users_collection = db["users"]