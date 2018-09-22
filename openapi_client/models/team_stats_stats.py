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


class TeamStatsStats(object):
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
        'type': 'TeamStatsType',
        'splits': 'list[TeamStatsSplits]'
    }

    attribute_map = {
        'type': 'type',
        'splits': 'splits'
    }

    def __init__(self, type=None, splits=None):  # noqa: E501
        """TeamStatsStats - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._splits = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if splits is not None:
            self.splits = splits

    @property
    def type(self):
        """Gets the type of this TeamStatsStats.  # noqa: E501


        :return: The type of this TeamStatsStats.  # noqa: E501
        :rtype: TeamStatsType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TeamStatsStats.


        :param type: The type of this TeamStatsStats.  # noqa: E501
        :type: TeamStatsType
        """

        self._type = type

    @property
    def splits(self):
        """Gets the splits of this TeamStatsStats.  # noqa: E501


        :return: The splits of this TeamStatsStats.  # noqa: E501
        :rtype: list[TeamStatsSplits]
        """
        return self._splits

    @splits.setter
    def splits(self, splits):
        """Sets the splits of this TeamStatsStats.


        :param splits: The splits of this TeamStatsStats.  # noqa: E501
        :type: list[TeamStatsSplits]
        """

        self._splits = splits

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
        if not isinstance(other, TeamStatsStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
