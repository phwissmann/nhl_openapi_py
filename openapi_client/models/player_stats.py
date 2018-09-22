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


class PlayerStats(object):
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
        'copyright': 'str',
        'stats': 'list[PlayerStatsStats]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'stats': 'stats'
    }

    def __init__(self, copyright=None, stats=None):  # noqa: E501
        """PlayerStats - a model defined in OpenAPI"""  # noqa: E501

        self._copyright = None
        self._stats = None
        self.discriminator = None

        if copyright is not None:
            self.copyright = copyright
        if stats is not None:
            self.stats = stats

    @property
    def copyright(self):
        """Gets the copyright of this PlayerStats.  # noqa: E501


        :return: The copyright of this PlayerStats.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this PlayerStats.


        :param copyright: The copyright of this PlayerStats.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def stats(self):
        """Gets the stats of this PlayerStats.  # noqa: E501


        :return: The stats of this PlayerStats.  # noqa: E501
        :rtype: list[PlayerStatsStats]
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this PlayerStats.


        :param stats: The stats of this PlayerStats.  # noqa: E501
        :type: list[PlayerStatsStats]
        """

        self._stats = stats

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
        if not isinstance(other, PlayerStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
