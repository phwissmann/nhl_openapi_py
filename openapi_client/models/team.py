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


class Team(object):
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
        'name': 'str',
        'link': 'str',
        'venue': 'Venue',
        'abbreviation': 'str',
        'tri_code': 'str',
        'team_name': 'str',
        'location_name': 'str',
        'first_year_of_play': 'float',
        'division': 'StandingsDivision',
        'conference': 'DivisionConference',
        'franchise': 'Franchise',
        'roster': 'TeamRoster',
        'next_game_schedule': 'TeamNextGameSchedule',
        'short_name': 'str',
        'official_site_url': 'str',
        'franchise_id': 'float',
        'active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'link': 'link',
        'venue': 'venue',
        'abbreviation': 'abbreviation',
        'tri_code': 'triCode',
        'team_name': 'teamName',
        'location_name': 'locationName',
        'first_year_of_play': 'firstYearOfPlay',
        'division': 'division',
        'conference': 'conference',
        'franchise': 'franchise',
        'roster': 'roster',
        'next_game_schedule': 'nextGameSchedule',
        'short_name': 'shortName',
        'official_site_url': 'officialSiteUrl',
        'franchise_id': 'franchiseId',
        'active': 'active'
    }

    def __init__(self, id=None, name=None, link=None, venue=None, abbreviation=None, tri_code=None, team_name=None, location_name=None, first_year_of_play=None, division=None, conference=None, franchise=None, roster=None, next_game_schedule=None, short_name=None, official_site_url=None, franchise_id=None, active=None):  # noqa: E501
        """Team - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._link = None
        self._venue = None
        self._abbreviation = None
        self._tri_code = None
        self._team_name = None
        self._location_name = None
        self._first_year_of_play = None
        self._division = None
        self._conference = None
        self._franchise = None
        self._roster = None
        self._next_game_schedule = None
        self._short_name = None
        self._official_site_url = None
        self._franchise_id = None
        self._active = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if link is not None:
            self.link = link
        if venue is not None:
            self.venue = venue
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if tri_code is not None:
            self.tri_code = tri_code
        if team_name is not None:
            self.team_name = team_name
        if location_name is not None:
            self.location_name = location_name
        if first_year_of_play is not None:
            self.first_year_of_play = first_year_of_play
        if division is not None:
            self.division = division
        if conference is not None:
            self.conference = conference
        if franchise is not None:
            self.franchise = franchise
        if roster is not None:
            self.roster = roster
        if next_game_schedule is not None:
            self.next_game_schedule = next_game_schedule
        if short_name is not None:
            self.short_name = short_name
        if official_site_url is not None:
            self.official_site_url = official_site_url
        if franchise_id is not None:
            self.franchise_id = franchise_id
        if active is not None:
            self.active = active

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501


        :return: The id of this Team.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.


        :param id: The id of this Team.  # noqa: E501
        :type: float
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501


        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def link(self):
        """Gets the link of this Team.  # noqa: E501


        :return: The link of this Team.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Team.


        :param link: The link of this Team.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def venue(self):
        """Gets the venue of this Team.  # noqa: E501


        :return: The venue of this Team.  # noqa: E501
        :rtype: Venue
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this Team.


        :param venue: The venue of this Team.  # noqa: E501
        :type: Venue
        """

        self._venue = venue

    @property
    def abbreviation(self):
        """Gets the abbreviation of this Team.  # noqa: E501


        :return: The abbreviation of this Team.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this Team.


        :param abbreviation: The abbreviation of this Team.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def tri_code(self):
        """Gets the tri_code of this Team.  # noqa: E501


        :return: The tri_code of this Team.  # noqa: E501
        :rtype: str
        """
        return self._tri_code

    @tri_code.setter
    def tri_code(self, tri_code):
        """Sets the tri_code of this Team.


        :param tri_code: The tri_code of this Team.  # noqa: E501
        :type: str
        """

        self._tri_code = tri_code

    @property
    def team_name(self):
        """Gets the team_name of this Team.  # noqa: E501


        :return: The team_name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._team_name

    @team_name.setter
    def team_name(self, team_name):
        """Sets the team_name of this Team.


        :param team_name: The team_name of this Team.  # noqa: E501
        :type: str
        """

        self._team_name = team_name

    @property
    def location_name(self):
        """Gets the location_name of this Team.  # noqa: E501


        :return: The location_name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this Team.


        :param location_name: The location_name of this Team.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def first_year_of_play(self):
        """Gets the first_year_of_play of this Team.  # noqa: E501


        :return: The first_year_of_play of this Team.  # noqa: E501
        :rtype: float
        """
        return self._first_year_of_play

    @first_year_of_play.setter
    def first_year_of_play(self, first_year_of_play):
        """Sets the first_year_of_play of this Team.


        :param first_year_of_play: The first_year_of_play of this Team.  # noqa: E501
        :type: float
        """

        self._first_year_of_play = first_year_of_play

    @property
    def division(self):
        """Gets the division of this Team.  # noqa: E501


        :return: The division of this Team.  # noqa: E501
        :rtype: StandingsDivision
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this Team.


        :param division: The division of this Team.  # noqa: E501
        :type: StandingsDivision
        """

        self._division = division

    @property
    def conference(self):
        """Gets the conference of this Team.  # noqa: E501


        :return: The conference of this Team.  # noqa: E501
        :rtype: DivisionConference
        """
        return self._conference

    @conference.setter
    def conference(self, conference):
        """Sets the conference of this Team.


        :param conference: The conference of this Team.  # noqa: E501
        :type: DivisionConference
        """

        self._conference = conference

    @property
    def franchise(self):
        """Gets the franchise of this Team.  # noqa: E501


        :return: The franchise of this Team.  # noqa: E501
        :rtype: Franchise
        """
        return self._franchise

    @franchise.setter
    def franchise(self, franchise):
        """Sets the franchise of this Team.


        :param franchise: The franchise of this Team.  # noqa: E501
        :type: Franchise
        """

        self._franchise = franchise

    @property
    def roster(self):
        """Gets the roster of this Team.  # noqa: E501


        :return: The roster of this Team.  # noqa: E501
        :rtype: TeamRoster
        """
        return self._roster

    @roster.setter
    def roster(self, roster):
        """Sets the roster of this Team.


        :param roster: The roster of this Team.  # noqa: E501
        :type: TeamRoster
        """

        self._roster = roster

    @property
    def next_game_schedule(self):
        """Gets the next_game_schedule of this Team.  # noqa: E501


        :return: The next_game_schedule of this Team.  # noqa: E501
        :rtype: TeamNextGameSchedule
        """
        return self._next_game_schedule

    @next_game_schedule.setter
    def next_game_schedule(self, next_game_schedule):
        """Sets the next_game_schedule of this Team.


        :param next_game_schedule: The next_game_schedule of this Team.  # noqa: E501
        :type: TeamNextGameSchedule
        """

        self._next_game_schedule = next_game_schedule

    @property
    def short_name(self):
        """Gets the short_name of this Team.  # noqa: E501


        :return: The short_name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Team.


        :param short_name: The short_name of this Team.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def official_site_url(self):
        """Gets the official_site_url of this Team.  # noqa: E501


        :return: The official_site_url of this Team.  # noqa: E501
        :rtype: str
        """
        return self._official_site_url

    @official_site_url.setter
    def official_site_url(self, official_site_url):
        """Sets the official_site_url of this Team.


        :param official_site_url: The official_site_url of this Team.  # noqa: E501
        :type: str
        """

        self._official_site_url = official_site_url

    @property
    def franchise_id(self):
        """Gets the franchise_id of this Team.  # noqa: E501


        :return: The franchise_id of this Team.  # noqa: E501
        :rtype: float
        """
        return self._franchise_id

    @franchise_id.setter
    def franchise_id(self, franchise_id):
        """Sets the franchise_id of this Team.


        :param franchise_id: The franchise_id of this Team.  # noqa: E501
        :type: float
        """

        self._franchise_id = franchise_id

    @property
    def active(self):
        """Gets the active of this Team.  # noqa: E501


        :return: The active of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Team.


        :param active: The active of this Team.  # noqa: E501
        :type: bool
        """

        self._active = active

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
        if not isinstance(other, Team):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other