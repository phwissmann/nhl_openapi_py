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


class RegularSeasonStatRankingsStat(object):
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
        'games_played': 'str',
        'wins': 'str',
        'losses': 'str',
        'ot': 'str',
        'pts': 'str',
        'pt_pctg': 'str',
        'goals_per_game': 'str',
        'goals_against_per_game': 'str',
        'ev_gga_ratio': 'str',
        'power_play_percentage': 'str',
        'power_play_goals': 'str',
        'power_play_goals_against': 'str',
        'power_play_opportunities': 'str',
        'penalty_kill_percentage': 'str',
        'shots_per_game': 'str',
        'shots_allowed': 'str',
        'win_score_first': 'str',
        'win_opp_score_first': 'str',
        'win_lead_first_per': 'str',
        'win_lead_second_per': 'str',
        'win_outshoot_opp': 'str',
        'win_outshot_by_opp': 'str',
        'face_offs_taken': 'str',
        'face_offs_won': 'str',
        'face_offs_lost': 'str',
        'face_off_win_percentage': 'str',
        'shooting_pctg': 'str',
        'save_pctg': 'str'
    }

    attribute_map = {
        'games_played': 'gamesPlayed',
        'wins': 'wins',
        'losses': 'losses',
        'ot': 'ot',
        'pts': 'pts',
        'pt_pctg': 'ptPctg',
        'goals_per_game': 'goalsPerGame',
        'goals_against_per_game': 'goalsAgainstPerGame',
        'ev_gga_ratio': 'evGGARatio',
        'power_play_percentage': 'powerPlayPercentage',
        'power_play_goals': 'powerPlayGoals',
        'power_play_goals_against': 'powerPlayGoalsAgainst',
        'power_play_opportunities': 'powerPlayOpportunities',
        'penalty_kill_percentage': 'penaltyKillPercentage',
        'shots_per_game': 'shotsPerGame',
        'shots_allowed': 'shotsAllowed',
        'win_score_first': 'winScoreFirst',
        'win_opp_score_first': 'winOppScoreFirst',
        'win_lead_first_per': 'winLeadFirstPer',
        'win_lead_second_per': 'winLeadSecondPer',
        'win_outshoot_opp': 'winOutshootOpp',
        'win_outshot_by_opp': 'winOutshotByOpp',
        'face_offs_taken': 'faceOffsTaken',
        'face_offs_won': 'faceOffsWon',
        'face_offs_lost': 'faceOffsLost',
        'face_off_win_percentage': 'faceOffWinPercentage',
        'shooting_pctg': 'shootingPctg',
        'save_pctg': 'savePctg'
    }

    def __init__(self, games_played=None, wins=None, losses=None, ot=None, pts=None, pt_pctg=None, goals_per_game=None, goals_against_per_game=None, ev_gga_ratio=None, power_play_percentage=None, power_play_goals=None, power_play_goals_against=None, power_play_opportunities=None, penalty_kill_percentage=None, shots_per_game=None, shots_allowed=None, win_score_first=None, win_opp_score_first=None, win_lead_first_per=None, win_lead_second_per=None, win_outshoot_opp=None, win_outshot_by_opp=None, face_offs_taken=None, face_offs_won=None, face_offs_lost=None, face_off_win_percentage=None, shooting_pctg=None, save_pctg=None):  # noqa: E501
        """RegularSeasonStatRankingsStat - a model defined in OpenAPI"""  # noqa: E501

        self._games_played = None
        self._wins = None
        self._losses = None
        self._ot = None
        self._pts = None
        self._pt_pctg = None
        self._goals_per_game = None
        self._goals_against_per_game = None
        self._ev_gga_ratio = None
        self._power_play_percentage = None
        self._power_play_goals = None
        self._power_play_goals_against = None
        self._power_play_opportunities = None
        self._penalty_kill_percentage = None
        self._shots_per_game = None
        self._shots_allowed = None
        self._win_score_first = None
        self._win_opp_score_first = None
        self._win_lead_first_per = None
        self._win_lead_second_per = None
        self._win_outshoot_opp = None
        self._win_outshot_by_opp = None
        self._face_offs_taken = None
        self._face_offs_won = None
        self._face_offs_lost = None
        self._face_off_win_percentage = None
        self._shooting_pctg = None
        self._save_pctg = None
        self.discriminator = None

        if games_played is not None:
            self.games_played = games_played
        if wins is not None:
            self.wins = wins
        if losses is not None:
            self.losses = losses
        if ot is not None:
            self.ot = ot
        if pts is not None:
            self.pts = pts
        if pt_pctg is not None:
            self.pt_pctg = pt_pctg
        if goals_per_game is not None:
            self.goals_per_game = goals_per_game
        if goals_against_per_game is not None:
            self.goals_against_per_game = goals_against_per_game
        if ev_gga_ratio is not None:
            self.ev_gga_ratio = ev_gga_ratio
        if power_play_percentage is not None:
            self.power_play_percentage = power_play_percentage
        if power_play_goals is not None:
            self.power_play_goals = power_play_goals
        if power_play_goals_against is not None:
            self.power_play_goals_against = power_play_goals_against
        if power_play_opportunities is not None:
            self.power_play_opportunities = power_play_opportunities
        if penalty_kill_percentage is not None:
            self.penalty_kill_percentage = penalty_kill_percentage
        if shots_per_game is not None:
            self.shots_per_game = shots_per_game
        if shots_allowed is not None:
            self.shots_allowed = shots_allowed
        if win_score_first is not None:
            self.win_score_first = win_score_first
        if win_opp_score_first is not None:
            self.win_opp_score_first = win_opp_score_first
        if win_lead_first_per is not None:
            self.win_lead_first_per = win_lead_first_per
        if win_lead_second_per is not None:
            self.win_lead_second_per = win_lead_second_per
        if win_outshoot_opp is not None:
            self.win_outshoot_opp = win_outshoot_opp
        if win_outshot_by_opp is not None:
            self.win_outshot_by_opp = win_outshot_by_opp
        if face_offs_taken is not None:
            self.face_offs_taken = face_offs_taken
        if face_offs_won is not None:
            self.face_offs_won = face_offs_won
        if face_offs_lost is not None:
            self.face_offs_lost = face_offs_lost
        if face_off_win_percentage is not None:
            self.face_off_win_percentage = face_off_win_percentage
        if shooting_pctg is not None:
            self.shooting_pctg = shooting_pctg
        if save_pctg is not None:
            self.save_pctg = save_pctg

    @property
    def games_played(self):
        """Gets the games_played of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The games_played of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._games_played

    @games_played.setter
    def games_played(self, games_played):
        """Sets the games_played of this RegularSeasonStatRankingsStat.


        :param games_played: The games_played of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._games_played = games_played

    @property
    def wins(self):
        """Gets the wins of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The wins of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._wins

    @wins.setter
    def wins(self, wins):
        """Sets the wins of this RegularSeasonStatRankingsStat.


        :param wins: The wins of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._wins = wins

    @property
    def losses(self):
        """Gets the losses of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The losses of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._losses

    @losses.setter
    def losses(self, losses):
        """Sets the losses of this RegularSeasonStatRankingsStat.


        :param losses: The losses of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._losses = losses

    @property
    def ot(self):
        """Gets the ot of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The ot of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._ot

    @ot.setter
    def ot(self, ot):
        """Sets the ot of this RegularSeasonStatRankingsStat.


        :param ot: The ot of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._ot = ot

    @property
    def pts(self):
        """Gets the pts of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The pts of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._pts

    @pts.setter
    def pts(self, pts):
        """Sets the pts of this RegularSeasonStatRankingsStat.


        :param pts: The pts of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._pts = pts

    @property
    def pt_pctg(self):
        """Gets the pt_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The pt_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._pt_pctg

    @pt_pctg.setter
    def pt_pctg(self, pt_pctg):
        """Sets the pt_pctg of this RegularSeasonStatRankingsStat.


        :param pt_pctg: The pt_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._pt_pctg = pt_pctg

    @property
    def goals_per_game(self):
        """Gets the goals_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The goals_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._goals_per_game

    @goals_per_game.setter
    def goals_per_game(self, goals_per_game):
        """Sets the goals_per_game of this RegularSeasonStatRankingsStat.


        :param goals_per_game: The goals_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._goals_per_game = goals_per_game

    @property
    def goals_against_per_game(self):
        """Gets the goals_against_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The goals_against_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._goals_against_per_game

    @goals_against_per_game.setter
    def goals_against_per_game(self, goals_against_per_game):
        """Sets the goals_against_per_game of this RegularSeasonStatRankingsStat.


        :param goals_against_per_game: The goals_against_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._goals_against_per_game = goals_against_per_game

    @property
    def ev_gga_ratio(self):
        """Gets the ev_gga_ratio of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The ev_gga_ratio of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._ev_gga_ratio

    @ev_gga_ratio.setter
    def ev_gga_ratio(self, ev_gga_ratio):
        """Sets the ev_gga_ratio of this RegularSeasonStatRankingsStat.


        :param ev_gga_ratio: The ev_gga_ratio of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._ev_gga_ratio = ev_gga_ratio

    @property
    def power_play_percentage(self):
        """Gets the power_play_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The power_play_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._power_play_percentage

    @power_play_percentage.setter
    def power_play_percentage(self, power_play_percentage):
        """Sets the power_play_percentage of this RegularSeasonStatRankingsStat.


        :param power_play_percentage: The power_play_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._power_play_percentage = power_play_percentage

    @property
    def power_play_goals(self):
        """Gets the power_play_goals of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The power_play_goals of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._power_play_goals

    @power_play_goals.setter
    def power_play_goals(self, power_play_goals):
        """Sets the power_play_goals of this RegularSeasonStatRankingsStat.


        :param power_play_goals: The power_play_goals of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._power_play_goals = power_play_goals

    @property
    def power_play_goals_against(self):
        """Gets the power_play_goals_against of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The power_play_goals_against of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._power_play_goals_against

    @power_play_goals_against.setter
    def power_play_goals_against(self, power_play_goals_against):
        """Sets the power_play_goals_against of this RegularSeasonStatRankingsStat.


        :param power_play_goals_against: The power_play_goals_against of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._power_play_goals_against = power_play_goals_against

    @property
    def power_play_opportunities(self):
        """Gets the power_play_opportunities of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The power_play_opportunities of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._power_play_opportunities

    @power_play_opportunities.setter
    def power_play_opportunities(self, power_play_opportunities):
        """Sets the power_play_opportunities of this RegularSeasonStatRankingsStat.


        :param power_play_opportunities: The power_play_opportunities of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._power_play_opportunities = power_play_opportunities

    @property
    def penalty_kill_percentage(self):
        """Gets the penalty_kill_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The penalty_kill_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._penalty_kill_percentage

    @penalty_kill_percentage.setter
    def penalty_kill_percentage(self, penalty_kill_percentage):
        """Sets the penalty_kill_percentage of this RegularSeasonStatRankingsStat.


        :param penalty_kill_percentage: The penalty_kill_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._penalty_kill_percentage = penalty_kill_percentage

    @property
    def shots_per_game(self):
        """Gets the shots_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The shots_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._shots_per_game

    @shots_per_game.setter
    def shots_per_game(self, shots_per_game):
        """Sets the shots_per_game of this RegularSeasonStatRankingsStat.


        :param shots_per_game: The shots_per_game of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._shots_per_game = shots_per_game

    @property
    def shots_allowed(self):
        """Gets the shots_allowed of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The shots_allowed of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._shots_allowed

    @shots_allowed.setter
    def shots_allowed(self, shots_allowed):
        """Sets the shots_allowed of this RegularSeasonStatRankingsStat.


        :param shots_allowed: The shots_allowed of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._shots_allowed = shots_allowed

    @property
    def win_score_first(self):
        """Gets the win_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_score_first

    @win_score_first.setter
    def win_score_first(self, win_score_first):
        """Sets the win_score_first of this RegularSeasonStatRankingsStat.


        :param win_score_first: The win_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_score_first = win_score_first

    @property
    def win_opp_score_first(self):
        """Gets the win_opp_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_opp_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_opp_score_first

    @win_opp_score_first.setter
    def win_opp_score_first(self, win_opp_score_first):
        """Sets the win_opp_score_first of this RegularSeasonStatRankingsStat.


        :param win_opp_score_first: The win_opp_score_first of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_opp_score_first = win_opp_score_first

    @property
    def win_lead_first_per(self):
        """Gets the win_lead_first_per of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_lead_first_per of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_lead_first_per

    @win_lead_first_per.setter
    def win_lead_first_per(self, win_lead_first_per):
        """Sets the win_lead_first_per of this RegularSeasonStatRankingsStat.


        :param win_lead_first_per: The win_lead_first_per of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_lead_first_per = win_lead_first_per

    @property
    def win_lead_second_per(self):
        """Gets the win_lead_second_per of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_lead_second_per of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_lead_second_per

    @win_lead_second_per.setter
    def win_lead_second_per(self, win_lead_second_per):
        """Sets the win_lead_second_per of this RegularSeasonStatRankingsStat.


        :param win_lead_second_per: The win_lead_second_per of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_lead_second_per = win_lead_second_per

    @property
    def win_outshoot_opp(self):
        """Gets the win_outshoot_opp of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_outshoot_opp of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_outshoot_opp

    @win_outshoot_opp.setter
    def win_outshoot_opp(self, win_outshoot_opp):
        """Sets the win_outshoot_opp of this RegularSeasonStatRankingsStat.


        :param win_outshoot_opp: The win_outshoot_opp of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_outshoot_opp = win_outshoot_opp

    @property
    def win_outshot_by_opp(self):
        """Gets the win_outshot_by_opp of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The win_outshot_by_opp of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._win_outshot_by_opp

    @win_outshot_by_opp.setter
    def win_outshot_by_opp(self, win_outshot_by_opp):
        """Sets the win_outshot_by_opp of this RegularSeasonStatRankingsStat.


        :param win_outshot_by_opp: The win_outshot_by_opp of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._win_outshot_by_opp = win_outshot_by_opp

    @property
    def face_offs_taken(self):
        """Gets the face_offs_taken of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The face_offs_taken of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._face_offs_taken

    @face_offs_taken.setter
    def face_offs_taken(self, face_offs_taken):
        """Sets the face_offs_taken of this RegularSeasonStatRankingsStat.


        :param face_offs_taken: The face_offs_taken of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._face_offs_taken = face_offs_taken

    @property
    def face_offs_won(self):
        """Gets the face_offs_won of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The face_offs_won of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._face_offs_won

    @face_offs_won.setter
    def face_offs_won(self, face_offs_won):
        """Sets the face_offs_won of this RegularSeasonStatRankingsStat.


        :param face_offs_won: The face_offs_won of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._face_offs_won = face_offs_won

    @property
    def face_offs_lost(self):
        """Gets the face_offs_lost of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The face_offs_lost of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._face_offs_lost

    @face_offs_lost.setter
    def face_offs_lost(self, face_offs_lost):
        """Sets the face_offs_lost of this RegularSeasonStatRankingsStat.


        :param face_offs_lost: The face_offs_lost of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._face_offs_lost = face_offs_lost

    @property
    def face_off_win_percentage(self):
        """Gets the face_off_win_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The face_off_win_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._face_off_win_percentage

    @face_off_win_percentage.setter
    def face_off_win_percentage(self, face_off_win_percentage):
        """Sets the face_off_win_percentage of this RegularSeasonStatRankingsStat.


        :param face_off_win_percentage: The face_off_win_percentage of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._face_off_win_percentage = face_off_win_percentage

    @property
    def shooting_pctg(self):
        """Gets the shooting_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The shooting_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._shooting_pctg

    @shooting_pctg.setter
    def shooting_pctg(self, shooting_pctg):
        """Sets the shooting_pctg of this RegularSeasonStatRankingsStat.


        :param shooting_pctg: The shooting_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._shooting_pctg = shooting_pctg

    @property
    def save_pctg(self):
        """Gets the save_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501


        :return: The save_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :rtype: str
        """
        return self._save_pctg

    @save_pctg.setter
    def save_pctg(self, save_pctg):
        """Sets the save_pctg of this RegularSeasonStatRankingsStat.


        :param save_pctg: The save_pctg of this RegularSeasonStatRankingsStat.  # noqa: E501
        :type: str
        """

        self._save_pctg = save_pctg

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
        if not isinstance(other, RegularSeasonStatRankingsStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
