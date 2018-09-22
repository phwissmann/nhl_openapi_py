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


class TeamNextGameScheduleTeamsAwayLeagueRecord(object):
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
        'wins': 'float',
        'losses': 'float',
        'ot': 'float',
        'type': 'str'
    }

    attribute_map = {
        'wins': 'wins',
        'losses': 'losses',
        'ot': 'ot',
        'type': 'type'
    }

    def __init__(self, wins=None, losses=None, ot=None, type=None):  # noqa: E501
        """TeamNextGameScheduleTeamsAwayLeagueRecord - a model defined in OpenAPI"""  # noqa: E501

        self._wins = None
        self._losses = None
        self._ot = None
        self._type = None
        self.discriminator = None

        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ot is not None:
            self.ot = ot
        if type is not None:
            self.type = type

    @property
    def wins(self):
        """Gets the wins of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501


        :return: The wins of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :rtype: float
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this TeamNextGameScheduleTeamsAwayLeagueRecord.


        :param wins: The wins of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :type: float
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501


        :return: The losses of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :rtype: float
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this TeamNextGameScheduleTeamsAwayLeagueRecord.


        :param losses: The losses of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :type: float
        """

        self._losses = losses

    @property
    def ot(self):
        """Gets the ot of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501


        :return: The ot of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :rtype: float
        """
        return self._ot

    @ot.setter
    def ot(self, ot):
        """Sets the ot of this TeamNextGameScheduleTeamsAwayLeagueRecord.


        :param ot: The ot of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :type: float
        """

        self._ot = ot

    @property
    def type(self):
        """Gets the type of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501


        :return: The type of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TeamNextGameScheduleTeamsAwayLeagueRecord.


        :param type: The type of this TeamNextGameScheduleTeamsAwayLeagueRecord.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if not isinstance(other, TeamNextGameScheduleTeamsAwayLeagueRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
