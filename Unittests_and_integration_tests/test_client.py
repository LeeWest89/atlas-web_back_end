#!/usr/bin/env python3
"""Unitest for utlis.py"""


import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={})
    def test_org(self, org_name, mock):
        """test that GithubOrgClient.org returns the correct value"""
        self.assertEqual(GithubOrgClient(org_name).org, {})

########################

    @parameterized.expand([
        ("url", {"repos_url": "http://url.com"})
    ])
    def test_public_repos_url(self, org_name, result):
        """
        Test that the result of _public_repos_url
        is the expected one based on the mocked payload
        """
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=result)):
            self.assertEqual(GithubOrgClient(org_name)._public_repos_url,
                             result.get("repos_url"))

########################

    @patch("client.get_json", return_value=[
        {"name": "Amazon"}, {"name": "Google"}
        ])
    def test_public_repos(self, mocked):
        """Test public_repo method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock):
            self.assertEqual(GithubOrgClient('test').public_repos(),
                             ["Amazon", "Google"])
            mocked.assert_called_once()


if __name__ == '__main__':
    unittest.main()
