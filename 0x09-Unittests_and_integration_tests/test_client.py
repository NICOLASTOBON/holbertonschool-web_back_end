#!/usr/bin/env python3
""" test for client module """

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org_name):
        """ Test function for client.GithubOrgClient.org """
        with patch('client.GithubOrgClient.org') as mock_org:
            client = GithubOrgClient(org_name=org_name)
            self.assertEqual(client.org.return_value, mock_org.return_value)
