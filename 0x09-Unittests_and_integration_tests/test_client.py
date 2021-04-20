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
    @patch('client.get_json')
    def test_org(self, org_name, mock_org):
        """ Test function for client.get_json """
        client = GithubOrgClient(org_name)
        client.org()
        mock_org.assert_called_once()
