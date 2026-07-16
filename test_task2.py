import unittest
from task2 import get_crease


class TestGetCrease(unittest.TestCase):
   
    def test_n1_x1_valley(self):
        """Test 1: n=1, x=1 -> should be Valley"""
        result = get_crease(1, 1)
        self.assertEqual(result, "Valley",
                          f"n=1, x=1 -> expected Valley, got {result}")

    def test_n3_x6_mountain(self):
        """Test 2: n=3, x=6 -> should be Mountain"""
        result = get_crease(3, 6)
        self.assertEqual(result, "Mountain",
                          f"n=3, x=6 -> expected Mountain, got {result}")

    def test_n5_x16_valley(self):
        """Test 3: n=5, x=16 -> should be Valley"""
        result = get_crease(5, 16)
        self.assertEqual(result, "Valley",
                          f"n=5, x=16 -> expected Valley, got {result}")

    def test_n8_x255_mountain(self):
        """Test 4: n=8, x=255 -> should be Mountain"""
        result = get_crease(8, 255)
        self.assertEqual(result, "Mountain",
                          f"n=8, x=255 -> expected Mountain, got {result}")


if __name__ == "__main__":
    unittest.main()