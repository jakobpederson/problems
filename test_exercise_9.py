from unittest import TestCase

from exercise_9 import solution_9, prints_solution


class Exercise9Test(TestCase):

    def test_one_line(self):
        lines = [
            'the cat in the hat',
        ]
        result = solution_9(lines)
        expected = [
            'THE CAT IN THE HAT',
        ]
        self.assertCountEqual(result, expected)

    def test_three_lines(self):
        lines = [
            'the cat in the hat',
            'green eggs and ham',
            'one fish two fish,'
        ]
        result = solution_9(lines)
        expected = [
            'THE CAT IN THE HAT',
            'GREEN EGGS AND HAM',
            'ONE FISH TWO FISH,'
        ]
        self.assertCountEqual(result, expected)

    def test_three_lines(self):
        lines = [
            'the cat in the hat',
            'green eggs and ham',
            'one fish two fish,'
        ]
        result = solution_9(lines)
        expected = [
            'THE CAT IN THE HAT',
            'GREEN EGGS AND HAM',
            'ONE FISH TWO FISH,'
        ]
        self.assertCountEqual(result, expected)
