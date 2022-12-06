import copy
from qwcobject import QatarWoldCupObject

class Match(QatarWoldCupObject):

    @classmethod
    def generate_matches(cls, team_list):
        opponents = copy.deepcopy(team_list)
        matches = []
        for one_team in team_list:
            opponents.remove(one_team)
            for one_opponent in opponents:
                matches.append(Match(one_team, one_opponent))
        return matches

    def __repr__(self):
        return f"<Match({self._teamA} vs {self._teamB})>"

    def __init__(self, local_team, visit_team):
        self._teamA = local_team
        self._teamB = visit_team
        self.winner = None
        self.looser = None

    def play(self):
        self.winner = self._teamA.play(self._teamB)
        if self.winner == self._teamA:
            self.looser = self._teamB
        else:
            self.looser = self._teamA
        return self.winner
