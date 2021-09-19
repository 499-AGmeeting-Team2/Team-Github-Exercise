import unittest
from addition import add_numbers
from subtraction import subtraction
from division import division


class testFunctions(unittest.TestCase):

    def test_sum(self):
        return add_numbers(3, 7) == 10

    def test_subtraction(self):
        return subtraction(7, 3) == 4
    
    def test_division(self):
        return division(10,2) == 5
        

if __name__ == '__main__':
    testFunctions.main()
