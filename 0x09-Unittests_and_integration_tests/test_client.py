#!/usr/bin/env python3
""" test for client module """

import unittest

from client import GitHubOrgClient

from unittest.mock import patch
from parameterized import parameterized


class TestGitHubOrgClient(unittest.TestCase):
    """ class for client """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, name_org, mock_org):
        """ test for org function """
        organization = GitHubOrgClient(name_org)
        organization.org()
        mock_org.assert_called_once()
