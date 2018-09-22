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


class GamePlay(object):
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
        'players': 'list[GamePlayPlayers]',
        'result': 'GamePlayResult',
        'about': 'GamePlayAbout',
        'coordinates': 'GamePlayCoordinates',
        'team': 'GamePlayTeam'
    }

    attribute_map = {
        'players': 'players',
        'result': 'result',
        'about': 'about',
        'coordinates': 'coordinates',
        'team': 'team'
    }

    def __init__(self, players=None, result=None, about=None, coordinates=None, team=None):  # noqa: E501
        """GamePlay - a model defined in OpenAPI"""  # noqa: E501

        self._players = None
        self._result = None
        self._about = None
        self._coordinates = None
        self._team = None
        self.discriminator = None

        if players is not None:
            self.players = players
        if result is not None:
            self.result = result
        if about is not None:
            self.about = about
        if coordinates is not None:
            self.coordinates = coordinates
        if team is not None:
            self.team = team

    @property
    def players(self):
        """Gets the players of this GamePlay.  # noqa: E501


        :return: The players of this GamePlay.  # noqa: E501
        :rtype: list[GamePlayPlayers]
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this GamePlay.


        :param players: The players of this GamePlay.  # noqa: E501
        :type: list[GamePlayPlayers]
        """

        self._players = players

    @property
    def result(self):
        """Gets the result of this GamePlay.  # noqa: E501


        :return: The result of this GamePlay.  # noqa: E501
        :rtype: GamePlayResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this GamePlay.


        :param result: The result of this GamePlay.  # noqa: E501
        :type: GamePlayResult
        """

        self._result = result

    @property
    def about(self):
        """Gets the about of this GamePlay.  # noqa: E501


        :return: The about of this GamePlay.  # noqa: E501
        :rtype: GamePlayAbout
        """
        return self._about

    @about.setter
    def about(self, about):
        """Sets the about of this GamePlay.


        :param about: The about of this GamePlay.  # noqa: E501
        :type: GamePlayAbout
        """

        self._about = about

    @property
    def coordinates(self):
        """Gets the coordinates of this GamePlay.  # noqa: E501


        :return: The coordinates of this GamePlay.  # noqa: E501
        :rtype: GamePlayCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this GamePlay.


        :param coordinates: The coordinates of this GamePlay.  # noqa: E501
        :type: GamePlayCoordinates
        """

        self._coordinates = coordinates

    @property
    def team(self):
        """Gets the team of this GamePlay.  # noqa: E501


        :return: The team of this GamePlay.  # noqa: E501
        :rtype: GamePlayTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this GamePlay.


        :param team: The team of this GamePlay.  # noqa: E501
        :type: GamePlayTeam
        """

        self._team = team

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
        if not isinstance(other, GamePlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other