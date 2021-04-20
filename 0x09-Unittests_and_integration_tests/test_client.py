#!/usr/bin/env python3
""" test for client module """
import unittest
from unittest.mock import patch, PropertyMock
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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """ test for public_repos_url """
        mock_org.return_value = {'repos_url': True}
        client = GithubOrgClient('fake_org')
        self.assertEqual(mock_org.return_value, client.org())

    @patch('client.get_json', return_value=[{"name": "google"}])
    def test_public_repos(self, mock_get_json):
        """ test public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_url:
            client = GithubOrgClient("google")
            public_repos = client.public_repos()
            self.assertEqual(public_repos, ["google"])
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()
