#!/usr/bin/env python3
""" Test Client Module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, get_json_mock):
        """ Tests that GithubOrgClient.org returns the correct value
        """
        get_json_mock.return_value = {"name": org_name}
        response = GithubOrgClient(org_name).org

        org_url = f"https://api.github.com/orgs/{org_name}"
        get_json_mock.assert_called_once_with(org_url)

        self.assertEqual(response, {"name": org_name})
