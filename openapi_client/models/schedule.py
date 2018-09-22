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


class Schedule(object):
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
        'total_items': 'float',
        'total_events': 'float',
        'total_games': 'float',
        'total_matches': 'float',
        'wait': 'float',
        'dates': 'list[ScheduleDay]'
    }

    attribute_map = {
        'copyright': 'copyright',
        'total_items': 'totalItems',
        'total_events': 'totalEvents',
        'total_games': 'totalGames',
        'total_matches': 'totalMatches',
        'wait': 'wait',
        'dates': 'dates'
    }

    def __init__(self, copyright=None, total_items=None, total_events=None, total_games=None, total_matches=None, wait=None, dates=None):  # noqa: E501
        """Schedule - a model defined in OpenAPI"""  # noqa: E501

        self._copyright = None
        self._total_items = None
        self._total_events = None
        self._total_games = None
        self._total_matches = None
        self._wait = None
        self._dates = None
        self.discriminator = None

        if copyright is not None:
            self.copyright = copyright
        if total_items is not None:
            self.total_items = total_items
        if total_events is not None:
            self.total_events = total_events
        if total_games is not None:
            self.total_games = total_games
        if total_matches is not None:
            self.total_matches = total_matches
        if wait is not None:
            self.wait = wait
        if dates is not None:
            self.dates = dates

    @property
    def copyright(self):
        """Gets the copyright of this Schedule.  # noqa: E501


        :return: The copyright of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright):
        """Sets the copyright of this Schedule.


        :param copyright: The copyright of this Schedule.  # noqa: E501
        :type: str
        """

        self._copyright = copyright

    @property
    def total_items(self):
        """Gets the total_items of this Schedule.  # noqa: E501


        :return: The total_items of this Schedule.  # noqa: E501
        :rtype: float
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this Schedule.


        :param total_items: The total_items of this Schedule.  # noqa: E501
        :type: float
        """

        self._total_items = total_items

    @property
    def total_events(self):
        """Gets the total_events of this Schedule.  # noqa: E501


        :return: The total_events of this Schedule.  # noqa: E501
        :rtype: float
        """
        return self._total_events

    @total_events.setter
    def total_events(self, total_events):
        """Sets the total_events of this Schedule.


        :param total_events: The total_events of this Schedule.  # noqa: E501
        :type: float
        """

        self._total_events = total_events

    @property
    def total_games(self):
        """Gets the total_games of this Schedule.  # noqa: E501


        :return: The total_games of this Schedule.  # noqa: E501
        :rtype: float
        """
        return self._total_games

    @total_games.setter
    def total_games(self, total_games):
        """Sets the total_games of this Schedule.


        :param total_games: The total_games of this Schedule.  # noqa: E501
        :type: float
        """

        self._total_games = total_games

    @property
    def total_matches(self):
        """Gets the total_matches of this Schedule.  # noqa: E501


        :return: The total_matches of this Schedule.  # noqa: E501
        :rtype: float
        """
        return self._total_matches

    @total_matches.setter
    def total_matches(self, total_matches):
        """Sets the total_matches of this Schedule.


        :param total_matches: The total_matches of this Schedule.  # noqa: E501
        :type: float
        """

        self._total_matches = total_matches

    @property
    def wait(self):
        """Gets the wait of this Schedule.  # noqa: E501


        :return: The wait of this Schedule.  # noqa: E501
        :rtype: float
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this Schedule.


        :param wait: The wait of this Schedule.  # noqa: E501
        :type: float
        """

        self._wait = wait

    @property
    def dates(self):
        """Gets the dates of this Schedule.  # noqa: E501


        :return: The dates of this Schedule.  # noqa: E501
        :rtype: list[ScheduleDay]
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this Schedule.


        :param dates: The dates of this Schedule.  # noqa: E501
        :type: list[ScheduleDay]
        """

        self._dates = dates

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
