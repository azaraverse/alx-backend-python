#!/usr/bin/env python3
"""Unittest for Nested Maps"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Any, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access_nested_map using parameterization
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> Any:
        """ Method that tests the return values of the access_nested_map
            function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ) -> Any:
        """ Tests that a KeyError is raised for the given inputs in the
            parameterized decorator.
        """
        with self.assertRaises(KeyError) as c:
            access_nested_map(nested_map, path)
        self.assertEqual(str(c.exception), expected)


if __name__ == "__main__":
    unittest.main()
