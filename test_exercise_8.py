from unittest import TestCase

from exercise_8 import get_sorted_list


class Exercise8Test(TestCase):

    def test_example(self):
        words = [
            'without', 'hello', 'bag', 'world'
        ]
        result = get_sorted_list(words)
        expected = [
            'bag', 'hello', 'without', 'world'
        ]
        self.assertEqual(result, expected)

    def test_other_list(self):
        words = [
            'abwithout', 'abhello', 'abbag', 'abworld'
        ]
        result = get_sorted_list(words)
        expected = [
            'abbag', 'abhello', 'abwithout', 'abworld'
        ]
        self.assertEqual(result, expected)
