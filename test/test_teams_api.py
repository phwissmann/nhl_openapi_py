# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.teams_api import TeamsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestTeamsApi(unittest.TestCase):
    """TeamsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.teams_api.TeamsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_team(self):
        """Test case for get_team

        Get an NHL team.  # noqa: E501
        """
        pass

    def test_get_team_roster(self):
        """Test case for get_team_roster

        Get an NHL team's roster.  # noqa: E501
        """
        pass

    def test_get_team_stats(self):
        """Test case for get_team_stats

        Get all statistics for an NHL team.  # noqa: E501
        """
        pass

    def test_get_teams(self):
        """Test case for get_teams

        Get all NHL teams.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
