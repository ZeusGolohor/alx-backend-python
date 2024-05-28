#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make sure
you understand.
"""
import unittest
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)
from unittest.mock import (patch, Mock)
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Familiarize yourself with the utils.access_nested_map function
    and understand its purpose.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        A method to test that the method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_res):
        """
        Implement TestAccessNestedMap.test_access_nested_map_exception.
        """
        with self.assertRaises(KeyError) as r:
            access_nested_map(nested_map, path)
        self.assertEqual(str(r.exception), expected_res)


class TestGetJson(unittest.TestCase):
    """
    Define the TestGetJson(unittest.TestCase) class and implement
    the TestGetJson.test_get_json method to test that utils.get_json
    returns the expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        TestGetJson.test_get_json method to test that utils.get_json
        returns the expected result.
        """
        attributes = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attributes)) as request:
            self.assertEqual(get_json(test_url), test_payload)
            request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    A TestMemoize(unittest.TestCase) class with a test_memoize method.
    """
    def test_memoize(self):
        """
        A TestMemoize(unittest.TestCase) class with a test_memoize method.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=lambda: 42) as p:
            test_ins = TestClass()
            self.assertEqual(test_ins.a_property(), 42)
            self.assertEqual(test_ins.a_property(), 42)
            p.assert_called_once()
