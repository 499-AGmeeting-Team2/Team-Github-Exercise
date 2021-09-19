import unittest
from addition import add_numbers
from subtraction import subtraction


class TestFunctions(unittest.TestCase):

    def test_sum(self):
        return add_numbers(3, 7) == 10

    def test_subtraction(self):
        return subtraction(7, 3) == 4


if __name__ == '__main__':
    TestFunctions.main()
