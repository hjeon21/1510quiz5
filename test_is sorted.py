from unittest import TestCase
from sort import is_sorted


class Test(TestCase):
    def is_sorted_true(self):
        result = is_sorted([5, 10, 25, 39])
        self.assertEqual(result, True)


