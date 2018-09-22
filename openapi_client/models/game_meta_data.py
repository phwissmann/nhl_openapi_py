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


class GameMetaData(object):
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
        'wait': 'float',
        'time_stamp': 'str'
    }

    attribute_map = {
        'wait': 'wait',
        'time_stamp': 'timeStamp'
    }

    def __init__(self, wait=None, time_stamp=None):  # noqa: E501
        """GameMetaData - a model defined in OpenAPI"""  # noqa: E501

        self._wait = None
        self._time_stamp = None
        self.discriminator = None

        if wait is not None:
            self.wait = wait
        if time_stamp is not None:
            self.time_stamp = time_stamp

    @property
    def wait(self):
        """Gets the wait of this GameMetaData.  # noqa: E501


        :return: The wait of this GameMetaData.  # noqa: E501
        :rtype: float
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this GameMetaData.


        :param wait: The wait of this GameMetaData.  # noqa: E501
        :type: float
        """

        self._wait = wait

    @property
    def time_stamp(self):
        """Gets the time_stamp of this GameMetaData.  # noqa: E501


        :return: The time_stamp of this GameMetaData.  # noqa: E501
        :rtype: str
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this GameMetaData.


        :param time_stamp: The time_stamp of this GameMetaData.  # noqa: E501
        :type: str
        """

        self._time_stamp = time_stamp

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
        if not isinstance(other, GameMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
