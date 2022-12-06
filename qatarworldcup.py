from match import Match
from qwcobject import QatarWoldCupObject
from configuration import WorldCupConfiguration
from group import Group

class QatarWorldCup(QatarWoldCupObject):

    def __init__(self):
        self.played = False
        self.wcc = WorldCupConfiguration()
        self.group_a = Group.group_a()
        self.group_b = Group.group_b()
        self.group_c = Group.group_c()
        self.group_d = Group.group_d()
        self.group_e = Group.group_e()
        self.group_f = Group.group_f()
        self.group_g = Group.group_g()
        self.group_h = Group.group_h()
        # Eighth finals
        self.m51_8th_1B_vs_2A = None
        self.m49_8th_1A_vs_2B = None
        self.m52_8th_1D_vs_2C = None
        self.m50_8th_1C_vs_2D = None
        self.m56_8th_1H_vs_2G = None
        self.m54_8th_1G_vs_2H = None
        self.m55_8th_1F_vs_2E = None
        self.m53_8th_1E_vs_2F = None
        # Quarter finals
        self.m59_4th_m51_vs_m52 = None
        self.m60_4th_m55_vs_m56 = None
        self.m57_4th_m49_vs_m50 = None
        self.m58_4th_m53_vs_m54 = None
        # Semi finals
        self.m61_sf_m57_vs_m58 = None
        self.m62_sf_m59_vs_m60 = None
        # Final
        self.m64_final = None
        self.m63_3rd_place = None

    def play(self):
        self.played = True
        winners = []
        self.play_eighth_finals()
        self.play_quarter_finals()
        self.play_semi_finals()
        self.play_final()
        winners.append(self.m64_final.winner)
        winners.append(self.m64_final.looser)
        winners.append(self.m63_3rd_place.winner)
        winners.append(self.m63_3rd_place.looser)
        return winners

    def play_eighth_finals(self):
        winners_a = self.group_a.winners()
        winners_b = self.group_b.winners()
        winners_c = self.group_c.winners()
        winners_d = self.group_d.winners()
        winners_e = self.group_e.winners()
        winners_f = self.group_f.winners()
        winners_g = self.group_g.winners()
        winners_h = self.group_h.winners()

        # Match 1 - 1B vs 2A
        self.m51_8th_1B_vs_2A = Match(winners_b[0], winners_a[1])

        # Match 2 - 1A vs 2B
        self.m49_8th_1A_vs_2B = Match(winners_a[0], winners_b[1])

        # Match 3 - 1D vs 2C
        self.m52_8th_1D_vs_2C = Match(winners_d[0], winners_c[1])

        # Match 4 - 1C vs 2D
        self.m50_8th_1C_vs_2D = Match(winners_c[0], winners_d[1])

        # Match 5 - 1H vs 2G
        self.m56_8th_1H_vs_2G = Match(winners_h[0], winners_g[1])

        # Match 6 - 1G vs 2H
        self.m54_8th_1G_vs_2H = Match(winners_g[0], winners_h[1])

        # Match 7 - 1F vs 2E
        self.m55_8th_1F_vs_2E = Match(winners_f[0], winners_e[1])

        # Match 8 - 1E vs 2F
        self.m53_8th_1E_vs_2F = Match(winners_e[0], winners_f[1])

    def play_quarter_finals(self):
        self.m59_4th_m51_vs_m52 = Match(self.m51_8th_1B_vs_2A.play(), self.m52_8th_1D_vs_2C.play())
        self.m60_4th_m55_vs_m56 = Match(self.m55_8th_1F_vs_2E.play(), self.m56_8th_1H_vs_2G.play())
        self.m57_4th_m49_vs_m50 = Match(self.m49_8th_1A_vs_2B.play(), self.m50_8th_1C_vs_2D.play())
        self.m58_4th_m53_vs_m54 = Match(self.m53_8th_1E_vs_2F.play(), self.m54_8th_1G_vs_2H.play())

    def play_semi_finals(self):
        self.m61_sf_m57_vs_m58 = Match(self.m57_4th_m49_vs_m50.play(), self.m58_4th_m53_vs_m54.play())
        self.m62_sf_m59_vs_m60 = Match(self.m59_4th_m51_vs_m52.play(), self.m60_4th_m55_vs_m56.play())

    def play_final(self):
        self.m64_final = Match(self.m61_sf_m57_vs_m58.play(), self.m62_sf_m59_vs_m60.play())
        self.m64_final.play()
        self.m63_3rd_place = Match(self.m61_sf_m57_vs_m58.looser, self.m62_sf_m59_vs_m60.looser)
        self.m63_3rd_place.play()

    def get_first_place(self):
        if self.played:
            return self.m64_final.winner

    def get_second_place(self):
        if self.played:
            return self.m64_final.looser

    def get_third_place(self):
        if self.played:
            return self.m63_3rd_place.winner

    def get_fourth_place(self):
        if self.played:
            return self.m63_3rd_place.looser

    def save(self):
        self.wcc.save(self)

