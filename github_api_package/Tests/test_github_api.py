# -*- coding: utf-8 -*-
"""test_github_api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qUAZFWqccV_5KBjBiKACtXNo86Sm51V_
"""

import unittest
from unittest.mock import patch, Mock
from github_api_package.github_api import get_github_user_data

class TestGitHubApi(unittest.TestCase):
    @patch('github_api_package.github_api.requests.get')
    def test_get_github_user_data(self, mock_requests_get):
        # Prepare a mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"login": "example_user", "name": "Example User"}'

        # Configure the mock to return the mock response
        mock_requests_get.return_value = mock_response

        # Call the function with a mock token
        user_data = get_github_user_data('mocked_token')

        # Assert that the function returned the expected data
        self.assertEqual(user_data['login'], 'example_user')
        self.assertEqual(user_data['name'], 'Example User')

        # Assert that requests.get was called with the expected parameters
        mock_requests_get.assert_called_once_with(
            url='https://api.github.com/user',
            headers={'Authorization': 'Bearer mocked_token'}
        )

    @patch('github_api_package.github_api.requests.get')
    def test_get_github_user_data_error(self, mock_requests_get):
        # Configure the mock to simulate an HTTP error
        mock_requests_get.side_effect = requests.exceptions.HTTPError("Mocked error")

        # Call the function with a mock token and expect an exception
        with self.assertRaises(requests.exceptions.HTTPError):
            get_github_user_data('mocked_token')

if __name__ == "__main__":
    unittest.main()