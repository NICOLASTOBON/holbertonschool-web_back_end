#!/usr/bin/env python3
""" test for utils module """

import json
import unittest
from unittest.mock import patch

import requests
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """ class that test utils functions """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test that check if the nested_map it's works """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test that manager the test that a keyError is raised """
        try:
            access_nested_map(nested_map, path)
        except Exception:
            self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """ class that test a get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_request):
        """ function that check the get_json function """
        mock_request.json.return_value = test_payload
        mock_request.return_value = mock_request
        self.assertEqual(get_json(test_url), test_payload)
