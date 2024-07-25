#!/usr/bin/env python3
"""Unittest for Nested Maps"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access_nested_map using parameterization
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Method that tests the return values of the access_nested_map
            function
        """
        self.assertEqual(
            access_nested_map(nested_map, path), expected
        )


if __name__ == "__main__":
    unittest.main()
