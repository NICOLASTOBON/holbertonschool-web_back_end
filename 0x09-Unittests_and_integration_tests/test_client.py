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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test function for client.GithubOrgClient.public_repos """
        mock_get_json.return_value = [
            {"name": "public_repo_0"}, {"name": "public_repo_1"}]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = "https://api.github.com/users/google/repos"
            new_client = GithubOrgClient("google")
            self.assertEqual(new_client.public_repos(), [repo.get(
                "name") for repo in mock_get_json.return_value])
            mock_get_json.assert_called_once()
            mock_pru.assert_called_once()
