import unittest
from multiply import multiply

from addition import add_numbers
from subtraction import subtraction


class test_main(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_sum(self):
        return add_numbers(3, 7) == 10

    def test_subtraction(self):
        return subtraction(7, 3) == 4


if __name__ == '__main__':
    test_main.main()
