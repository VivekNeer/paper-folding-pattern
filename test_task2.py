import unittest
from task2 import get_crease


class TestGetCrease(unittest.TestCase):
    def test_n1_x1(self):
        self.assertEqual(get_crease(1, 1), "Valley")

    def test_n3_x6(self):
        self.assertEqual(get_crease(3, 6), "Mountain")

    def test_n5_x16(self):
        self.assertEqual(get_crease(5, 16), "Valley")

    def test_n8_x255(self):
        self.assertEqual(get_crease(8, 255), "Mountain")


if __name__ == "__main__":
    unittest.main()