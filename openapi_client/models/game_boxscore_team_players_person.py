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


class GameBoxscoreTeamPlayersPerson(object):
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
        'id': 'float',
        'full_name': 'str',
        'link': 'str',
        'shoots_catches': 'str',
        'roster_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'fullName',
        'link': 'link',
        'shoots_catches': 'shootsCatches',
        'roster_status': 'rosterStatus'
    }

    def __init__(self, id=None, full_name=None, link=None, shoots_catches=None, roster_status=None):  # noqa: E501
        """GameBoxscoreTeamPlayersPerson - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._full_name = None
        self._link = None
        self._shoots_catches = None
        self._roster_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if full_name is not None:
            self.full_name = full_name
        if link is not None:
            self.link = link
        if shoots_catches is not None:
            self.shoots_catches = shoots_catches
        if roster_status is not None:
            self.roster_status = roster_status

    @property
    def id(self):
        """Gets the id of this GameBoxscoreTeamPlayersPerson.  # noqa: E501


        :return: The id of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GameBoxscoreTeamPlayersPerson.


        :param id: The id of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this GameBoxscoreTeamPlayersPerson.  # noqa: E501


        :return: The full_name of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this GameBoxscoreTeamPlayersPerson.


        :param full_name: The full_name of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def link(self):
        """Gets the link of this GameBoxscoreTeamPlayersPerson.  # noqa: E501


        :return: The link of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this GameBoxscoreTeamPlayersPerson.


        :param link: The link of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def shoots_catches(self):
        """Gets the shoots_catches of this GameBoxscoreTeamPlayersPerson.  # noqa: E501


        :return: The shoots_catches of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :rtype: str
        """
        return self._shoots_catches

    @shoots_catches.setter
    def shoots_catches(self, shoots_catches):
        """Sets the shoots_catches of this GameBoxscoreTeamPlayersPerson.


        :param shoots_catches: The shoots_catches of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :type: str
        """

        self._shoots_catches = shoots_catches

    @property
    def roster_status(self):
        """Gets the roster_status of this GameBoxscoreTeamPlayersPerson.  # noqa: E501


        :return: The roster_status of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :rtype: str
        """
        return self._roster_status

    @roster_status.setter
    def roster_status(self, roster_status):
        """Sets the roster_status of this GameBoxscoreTeamPlayersPerson.


        :param roster_status: The roster_status of this GameBoxscoreTeamPlayersPerson.  # noqa: E501
        :type: str
        """

        self._roster_status = roster_status

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
        if not isinstance(other, GameBoxscoreTeamPlayersPerson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
