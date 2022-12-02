from pymongo import MongoClient
import time

MONGODB_URI = "mongodb+srv://google_image_fetch:100%25cows&0%25beavers@googleimagedata.tvztbqw.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URI)

def add_timestamp(image):
    return { "src": image, "timestamp": time.time() }

def insert_many(query, src_images):
    query = query.replace(" ", "_")
    db = client['images']
    collection = db[query]
    data = map(add_timestamp, src_images)

    results = collection.insert_many(data)
    print(len(results.inserted_ids))