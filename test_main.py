import unittest
from multiply import multiply

from addition import add_numbers
from subtraction import subtraction
from division import division


<<<<<<< HEAD
class testFunctions(unittest.TestCase):
=======
class test_main(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
>>>>>>> 212582635119f6512c7d672c56a75111975e344d

    def test_sum(self):
        return add_numbers(3, 7) == 10

    def test_subtraction(self):
        return subtraction(7, 3) == 4
    
    def test_division(self):
        return division(10,2) == 5
        

if __name__ == '__main__':
<<<<<<< HEAD
    testFunctions.main()
=======
    test_main.main()
>>>>>>> 212582635119f6512c7d672c56a75111975e344d
