#!/usr/bin/env python3
"""Unitest for utlis.py"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test for acessing the nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Use the assertRaises context manager to
        test that a KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """get_json test"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json, using mocking"""
        with patch("requests.get") as mocked:
            mocked.return_value.json = Mock(return_value=test_payload)
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """memoize test"""
    def test_memoize(self):
        """test memorize"""
        class TestClass:
            """test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass(), "a_method") as mocked:
            TestClass().a_property
            TestClass().a_property
            mocked.assert_called_once


if __name__ == "__main__":
    unittest.main()
