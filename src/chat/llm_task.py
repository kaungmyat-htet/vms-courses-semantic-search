import os
from typing import List

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from langchain_community.vectorstores import MongoDBAtlasVectorSearch

from config import MyConfig

# Load ENV variables
mongo_uri = MyConfig.mongo_uri
DB_NAME = MyConfig.DB_NAME
COLLECTION_NAME = MyConfig.COLLECTION_NAME
ATLAS_VECTOR_SEARCH_INDEX_NAME = MyConfig.ATLAS_VECTOR_SEARCH_INDEX_NAME

# Embedder Model
embedder = NVIDIAEmbeddings(model="nvolveqa_40k", model_type=None)

# Mongo Atlas Vector Search
vector_search = MongoDBAtlasVectorSearch.from_connection_string(
    mongo_uri,
    DB_NAME + "." + COLLECTION_NAME,
    embedder,
    index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,
)


def search_courses(query: str, k: int) -> List:
    courses_list = []
    results = vector_search.similarity_search_with_score(
        query=query, k=k
    )

    # Display results
    for result in results:
        course_data = {
            "id": result[0].metadata['id'],
            "course_id": result[0].metadata['metadata']['id'],
            "course_title": result[0].metadata['metadata']['title'],
            "major": result[0].metadata['metadata']['major'],
            "category":  result[0].metadata['metadata']['category'],
            "course_description":  result[0].metadata['metadata']['course_detail'],
            "similarity_score": result[1]
        }
        courses_list.append(course_data)

    return courses_list