#!/usr/bin/env python3
"""Unitest for utlis.py"""


import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import requests
from fixtures import TEST_PAYLOAD


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

########################

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, result):
        """testing to see if has_lince returns the correct result"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         result)

########################


@parameterized_class(("org_payload",
                      "repos_payload",
                      "expected_repos",
                      "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test"""
    @classmethod
    def setUpClass(cls):
        """Setup class method"""
        parameters = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
        ]}
        cls.get_patcher = patch("requests.get", **parameters)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Teardown class method"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """test public_repo"""
        self.assertEqual(GithubOrgClient("Google").public_repos(),
                         self.expected_repos)


if __name__ == '__main__':
    unittest.main()
