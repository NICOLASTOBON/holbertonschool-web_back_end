#!/usr/bin/env python3
""" test for client module """

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGitHubOrgClient(unittest.TestCase):
    """ class for client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, org, mock_org):
        """ test for org function """
        site = GithubOrgClient(org)
        self.assertEqual(site.org.return_value, mock_org.return_value)
