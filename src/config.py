"""
Global Configuration File
"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv, dotenv_values 

load_dotenv()

@dataclass
class MyConfig:
    mongo_uri: str = os.getenv("MONGO_URI")
    DB_NAME: str = os.getenv("DB_NAME")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME")
    ATLAS_VECTOR_SEARCH_INDEX_NAME: str = os.getenv("ATLAS_VECTOR_SEARCH_INDEX_NAME")