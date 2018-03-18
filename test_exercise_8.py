from unittest import TestCase

from exercise_8 import get_sorted_list


class Exercise8Test(TestCase):

    def test_x(self):
        words = [
            'without', 'hello', 'bag', 'world'
        ]
        result = get_sorted_list(words)
        expected = [
            'bag', 'hello', 'without', 'world'
        ]
        self.assertEqual(result, expected)
