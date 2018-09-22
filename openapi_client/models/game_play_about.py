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


class GamePlayAbout(object):
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
        'event_idx': 'float',
        'event_id': 'float',
        'period': 'float',
        'period_type': 'str',
        'ordinal_num': 'str',
        'period_time': 'str',
        'period_time_remaining': 'str',
        'date_time': 'datetime',
        'goals': 'GamePlayAboutGoals'
    }

    attribute_map = {
        'event_idx': 'eventIdx',
        'event_id': 'eventId',
        'period': 'period',
        'period_type': 'periodType',
        'ordinal_num': 'ordinalNum',
        'period_time': 'periodTime',
        'period_time_remaining': 'periodTimeRemaining',
        'date_time': 'dateTime',
        'goals': 'goals'
    }

    def __init__(self, event_idx=None, event_id=None, period=None, period_type=None, ordinal_num=None, period_time=None, period_time_remaining=None, date_time=None, goals=None):  # noqa: E501
        """GamePlayAbout - a model defined in OpenAPI"""  # noqa: E501

        self._event_idx = None
        self._event_id = None
        self._period = None
        self._period_type = None
        self._ordinal_num = None
        self._period_time = None
        self._period_time_remaining = None
        self._date_time = None
        self._goals = None
        self.discriminator = None

        if event_idx is not None:
            self.event_idx = event_idx
        if event_id is not None:
            self.event_id = event_id
        if period is not None:
            self.period = period
        if period_type is not None:
            self.period_type = period_type
        if ordinal_num is not None:
            self.ordinal_num = ordinal_num
        if period_time is not None:
            self.period_time = period_time
        if period_time_remaining is not None:
            self.period_time_remaining = period_time_remaining
        if date_time is not None:
            self.date_time = date_time
        if goals is not None:
            self.goals = goals

    @property
    def event_idx(self):
        """Gets the event_idx of this GamePlayAbout.  # noqa: E501


        :return: The event_idx of this GamePlayAbout.  # noqa: E501
        :rtype: float
        """
        return self._event_idx

    @event_idx.setter
    def event_idx(self, event_idx):
        """Sets the event_idx of this GamePlayAbout.


        :param event_idx: The event_idx of this GamePlayAbout.  # noqa: E501
        :type: float
        """

        self._event_idx = event_idx

    @property
    def event_id(self):
        """Gets the event_id of this GamePlayAbout.  # noqa: E501


        :return: The event_id of this GamePlayAbout.  # noqa: E501
        :rtype: float
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this GamePlayAbout.


        :param event_id: The event_id of this GamePlayAbout.  # noqa: E501
        :type: float
        """

        self._event_id = event_id

    @property
    def period(self):
        """Gets the period of this GamePlayAbout.  # noqa: E501


        :return: The period of this GamePlayAbout.  # noqa: E501
        :rtype: float
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this GamePlayAbout.


        :param period: The period of this GamePlayAbout.  # noqa: E501
        :type: float
        """

        self._period = period

    @property
    def period_type(self):
        """Gets the period_type of this GamePlayAbout.  # noqa: E501


        :return: The period_type of this GamePlayAbout.  # noqa: E501
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this GamePlayAbout.


        :param period_type: The period_type of this GamePlayAbout.  # noqa: E501
        :type: str
        """

        self._period_type = period_type

    @property
    def ordinal_num(self):
        """Gets the ordinal_num of this GamePlayAbout.  # noqa: E501


        :return: The ordinal_num of this GamePlayAbout.  # noqa: E501
        :rtype: str
        """
        return self._ordinal_num

    @ordinal_num.setter
    def ordinal_num(self, ordinal_num):
        """Sets the ordinal_num of this GamePlayAbout.


        :param ordinal_num: The ordinal_num of this GamePlayAbout.  # noqa: E501
        :type: str
        """

        self._ordinal_num = ordinal_num

    @property
    def period_time(self):
        """Gets the period_time of this GamePlayAbout.  # noqa: E501


        :return: The period_time of this GamePlayAbout.  # noqa: E501
        :rtype: str
        """
        return self._period_time

    @period_time.setter
    def period_time(self, period_time):
        """Sets the period_time of this GamePlayAbout.


        :param period_time: The period_time of this GamePlayAbout.  # noqa: E501
        :type: str
        """

        self._period_time = period_time

    @property
    def period_time_remaining(self):
        """Gets the period_time_remaining of this GamePlayAbout.  # noqa: E501


        :return: The period_time_remaining of this GamePlayAbout.  # noqa: E501
        :rtype: str
        """
        return self._period_time_remaining

    @period_time_remaining.setter
    def period_time_remaining(self, period_time_remaining):
        """Sets the period_time_remaining of this GamePlayAbout.


        :param period_time_remaining: The period_time_remaining of this GamePlayAbout.  # noqa: E501
        :type: str
        """

        self._period_time_remaining = period_time_remaining

    @property
    def date_time(self):
        """Gets the date_time of this GamePlayAbout.  # noqa: E501


        :return: The date_time of this GamePlayAbout.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this GamePlayAbout.


        :param date_time: The date_time of this GamePlayAbout.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def goals(self):
        """Gets the goals of this GamePlayAbout.  # noqa: E501


        :return: The goals of this GamePlayAbout.  # noqa: E501
        :rtype: GamePlayAboutGoals
        """
        return self._goals

    @goals.setter
    def goals(self, goals):
        """Sets the goals of this GamePlayAbout.


        :param goals: The goals of this GamePlayAbout.  # noqa: E501
        :type: GamePlayAboutGoals
        """

        self._goals = goals

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
        if not isinstance(other, GamePlayAbout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other