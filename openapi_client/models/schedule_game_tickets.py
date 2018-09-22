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


class ScheduleGameTickets(object):
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
        'ticket_type': 'str',
        'ticket_link': 'str'
    }

    attribute_map = {
        'ticket_type': 'ticketType',
        'ticket_link': 'ticketLink'
    }

    def __init__(self, ticket_type=None, ticket_link=None):  # noqa: E501
        """ScheduleGameTickets - a model defined in OpenAPI"""  # noqa: E501

        self._ticket_type = None
        self._ticket_link = None
        self.discriminator = None

        if ticket_type is not None:
            self.ticket_type = ticket_type
        if ticket_link is not None:
            self.ticket_link = ticket_link

    @property
    def ticket_type(self):
        """Gets the ticket_type of this ScheduleGameTickets.  # noqa: E501


        :return: The ticket_type of this ScheduleGameTickets.  # noqa: E501
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        """Sets the ticket_type of this ScheduleGameTickets.


        :param ticket_type: The ticket_type of this ScheduleGameTickets.  # noqa: E501
        :type: str
        """
        allowed_values = ["buysell", "club buysell", "club mobile", "club mobile buysell", "club ticket", "mobile app ticket", "mobile buysell", "mobile ticket", "tablet app ticket", "ticket"]  # noqa: E501
        if ticket_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ticket_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ticket_type, allowed_values)
            )

        self._ticket_type = ticket_type

    @property
    def ticket_link(self):
        """Gets the ticket_link of this ScheduleGameTickets.  # noqa: E501


        :return: The ticket_link of this ScheduleGameTickets.  # noqa: E501
        :rtype: str
        """
        return self._ticket_link

    @ticket_link.setter
    def ticket_link(self, ticket_link):
        """Sets the ticket_link of this ScheduleGameTickets.


        :param ticket_link: The ticket_link of this ScheduleGameTickets.  # noqa: E501
        :type: str
        """

        self._ticket_link = ticket_link

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
        if not isinstance(other, ScheduleGameTickets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
