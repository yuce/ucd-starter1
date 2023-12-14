import unittest

from job import transform


class TransformTestCase(unittest.TestCase):

    def test_transform(self):
        test_cases = [
                (-5, 0),
                (0, 0),
                (1, 10),
                (2, 14.142135623730951),
                (10, 31.622776601683793),
                (1000, 316.22776601683796),
        ]
        for num, expected in test_cases:
            actual = transform(num)
            self.assertEqual(expected, actual)
