from unittest import TestCase
from sort import is_sorted


class Test(TestCase):
    def test_is_sorted_true(self):
        result = is_sorted([5, 10, 25, 39])
        self.assertEqual(result, True)

    def test_is_sorted_untrue(self):
        result = is_sorted([25, 39, 5, 10])
        self.assertEqual(result, False)

    def test_is_sorted_empty(self):
        result = is_sorted([])
        self.assertEqual(result, False)

    def test_is_sorted_negative_true(self):
        result = is_sorted([-6, -1, 4, 92])
        self.assertEqual(result, True)

    def test_is_sorted_zero(self):
        result = is_sorted([-4, -3, -2, 0, 2])
        self.assertEqual(result, True)


