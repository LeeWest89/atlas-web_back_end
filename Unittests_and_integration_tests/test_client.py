#!/usr/bin/env python3
"""Unitest for utlis.py"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, mock):
        """test that GithubOrgClient.org returns the correct value"""
        self.assertEqual(GithubOrgClient(org_name).org, {})


if __name__ == '__main__':
    unittest.main()
