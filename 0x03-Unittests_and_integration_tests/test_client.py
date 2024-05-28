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
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org):
        """
        A TestGithubOrgClient(unittest.TestCase) class
        and implement the test_org method.
        """
        cli = GithubOrgClient(org)
        with patch.object(cli, 'get_json') as get_json:
            cli.org()
            get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """
        memoize turns methods into properties. Read up
        on how to mock a property (see resource).
        """
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
