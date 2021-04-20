#!/usr/bin/env python3
""" test for client module """
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, org_name, mock_org):
        """ Test function for client.GithubOrgClient.org """
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org.return_value, mock_org.return_value)
