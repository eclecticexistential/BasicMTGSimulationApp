from play_the_game_output import out_of_all_games
from collect_stats import get_open_hand_stats, get_first_blood_stats, get_mana_starved_stats, \
    get_who_wins_stats, get_draw_into_win_stats


class Game:
    def __init__(self, cc, mana, num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evos):
        self.cc = cc
        self.mana = mana
        self.num_lands = num_lands
        self.removal = removal
        self.life_gain = life_gain
        self.tutor = tutor
        self.draw_cards = draw_cards
        self.combat_tricks = combat_tricks
        self.lil = lil
        self.bombs = bombs
        self.evos = evos
        self.start_game = out_of_all_games(self.cc, self.mana, self.num_lands, self.removal, self.life_gain, self.tutor,
                                           self.draw_cards, self.combat_tricks, self.lil, self.bombs, self.evos)

    def open_hand(self):
        for data in get_open_hand_stats():
            yield data

    def first_blood(self):
        for data in get_first_blood_stats():
            yield data

    def mana_starved(self):
        for data in get_mana_starved_stats():
            yield data

    def who_wins(self):
        for data in get_who_wins_stats():
            yield data

    def draw_steps(self):
        for data in get_draw_into_win_stats():
            yield data


def provide_winner_insight(data):
    p1_wins_out_of_games = 0
    p2_wins_out_of_games = 0
    winner_went_first = 0
    winner_went_second = 0
    win_by_combat = 0
    win_by_no_mana = 0
    win_by_milled = 0
    winning_round = []
    for info in data.who_wins():
        if info[3] == 'P1':
            p1_wins_out_of_games += 1
            if info[5] == '0':
                winner_went_first += 1
            elif info[5] == '1':
                winner_went_second += 1
        elif info[3] == 'P2':
            p2_wins_out_of_games += 1
            if info[5] == '1':
                winner_went_first += 1
            elif info[5] == '0':
                winner_went_second += 1
        if info[4] == 'Combat':
            win_by_combat += 1
        elif info[4] == 'NoManaHand' or info[4] == 'ManaStarved':
            win_by_no_mana += 1
        elif info[4] == 'Milled':
            win_by_milled += 1
        if info[2] > 0:
            winning_round.append(info[2])
    p1_wins = p1_wins_out_of_games/100
    p2_wins = p2_wins_out_of_games/100
    went_first = winner_went_first/100
    went_second = winner_went_second/100
    combat_damage_win = win_by_combat/100
    no_mana = win_by_no_mana/100
    milled = win_by_milled/100
    win_round = sum(winning_round)/len(winning_round)
    return p1_wins, p2_wins, went_first, went_second, combat_damage_win, no_mana, milled, win_round

# cc, mana, num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evos
# commander_3m = Game(100, 3, 36, 10, 2, 7, 10, 10, 10, 15, 4)
# print(provide_winner_insight(commander_3m))
# print(provide_winner_insight(commander_3m))
# print(provide_winner_insight(commander_3m))
# print(provide_winner_insight(commander_3m))
# limited3m = Game(40, 3, 17, 4, 2, 2, 2, 3, 8, 2, 3)
# print(provide_winner_insight(limited3m, ww=True))
# print(provide_winner_insight(limited3m, wwf=True))
# print(provide_winner_insight(limited3m, wm=True))
# print(provide_winner_insight(limited3m, wr=True))
# limited2m = Game(40, 2, 17, 4, 2, 2, 2, 3, 8, 2, 2)
# print(provide_winner_insight(limited2m, ww=True))
# print(provide_winner_insight(limited2m, wwf=True))
# print(provide_winner_insight(limited2m, wm=True))
# print(provide_winner_insight(limited2m, wr=True))

# commander_2m = Game(100, 2, 36, 10, 2, 7, 10, 10, 10, 15, 4)
# print(provide_winner_insight(commander_2m, ww=True))
