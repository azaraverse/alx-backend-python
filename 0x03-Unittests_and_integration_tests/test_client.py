#!/usr/bin/env python3
""" Test Client Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from typing import Callable, Any


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, get_json_mock: Mock) -> Any:
        """ Tests that GithubOrgClient.org returns the correct value
        """
        get_json_mock.return_value = {"name": org_name}
        response = GithubOrgClient(org_name).org

        org_url = f"https://api.github.com/orgs/{org_name}"
        get_json_mock.assert_called_once_with(org_url)

        self.assertEqual(response, {"name": org_name})

    def test_public_repos_url(self) -> Any:
        """ Tests the _public_repos_url method of the class
        """
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url":
                "https://api.github.com/users/gitloper-azara/repos"
            }
            response = GithubOrgClient("gitloper-azara")._public_repos_url
            result = "https://api.github.com/users/gitloper-azara/repos"

            self.assertEqual(response, result)

    @patch("client.get_json")
    def test_public_repos(self, get_json: Callable) -> Any:
        """ Tests the public_repos method of the GithubOrgClient class
        """
        test_payload = {
            "repos_url": "https://api.github.com/users/gitloper-azara/repos",
            "repos": [
                {
                    "id": 802504935,
                    "node_id": "R_kgDOL9VA5w",
                    "name": "SkySync",
                    "full_name": "gitloper-azara/SkySync",
                    "private": False,
                    "owner": {
                        "login": "gitloper-azara",
                        "id": 133230975,
                    },
                    "fork": False,
                    "url":
                    "https://api.github.com/repos/gitloper-azara/SkySync",
                    "created_at": "2024-05-18T13:36:21Z",
                    "updated_at": "2024-06-11T23:36:44Z",
                    "pushed_at": "2024-06-11T23:36:40Z",
                    "size": 389,
                    "language": "Python",
                },
                {
                    "id": 808693419,
                    "node_id": "R_kgDOMDOuqw",
                    "name": "SkySync_landing_page",
                    "full_name": "gitloper-azara/SkySync_landing_page",
                    "private": False,
                    "owner": {
                        "login": "gitloper-azara",
                        "id": 133230975,
                    },
                    "fork": False,
                    "url":
                    "https://api.github.com/repos/gitloper-azara/"
                    "SkySync_landing_page",
                    "created_at": "2024-05-31T15:57:37Z",
                    "updated_at": "2024-06-02T18:02:26Z",
                    "pushed_at": "2024-06-02T18:02:23Z",
                    "size": 88080,
                    "language": "HTML",
                }
            ]
        }

        get_json.return_value = test_payload["repos"]
        with patch.object(
            GithubOrgClient, "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            response = GithubOrgClient("gitloper-azara").public_repos()

            result = ["SkySync", "SkySync_landing_page"]

            self.assertEqual(response, result)

            get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
        self, repo, license_key: str, expected: bool
    ) -> Any:
        """ Tests that the has_license method returns the expected value
        by parameterizing the test with inputs
        """
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected)
