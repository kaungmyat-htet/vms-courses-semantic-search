import unittest
from typing import List

from src.chat.llm_task import search_courses

class TestChatPackage(unittest.TestCase):
    def setUp(self) -> None:
        self.query = "Are there any courses related to data science?"
    
    def test_search_courses(self):
        self.assertIsInstance(search_courses(self.query, 5), List)