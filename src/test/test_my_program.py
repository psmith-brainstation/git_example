import unittest
import sys
import logging
logger = logging.getLogger()
logger.level = logging.DEBUG
logger.addHandler(logging.StreamHandler(sys.stdout))

class TestMyFunctionMethods(unittest.TestCase):

    def test_my_function(self):
        assert logging.getLogger().info("Hello World!")

if __name__ == '__main__':
    unittest.main()