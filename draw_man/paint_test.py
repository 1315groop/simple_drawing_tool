import unittest
from paint import Paint


class TestLine(unittest.TestCase):
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


class TestRectNFlood(unittest.TestCase):
    def test_rectangle(self):
        picture = Paint(15, 10)
        expected = """-----------------
|        xxxxx  |
|        x   x  |
|        xxxxx  |
|               |
|               |
|               |
|               |
|               |
|               |
|               |
-----------------"""
        picture.rectangle(13, 1, 9, 3)
        self.assertEqual(str(picture.draw_me()), expected)

    def test_floodfill(self):
        picture = Paint(15, 10)
        expected = """-----------------
|ooooooooxxxxxoo|
|oooooooox   xoo|
|ooooooooxxxxxoo|
|ooooooooooooooo|
|ooooooooooooooo|
|ooooooooooooooo|
|ooooooooooooooo|
|ooooooooooooooo|
|ooooooooooooooo|
|ooooooooooooooo|
-----------------"""
        picture.rectangle(13, 1, 9, 3)
        picture.bucket_fill(1, 9, "o")
        self.assertEqual(str(picture.draw_me()), expected)


if __name__ == "__main__":
    unittest.main()

