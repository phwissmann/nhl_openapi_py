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


class GameLinescoreIntermissionInfo(object):
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
        'intermission_time_remaining': 'float',
        'intermission_time_elapsed': 'float',
        'in_intermission': 'bool'
    }

    attribute_map = {
        'intermission_time_remaining': 'intermissionTimeRemaining',
        'intermission_time_elapsed': 'intermissionTimeElapsed',
        'in_intermission': 'inIntermission'
    }

    def __init__(self, intermission_time_remaining=None, intermission_time_elapsed=None, in_intermission=None):  # noqa: E501
        """GameLinescoreIntermissionInfo - a model defined in OpenAPI"""  # noqa: E501

        self._intermission_time_remaining = None
        self._intermission_time_elapsed = None
        self._in_intermission = None
        self.discriminator = None

        if intermission_time_remaining is not None:
            self.intermission_time_remaining = intermission_time_remaining
        if intermission_time_elapsed is not None:
            self.intermission_time_elapsed = intermission_time_elapsed
        if in_intermission is not None:
            self.in_intermission = in_intermission

    @property
    def intermission_time_remaining(self):
        """Gets the intermission_time_remaining of this GameLinescoreIntermissionInfo.  # noqa: E501


        :return: The intermission_time_remaining of this GameLinescoreIntermissionInfo.  # noqa: E501
        :rtype: float
        """
        return self._intermission_time_remaining

    @intermission_time_remaining.setter
    def intermission_time_remaining(self, intermission_time_remaining):
        """Sets the intermission_time_remaining of this GameLinescoreIntermissionInfo.


        :param intermission_time_remaining: The intermission_time_remaining of this GameLinescoreIntermissionInfo.  # noqa: E501
        :type: float
        """

        self._intermission_time_remaining = intermission_time_remaining

    @property
    def intermission_time_elapsed(self):
        """Gets the intermission_time_elapsed of this GameLinescoreIntermissionInfo.  # noqa: E501


        :return: The intermission_time_elapsed of this GameLinescoreIntermissionInfo.  # noqa: E501
        :rtype: float
        """
        return self._intermission_time_elapsed

    @intermission_time_elapsed.setter
    def intermission_time_elapsed(self, intermission_time_elapsed):
        """Sets the intermission_time_elapsed of this GameLinescoreIntermissionInfo.


        :param intermission_time_elapsed: The intermission_time_elapsed of this GameLinescoreIntermissionInfo.  # noqa: E501
        :type: float
        """

        self._intermission_time_elapsed = intermission_time_elapsed

    @property
    def in_intermission(self):
        """Gets the in_intermission of this GameLinescoreIntermissionInfo.  # noqa: E501


        :return: The in_intermission of this GameLinescoreIntermissionInfo.  # noqa: E501
        :rtype: bool
        """
        return self._in_intermission

    @in_intermission.setter
    def in_intermission(self, in_intermission):
        """Sets the in_intermission of this GameLinescoreIntermissionInfo.


        :param in_intermission: The in_intermission of this GameLinescoreIntermissionInfo.  # noqa: E501
        :type: bool
        """

        self._in_intermission = in_intermission

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
        if not isinstance(other, GameLinescoreIntermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
