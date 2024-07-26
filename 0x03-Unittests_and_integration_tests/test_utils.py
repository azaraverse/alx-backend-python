#!/usr/bin/env python3
"""Unittest for Nested Maps"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Any, Sequence, Dict
from unittest.mock import Mock, patch


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


class TestGetJson(unittest.TestCase):
    """"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(
        self, url: str, expected_payload: Dict, mock_func: Any
    ) -> Any:
        """ Tests if the utils.get_json method returns the expected
            results
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_payload
        mock_func.return_value = mock_response

        # call the function that uses the requests module
        result = get_json(url)

        # assert that function returns the expected payload
        self.assertEqual(result, expected_payload)

        # verify that the requests module was called once with the url
        mock_func.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
