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


class GameHighlights(object):
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
        'scoreboard': 'GameHighlightType',
        'game_center': 'GameHighlightType'
    }

    attribute_map = {
        'scoreboard': 'scoreboard',
        'game_center': 'gameCenter'
    }

    def __init__(self, scoreboard=None, game_center=None):  # noqa: E501
        """GameHighlights - a model defined in OpenAPI"""  # noqa: E501

        self._scoreboard = None
        self._game_center = None
        self.discriminator = None

        if scoreboard is not None:
            self.scoreboard = scoreboard
        if game_center is not None:
            self.game_center = game_center

    @property
    def scoreboard(self):
        """Gets the scoreboard of this GameHighlights.  # noqa: E501


        :return: The scoreboard of this GameHighlights.  # noqa: E501
        :rtype: GameHighlightType
        """
        return self._scoreboard

    @scoreboard.setter
    def scoreboard(self, scoreboard):
        """Sets the scoreboard of this GameHighlights.


        :param scoreboard: The scoreboard of this GameHighlights.  # noqa: E501
        :type: GameHighlightType
        """

        self._scoreboard = scoreboard

    @property
    def game_center(self):
        """Gets the game_center of this GameHighlights.  # noqa: E501


        :return: The game_center of this GameHighlights.  # noqa: E501
        :rtype: GameHighlightType
        """
        return self._game_center

    @game_center.setter
    def game_center(self, game_center):
        """Sets the game_center of this GameHighlights.


        :param game_center: The game_center of this GameHighlights.  # noqa: E501
        :type: GameHighlightType
        """

        self._game_center = game_center

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
        if not isinstance(other, GameHighlights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other