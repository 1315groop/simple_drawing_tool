import unittest
from paint import Paint


class TestPaint(unittest.TestCase):
    picture = Paint(15, 10)

    def test_borders(self):

        expected = """-----------------
|               |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
-----------------"""
        self.assertEqual(str(self.picture.draw_me()), expected)

    def test_horizontal(self):

        expected = """-----------------
|               |
| xxxxx         |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
-----------------"""
        self.picture.line(2, 2, 6, 2)
        self.assertEqual(str(self.picture.draw_me()), expected)

    def test_vertical(self):

        expected = """-----------------
|               |
| xxxxx         |
|   x           |
|   x           |
|               |
|               |
|               |
|               |
|               |
|               |
-----------------"""
        self.picture.line(4, 3, 4, 4)
        self.assertEqual(str(self.picture.draw_me()), expected)


if __name__ == "__main__":
    unittest.main()

