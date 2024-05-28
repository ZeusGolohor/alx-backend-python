#!/usr/bin/env python3
"""
A TestGithubOrgClient(unittest.TestCase) class
and implement the test_org method.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
            get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

    def test_public_repos_url(self):
        """
        memoize turns methods into properties. Read up
        on how to mock a property (see resource).
        """
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        A TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                        "id": 460600860,
                        "node_id": "R_kgDOG3Q2HA",
                        "name": ".allstar",
                        "full_name": "google/.allstar",
                        "private": false,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        }
                },
                {
                        "id": 170908616,
                        "node_id": "MDEwOlJlcG9zaXRvcnkxNzA5MDg2MTY=",
                        "name": ".github",
                        "full_name": "google/.github",
                        "private": false,
                        "owner": {
                            "login": "google",
                            "id": 1342004,
                            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                        }
                }
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_url:
            mock_public_url.return_value = test_payload['repos_url']
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    '.allstar',
                    '.github',
                ],
            )
            mock_public_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        TestGithubOrgClient.test_has_license to
        unit-test GithubOrgClient.has_license.
        """
        cli = GithubOrgClient("google")
        res = cli.has_license(repo, key)
        self.assertEqual(res, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    A GithubOrgClient.public_repos method in an integration
    test. That means that we will only mock code that sends
    external requests.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        A method used to set up the class
        """
        payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(data):
            if data in payload:
                return Mock(**{'json.return_value': payload[data]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        A method to ensure the class ends gracefully.
        """
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """
        A method to test public repos
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """
        A method to test public repos with license.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license='Apache-2.0'),
            self.apache2_repos,
        )
