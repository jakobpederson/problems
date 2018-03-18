from unittest import TestCase

from exercise_1 import get_numbers


class ExerciseTest(TestCase):

    def test_x(self):
        result = get_numbers(0, 35)
        self.assertCountEqual(result, [7, 14, 21, 28])
        self.fail('x')
