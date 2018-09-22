# coding: utf-8

"""
    NHL API

    Documenting the publicly accessible portions of the NHL API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GameBoxscoreTeamTeamStats(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'team_skater_stats': 'GameBoxscoreTeamTeamStatsTeamSkaterStats'
    }

    attribute_map = {
        'team_skater_stats': 'teamSkaterStats'
    }

    def __init__(self, team_skater_stats=None):  # noqa: E501
        """GameBoxscoreTeamTeamStats - a model defined in OpenAPI"""  # noqa: E501

        self._team_skater_stats = None
        self.discriminator = None

        if team_skater_stats is not None:
            self.team_skater_stats = team_skater_stats

    @property
    def team_skater_stats(self):
        """Gets the team_skater_stats of this GameBoxscoreTeamTeamStats.  # noqa: E501


        :return: The team_skater_stats of this GameBoxscoreTeamTeamStats.  # noqa: E501
        :rtype: GameBoxscoreTeamTeamStatsTeamSkaterStats
        """
        return self._team_skater_stats

    @team_skater_stats.setter
    def team_skater_stats(self, team_skater_stats):
        """Sets the team_skater_stats of this GameBoxscoreTeamTeamStats.


        :param team_skater_stats: The team_skater_stats of this GameBoxscoreTeamTeamStats.  # noqa: E501
        :type: GameBoxscoreTeamTeamStatsTeamSkaterStats
        """

        self._team_skater_stats = team_skater_stats

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GameBoxscoreTeamTeamStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
