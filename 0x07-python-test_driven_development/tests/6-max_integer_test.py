#!/usr/bin/python3
"""Unittest for max_integer """
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestFindMax(unittest.TestCase):
    def test_no_argument(self):
        self.assertEqual(find_max(), None)

    def test_empty_list(self):
        self.assertEqual(find_max([]), None)

    def test_single_element(self):
        self.assertEqual(find_max([98]), 98)

    def test_identical_elements(self):
        self.assertEqual(find_max([7, 7, 7, 7]), 7)

    def test_max_at_start(self):
        self.assertEqual(find_max([5, 4, 3, 2]), 5)

    def test_negatives(self):
         """Unittest for max_integer([..])"""
         self.assertEqual(max_integer([-34535, -6 , 567, 8990, 90])

    def test_int_and_float(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [100, 990.8, -10, -0.01, 10000, 999, -10000, 98898.9]), 99999)
    def test_number_text(self):
          """Unittest for max_integer([..])"""
          self.assertEqual(max_integer("19283"), "9666")
    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([, float('nan'), 1050]), 1050)
    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])



if __name__ == '__main__':
    unittest.main()
