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


class GameLinescore(object):
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
        'current_period': 'float',
        'current_period_ordinal': 'str',
        'current_period_time_remaining': 'str',
        'periods': 'list[GamePeriod]',
        'shootout_info': 'GameLinescoreShootoutInfo',
        'teams': 'GameLinescoreTeams',
        'power_play_strength': 'str',
        'has_shootout': 'bool',
        'intermission_info': 'GameLinescoreIntermissionInfo',
        'power_play_info': 'GameLinescorePowerPlayInfo'
    }

    attribute_map = {
        'current_period': 'currentPeriod',
        'current_period_ordinal': 'currentPeriodOrdinal',
        'current_period_time_remaining': 'currentPeriodTimeRemaining',
        'periods': 'periods',
        'shootout_info': 'shootoutInfo',
        'teams': 'teams',
        'power_play_strength': 'powerPlayStrength',
        'has_shootout': 'hasShootout',
        'intermission_info': 'intermissionInfo',
        'power_play_info': 'powerPlayInfo'
    }

    def __init__(self, current_period=None, current_period_ordinal=None, current_period_time_remaining=None, periods=None, shootout_info=None, teams=None, power_play_strength=None, has_shootout=None, intermission_info=None, power_play_info=None):  # noqa: E501
        """GameLinescore - a model defined in OpenAPI"""  # noqa: E501

        self._current_period = None
        self._current_period_ordinal = None
        self._current_period_time_remaining = None
        self._periods = None
        self._shootout_info = None
        self._teams = None
        self._power_play_strength = None
        self._has_shootout = None
        self._intermission_info = None
        self._power_play_info = None
        self.discriminator = None

        if current_period is not None:
            self.current_period = current_period
        if current_period_ordinal is not None:
            self.current_period_ordinal = current_period_ordinal
        if current_period_time_remaining is not None:
            self.current_period_time_remaining = current_period_time_remaining
        if periods is not None:
            self.periods = periods
        if shootout_info is not None:
            self.shootout_info = shootout_info
        if teams is not None:
            self.teams = teams
        if power_play_strength is not None:
            self.power_play_strength = power_play_strength
        if has_shootout is not None:
            self.has_shootout = has_shootout
        if intermission_info is not None:
            self.intermission_info = intermission_info
        if power_play_info is not None:
            self.power_play_info = power_play_info

    @property
    def current_period(self):
        """Gets the current_period of this GameLinescore.  # noqa: E501


        :return: The current_period of this GameLinescore.  # noqa: E501
        :rtype: float
        """
        return self._current_period

    @current_period.setter
    def current_period(self, current_period):
        """Sets the current_period of this GameLinescore.


        :param current_period: The current_period of this GameLinescore.  # noqa: E501
        :type: float
        """

        self._current_period = current_period

    @property
    def current_period_ordinal(self):
        """Gets the current_period_ordinal of this GameLinescore.  # noqa: E501


        :return: The current_period_ordinal of this GameLinescore.  # noqa: E501
        :rtype: str
        """
        return self._current_period_ordinal

    @current_period_ordinal.setter
    def current_period_ordinal(self, current_period_ordinal):
        """Sets the current_period_ordinal of this GameLinescore.


        :param current_period_ordinal: The current_period_ordinal of this GameLinescore.  # noqa: E501
        :type: str
        """

        self._current_period_ordinal = current_period_ordinal

    @property
    def current_period_time_remaining(self):
        """Gets the current_period_time_remaining of this GameLinescore.  # noqa: E501


        :return: The current_period_time_remaining of this GameLinescore.  # noqa: E501
        :rtype: str
        """
        return self._current_period_time_remaining

    @current_period_time_remaining.setter
    def current_period_time_remaining(self, current_period_time_remaining):
        """Sets the current_period_time_remaining of this GameLinescore.


        :param current_period_time_remaining: The current_period_time_remaining of this GameLinescore.  # noqa: E501
        :type: str
        """

        self._current_period_time_remaining = current_period_time_remaining

    @property
    def periods(self):
        """Gets the periods of this GameLinescore.  # noqa: E501


        :return: The periods of this GameLinescore.  # noqa: E501
        :rtype: list[GamePeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this GameLinescore.


        :param periods: The periods of this GameLinescore.  # noqa: E501
        :type: list[GamePeriod]
        """

        self._periods = periods

    @property
    def shootout_info(self):
        """Gets the shootout_info of this GameLinescore.  # noqa: E501


        :return: The shootout_info of this GameLinescore.  # noqa: E501
        :rtype: GameLinescoreShootoutInfo
        """
        return self._shootout_info

    @shootout_info.setter
    def shootout_info(self, shootout_info):
        """Sets the shootout_info of this GameLinescore.


        :param shootout_info: The shootout_info of this GameLinescore.  # noqa: E501
        :type: GameLinescoreShootoutInfo
        """

        self._shootout_info = shootout_info

    @property
    def teams(self):
        """Gets the teams of this GameLinescore.  # noqa: E501


        :return: The teams of this GameLinescore.  # noqa: E501
        :rtype: GameLinescoreTeams
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this GameLinescore.


        :param teams: The teams of this GameLinescore.  # noqa: E501
        :type: GameLinescoreTeams
        """

        self._teams = teams

    @property
    def power_play_strength(self):
        """Gets the power_play_strength of this GameLinescore.  # noqa: E501


        :return: The power_play_strength of this GameLinescore.  # noqa: E501
        :rtype: str
        """
        return self._power_play_strength

    @power_play_strength.setter
    def power_play_strength(self, power_play_strength):
        """Sets the power_play_strength of this GameLinescore.


        :param power_play_strength: The power_play_strength of this GameLinescore.  # noqa: E501
        :type: str
        """

        self._power_play_strength = power_play_strength

    @property
    def has_shootout(self):
        """Gets the has_shootout of this GameLinescore.  # noqa: E501


        :return: The has_shootout of this GameLinescore.  # noqa: E501
        :rtype: bool
        """
        return self._has_shootout

    @has_shootout.setter
    def has_shootout(self, has_shootout):
        """Sets the has_shootout of this GameLinescore.


        :param has_shootout: The has_shootout of this GameLinescore.  # noqa: E501
        :type: bool
        """

        self._has_shootout = has_shootout

    @property
    def intermission_info(self):
        """Gets the intermission_info of this GameLinescore.  # noqa: E501


        :return: The intermission_info of this GameLinescore.  # noqa: E501
        :rtype: GameLinescoreIntermissionInfo
        """
        return self._intermission_info

    @intermission_info.setter
    def intermission_info(self, intermission_info):
        """Sets the intermission_info of this GameLinescore.


        :param intermission_info: The intermission_info of this GameLinescore.  # noqa: E501
        :type: GameLinescoreIntermissionInfo
        """

        self._intermission_info = intermission_info

    @property
    def power_play_info(self):
        """Gets the power_play_info of this GameLinescore.  # noqa: E501


        :return: The power_play_info of this GameLinescore.  # noqa: E501
        :rtype: GameLinescorePowerPlayInfo
        """
        return self._power_play_info

    @power_play_info.setter
    def power_play_info(self, power_play_info):
        """Sets the power_play_info of this GameLinescore.


        :param power_play_info: The power_play_info of this GameLinescore.  # noqa: E501
        :type: GameLinescorePowerPlayInfo
        """

        self._power_play_info = power_play_info

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
        if not isinstance(other, GameLinescore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other