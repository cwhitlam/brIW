#!/usr/bin/python
import unittest

loader = unittest.TestLoader()
test_dir = "/home/chris/repos/miniproject/test/"
test_suite = loader.discover(test_dir)
unittest.TextTestRunner().run(test_suite)