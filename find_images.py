from pymongo import MongoClient
import random_image_selector

MONGODB_URI = "mongodb+srv://google_image_fetch:100%25cows&0%25beavers@googleimagedata.tvztbqw.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URI)
db = client['images']

def find_random_images():
    collection_names = db.list_collection_names()
    collection_name = random_image_selector.select_topic(collection_names)
    print(collection_name)
    srcs = find_all(collection_name)
    srcs = [src['src'] for src in srcs]
    images = random_image_selector.select_images(srcs)
    print(len(images))
    return images

def find_all(collection_name):
    collection = db[collection_name]
    results = collection.find({})
    return results