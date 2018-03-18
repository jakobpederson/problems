from unittest import TestCase

from exercise_7 import get_2_dimensional_array

class Exercise7Test(TestCase):

    def test_example(self):
        expected = [
            [0, 0, 0, 0, 0],
            [0, 1, 2, 3, 4],
            [0, 2, 4, 6, 8]
        ]
        self.assertCountEqual(get_2_dimensional_array(3, 5), expected)

    def test_1_2(self):
        expected = [
            [0, 0],
        ]
        self.assertCountEqual(get_2_dimensional_array(1, 2), expected)

    def test_4_2(self):
        expected = [
            [0, 0],
            [0, 1],
            [0, 2],
            [0, 3],
        ]
        self.assertCountEqual(get_2_dimensional_array(4, 2), expected)

