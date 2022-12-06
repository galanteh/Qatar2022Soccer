#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Qatar 2022 Soccer is a project that aims to produce all the possible candidates to win.

import copy
from collections import Counter
from qwcobject import QatarWoldCupObject
from team import Team
from match import Match


class Group(QatarWoldCupObject):

    def __repr__(self):
        return f"<Group({self._teams})>"

    def __init__(self, one_team, second_team, third_team, fourth_team):
        self._matches = []
        self._teams = []
        self.add(one_team)
        self.add(second_team)
        self.add(third_team)
        self.add(fourth_team)
        self.generate_matches()

    def matches(self):
        return copy.deepcopy(self._matches)

    def teams(self):
        return copy.deepcopy(self._teams)

    def add(self, one_team):
        self._teams.append(one_team)

    def generate_matches(self):
        self._matches = Match.generate_matches(self.teams())

    def winners(self):
        results = (match.play() for match in self.matches())
        winners = []
        counter_results = Counter(results)
        # first
        winners.append(counter_results.most_common(2)[0][0])
        # second
        winners.append(counter_results.most_common(2)[1][0])
        return winners

    @classmethod
    def group_a(cls):
        return cls(Team.qatar(), Team.ecuador(), Team.senegal(), Team.netherlands())

    @classmethod
    def group_b(cls):
        return cls(Team.england(), Team.iran(), Team.usa(), Team.wales())

    @classmethod
    def group_c(cls):
        return cls(Team.argentina(), Team.saudi_arabia(), Team.mexico(), Team.poland())

    @classmethod
    def group_d(cls):
        return cls(Team.france(), Team.australia(), Team.denmark(), Team.tunisia())

    @classmethod
    def group_e(cls):
        return cls(Team.spain(), Team.costa_rica(), Team.germany(), Team.japan())

    @classmethod
    def group_f(cls):
        return cls(Team.belgium(), Team.canada(), Team.morocco(), Team.croatia())

    @classmethod
    def group_g(cls):
        return cls(Team.brazil(), Team.serbia(), Team.switzerland(), Team.cameroon())

    @classmethod
    def group_h(cls):
        return cls(Team.portugal(), Team.ghana(), Team.uruguay(), Team.korea_republic())
