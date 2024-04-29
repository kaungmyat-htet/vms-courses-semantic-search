import os

import pymongo



def get_mongo_client(mongo_uri):
  """Establish connection to the MongoDB."""
  try:
    client = pymongo.MongoClient(mongo_uri)
    print("Connection to MongoDB successful")
    return client
  except pymongo.errors.ConnectionFailure as e:
    print(f"Connection failed: {e}")
    return None

mongo_uri = os.getenv('NVIDIA_API_KEY')
if not mongo_uri:
  print("MONGO_URI not set in environment variables")

mongo_client = get_mongo_client(mongo_uri)

DB_NAME="vms_courses"
COLLECTION_NAME="courses"

db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]
ATLAS_VECTOR_SEARCH_INDEX_NAME = "vector_index"