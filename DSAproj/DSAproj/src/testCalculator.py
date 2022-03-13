import unittest

from pandas import array
from queue import Queue
from calculator import convert
from calculator import separate
from calculator import shuntingYard
from calculator import postFixEval

class Test(unittest.TestCase):
    def testConvert(self):
        example = "abcd123+"
        example = convert(example)
        self.assertTrue(isinstance(example, list),
                    "Expected list instead of string")

    def testSeparate(self):
        example = ("1+63-3")
        example = separate(example)
        list = [1, "+", 63, "-", 3]
        self.assertEqual(example, list)

    def testShuntingYard(self):
        example = [1, "+", "(", 2, "*", 3, ")", "-", 4]
        result = Queue()
        result.put(1)
        result.put(2)
        result.put(3)
        result.put("*")
        result.put("+")
        result.put(4)
        result.put("-")
        example = shuntingYard(example)
        self.assertEqual(example, result)

"""
    def testPostFix(self):
        example = 
"""
  
if __name__ == '__main__':
    unittest.main()