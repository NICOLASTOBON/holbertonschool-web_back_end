#!/usr/bin/env python3
""" This module tests the clients.py file """
from unittest import mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch
import unittest


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
