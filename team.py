from qwcobject import QatarWoldCupObject
from configuration import WorldCupConfiguration
import random

class Team(QatarWoldCupObject):

    @classmethod
    def qatar(cls):
        return cls(country_name="Qatar", fifa_points = 1441.97)

    @classmethod
    def ecuador(cls):
        return cls(country_name="Ecuador", fifa_points = 1463.74)

    @classmethod
    def senegal(cls):
        return cls(country_name="Senegal", fifa_points = 1584.59)

    @classmethod
    def netherlands(cls):
        return cls(country_name="Netherlands", fifa_points = 1679.41)

    @classmethod
    def england(cls):
        return cls(country_name="England", fifa_points = 1737.46)

    @classmethod
    def iran(cls):
        return cls(country_name="Iran", fifa_points = 1558.64)

    @classmethod
    def usa(cls):
        return cls(country_name="USA", fifa_points = 1635.01)

    @classmethod
    def wales(cls):
        return cls(country_name="Wales", fifa_points=1582.13)

    @classmethod
    def argentina(cls):
        return cls(country_name="Argentina", fifa_points=1770.65)

    @classmethod
    def saudi_arabia(cls):
        return cls(country_name="Saudi Arabia", fifa_points=1435.74)

    @classmethod
    def mexico(cls):
        return cls(country_name="Mexico", fifa_points=1649.57)

    @classmethod
    def poland(cls):
        return cls(country_name="Poland", fifa_points=1546.18)

    @classmethod
    def france(cls):
        return cls(country_name="France", fifa_points=1764.85)

    @classmethod
    def australia(cls):
        return cls(country_name="Australia", fifa_points=1483.73)

    @classmethod
    def denmark(cls):
        return cls(country_name="Denmark", fifa_points=1665.47)

    @classmethod
    def tunisia(cls):
        return cls(country_name="Tunisia", fifa_points=1507.86)

    @classmethod
    def spain(cls):
        return cls(country_name="Spain", fifa_points=1716.93)

    @classmethod
    def costa_rica(cls):
        return cls(country_name="Costa Rica", fifa_points=1500.06)

    @classmethod
    def germany(cls):
        return cls(country_name="Germany", fifa_points=1658.96)

    @classmethod
    def japan(cls):
        return cls(country_name="Japan", fifa_points=1554.69)

    @classmethod
    def belgium(cls):
        return cls(country_name="Belgium", fifa_points=1821.92)

    @classmethod
    def canada(cls):
        return cls(country_name="Canada", fifa_points=1473.82)

    @classmethod
    def morocco(cls):
        return cls(country_name="Morocco", fifa_points=1558.35)

    @classmethod
    def croatia(cls):
        return cls(country_name="Croatia", fifa_points=1632.15)

    @classmethod
    def brazil(cls):
        return cls(country_name="Brazil", fifa_points=1837.56)

    @classmethod
    def serbia(cls):
        return cls(country_name="Serbia", fifa_points=1549.53)

    @classmethod
    def switzerland(cls):
        return cls(country_name="Switzerland", fifa_points=1621.43)

    @classmethod
    def cameroon(cls):
        return cls(country_name="Cameroon", fifa_points=1484.95)

    @classmethod
    def portugal(cls):
        return cls(country_name="Portugal", fifa_points=1678.65)

    @classmethod
    def ghana(cls):
        return cls(country_name="Ghana", fifa_points=1393.47)

    @classmethod
    def uruguay(cls):
        return cls(country_name="Uruguay", fifa_points=1640.95)

    @classmethod
    def korea_republic(cls):
        return cls(country_name="Korea Republic", fifa_points=1526.02)

    def __eq__(self, other):
        return self.country_name == other.country_name

    def __hash__(self):
        return hash((self.fifa_points, self.country_name))

    def __repr__(self):
        return f"<Team({self.country_name}: {self.fifa_points})>"

    def __init__(self, country_name="", fifa_points=0.0):
        self.country_name = country_name
        self.fifa_points = fifa_points

    def __ge__(self, other_team):
        if isinstance(other_team, Team):
            return self.fifa_points >= other_team.fifa_points
        else:
            return False

    def __lt__(self, other_team):
        if isinstance(other_team, Team):
            return self.fifa_points < other_team.fifa_points
        else:
            return False

    def spread_fifa_points(self):
        wcc = WorldCupConfiguration()
        return wcc.automatic_points_required_to_win

    def play(self, other_team):
        difference = self.fifa_points - other_team.fifa_points
        if abs(difference) > self.spread_fifa_points():
            return max(self, other_team)
        else:
            return random.choice([self, other_team])
