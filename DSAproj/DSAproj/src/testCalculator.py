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
        self.assertTrue(isinstance(example, list))

    def testSeparate(self):
        example = ("1+63-3")
        example = separate(example)
        list = [1, "+", 63, "-", 3]
        list2 = [1, "+", "&", 63, "-", 3]
        self.assertEqual(example, list)
        self.assertRaises(Exception, list2)

    def testShuntingYard(self):
        example = [7, "^", 2, "*", "(", 25, "+", 10, "/", 5, ")", "-", 13]
        result = Queue()
        result.put(7)
        result.put(2)
        result.put("^")
        result.put(25)
        result.put(10)
        result.put(5)
        result.put("/")
        result.put("+")
        result.put("*")
        result.put(13)
        result.put("-")
        example = shuntingYard(example)
        self.assertEqual(example.queue, result.queue)

    def testPostFixEval(self):
        result = Queue()
        result.put(7)
        result.put(2)
        result.put("^")
        result.put(25)
        result.put(10)
        result.put(5)
        result.put("/")
        result.put("+")
        result.put("*")
        result.put(13)
        result.put("-")
        res = 1310.0
        self.assertEqual(postFixEval(result), res)
  
if __name__ == '__main__':
    unittest.main()