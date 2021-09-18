import unittest
from addition import add_numbers


class TestFunctions(unittest.TestCase):

    def test_sum(self):
        return add_numbers(3, 7) == 10


if __name__ == '__main__':
    TestFunctions.main()
