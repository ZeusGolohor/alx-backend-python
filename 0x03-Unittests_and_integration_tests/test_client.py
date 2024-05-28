#!/usr/bin/env python3
"""
A TestGithubOrgClient(unittest.TestCase) class
and implement the test_org method.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    A TestGithubOrgClient(unittest.TestCase) class and implement
    the test_org method.
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org):
        """
        A TestGithubOrgClient(unittest.TestCase) class
        and implement the test_org method.
        """
        cli = GithubOrgClient(org)
        with patch.object(cli, 'get_json') as get_json:
            cli.org()
            get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
