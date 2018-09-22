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


class GameLiveDataDecisions(object):
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
        'winner': 'GameDecisionPlayer',
        'loser': 'GameDecisionPlayer',
        'first_star': 'GameDecisionPlayer',
        'second_star': 'GameDecisionPlayer',
        'third_star': 'GameDecisionPlayer'
    }

    attribute_map = {
        'winner': 'winner',
        'loser': 'loser',
        'first_star': 'firstStar',
        'second_star': 'secondStar',
        'third_star': 'thirdStar'
    }

    def __init__(self, winner=None, loser=None, first_star=None, second_star=None, third_star=None):  # noqa: E501
        """GameLiveDataDecisions - a model defined in OpenAPI"""  # noqa: E501

        self._winner = None
        self._loser = None
        self._first_star = None
        self._second_star = None
        self._third_star = None
        self.discriminator = None

        if winner is not None:
            self.winner = winner
        if loser is not None:
            self.loser = loser
        if first_star is not None:
            self.first_star = first_star
        if second_star is not None:
            self.second_star = second_star
        if third_star is not None:
            self.third_star = third_star

    @property
    def winner(self):
        """Gets the winner of this GameLiveDataDecisions.  # noqa: E501


        :return: The winner of this GameLiveDataDecisions.  # noqa: E501
        :rtype: GameDecisionPlayer
        """
        return self._winner

    @winner.setter
    def winner(self, winner):
        """Sets the winner of this GameLiveDataDecisions.


        :param winner: The winner of this GameLiveDataDecisions.  # noqa: E501
        :type: GameDecisionPlayer
        """

        self._winner = winner

    @property
    def loser(self):
        """Gets the loser of this GameLiveDataDecisions.  # noqa: E501


        :return: The loser of this GameLiveDataDecisions.  # noqa: E501
        :rtype: GameDecisionPlayer
        """
        return self._loser

    @loser.setter
    def loser(self, loser):
        """Sets the loser of this GameLiveDataDecisions.


        :param loser: The loser of this GameLiveDataDecisions.  # noqa: E501
        :type: GameDecisionPlayer
        """

        self._loser = loser

    @property
    def first_star(self):
        """Gets the first_star of this GameLiveDataDecisions.  # noqa: E501


        :return: The first_star of this GameLiveDataDecisions.  # noqa: E501
        :rtype: GameDecisionPlayer
        """
        return self._first_star

    @first_star.setter
    def first_star(self, first_star):
        """Sets the first_star of this GameLiveDataDecisions.


        :param first_star: The first_star of this GameLiveDataDecisions.  # noqa: E501
        :type: GameDecisionPlayer
        """

        self._first_star = first_star

    @property
    def second_star(self):
        """Gets the second_star of this GameLiveDataDecisions.  # noqa: E501


        :return: The second_star of this GameLiveDataDecisions.  # noqa: E501
        :rtype: GameDecisionPlayer
        """
        return self._second_star

    @second_star.setter
    def second_star(self, second_star):
        """Sets the second_star of this GameLiveDataDecisions.


        :param second_star: The second_star of this GameLiveDataDecisions.  # noqa: E501
        :type: GameDecisionPlayer
        """

        self._second_star = second_star

    @property
    def third_star(self):
        """Gets the third_star of this GameLiveDataDecisions.  # noqa: E501


        :return: The third_star of this GameLiveDataDecisions.  # noqa: E501
        :rtype: GameDecisionPlayer
        """
        return self._third_star

    @third_star.setter
    def third_star(self, third_star):
        """Sets the third_star of this GameLiveDataDecisions.


        :param third_star: The third_star of this GameLiveDataDecisions.  # noqa: E501
        :type: GameDecisionPlayer
        """

        self._third_star = third_star

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
        if not isinstance(other, GameLiveDataDecisions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
