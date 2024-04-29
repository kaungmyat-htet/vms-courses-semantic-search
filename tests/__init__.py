#-*- coding:utf-8 -*-
"""
Unit test.

Each file in tests/ is for each main package.
"""
import sys
import unittest

loader = unittest.TestLoader()
testSuits = loader.discover("tests")
testRunner = unittest.TextTestRunner(verbosity=1)
testRunner.run(testSuits)