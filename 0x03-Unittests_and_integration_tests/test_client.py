#!/usr/bin/env python3
""" Test Client Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, get_json_mock: Mock) -> None:
        """ Tests that GithubOrgClient.org returns the correct value
        """
        get_json_mock.return_value = {"name": org_name}
        response = GithubOrgClient(org_name).org

        org_url = f"https://api.github.com/orgs/{org_name}"
        get_json_mock.assert_called_once_with(org_url)

        self.assertEqual(response, {"name": org_name})

    def test_public_repos_url(self):
        """ Tests the _public_repos_url method of the class
        """
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/gitloper-azara/repos"  # nopep8
            }
            response = GithubOrgClient("gitloper-azara")._public_repos_url
            result = "https://api.github.com/users/gitloper-azara/repos"

            self.assertEqual(response, result)
