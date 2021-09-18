import unittest
from addition import add_numbers
import random


class test_main(unittest.TestCase):

    def test_sum(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        return add_numbers(a, b) == a + b


if __name__ == '__main__':
    test_main.main()
