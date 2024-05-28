#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make sure
you understand.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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
