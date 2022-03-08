import unittest
from src.calculator import Clause

class Test(unittest.TestCase):
    def testSplit(self):
        example = Clause("1+6-3")
        example.split()
        self.assertTrue(isinstance(example, list),
                            "Expected list instead of string")
        
if __name__ == '__main__':
    unittest.main()