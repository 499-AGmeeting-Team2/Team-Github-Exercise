import unittest
from multiply import multiply


class testMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)


if '__main__' == __name__:
    unittest.main()
