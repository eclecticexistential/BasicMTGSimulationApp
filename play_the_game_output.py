from mtg_evo_wilds_stats import *
from collect_stats import game_stats


def play_the_game(player_one, player_two, mana, goes_first, game_num):
    p1_deck, p1_hand, p1_field, p1_grave = player_one
    p2_deck, p2_hand, p2_field, p2_grave = player_two
    p1_turns = 0
    p2_turns = 0
    p1_ss = []
    p2_ss = []
    if len(p1_deck) < 93:
        p1_life = 20
        p2_life = 20
    else:
        p1_life = 40
        p2_life = 40
    ticker = 0
    ticker2 = 0
    method = ""
    no_draw = 0
    no_draw2 = 0
# taking turns... goes_first determines who plays first
    if goes_first == 0:
        while True:
            # print()
            # print("Start of Round {}.".format(p1_turns + 1))
            # print("Player1 Field {} Hand {} Graveyard {} Life Total {}".format(p1_field, p1_hand, p1_grave, p1_life))
            # print("Player2 Field {} Hand {} Graveyard {} Life Total {} ".format(p2_field, p2_hand, p2_grave, p2_life))

            if no_draw != 0:
                try:
                    p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
                except TypeError:
                    stats = ["P2", p2_turns]
                    game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                               winner=True, goes_first=goes_first)
                    return stats
                if p1new_deck == []:
                    stats = ["P2", p2_turns]
                    game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                               winner=True, goes_first=goes_first)
                    return stats
            elif no_draw == 0:
                p1new_deck, p1new_hand = p1_deck, p1_hand
            p1start_num_creatures = p1_field.count(8) + p1_field.count(77)
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck,
                                                                               p1_field, p1_grave, mana)
            p1now_num_creatures = p1_field.count(8) + p1_field.count(77)
            p1no_summoning_sickness = p1start_num_creatures - p1now_num_creatures

            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None,
                           method="ManaStarved", winner=True, goes_first=goes_first)
                return stats
            if p1untapped_mana is not None:
                # print(p1untapped_mana)
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    if 13 in p1_hand:
                        stats = direct_damage(p1_hand, p1_grave, p1untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 18 in p1_hand and 8 in p2_field or 77 in p2_field:
                        removal(p1_hand, p2_field, p1_grave, p2_grave, p1untapped_mana, mana, 'P1')
                    if len(p1_hand) < 7:
                        if 17 in p1_hand:
                            draw_card(p1_deck, p1_hand, p1_grave, mana, p1untapped_mana)
                    if p1_life >= 3 and 66 in p1_hand and len(p1_hand) < 6:
                        stats = tutor(p1_hand, p1_deck, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 9 in p1_hand:
                        stats = life_gain(p1_hand, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[1] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]

            if p1no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck,
                                      p1no_summoning_sickness, "P1")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_P2 != p2_life and before_p1 == p1_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat",
                               winner=True, goes_first=goes_first)
                    return health

            # main phase two
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    if 13 in p1_hand:
                        stats = direct_damage(p1_hand, p1_grave, p1untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                                if ticker == 0:
                                    method == "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 18 in p1_hand and 8 in p2_field or 77 in p2_field:
                        removal(p1_hand, p2_field, p1_grave, p2_grave, p1untapped_mana, mana, 'P1')
                    if len(p1_hand) < 7:
                        if 17 in p1_hand:
                            draw_card(p1_deck, p1_hand, p1_grave, mana, p1untapped_mana)
                    if p1_life >= 3 and 66 in p1_hand and len(p1_hand) < 6:
                        stats = tutor(p1_hand, p1_deck, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 9 in p1_hand:
                        stats = life_gain(p1_hand, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[1] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]

            p1_turns += 1
            hand_check(p1_hand, p1_grave)

            if p2_life < 20 and ticker == 1:
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker += 1

            ### player two's turn
            if no_draw == 0:
                no_draw += 1
            try:
                p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
            except TypeError:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p2new_deck == []:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None,
                           method="Milled", winner=True, goes_first=goes_first)
                return stats

            p2start_num_creatures = p2_field.count(8) + p2_field.count(77)
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2now_num_creatures = p1_field.count(8) + p2_field.count(77)
            p2no_summoning_sickness = p2start_num_creatures - p2now_num_creatures
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="ManaStarved",
                           winner=True, goes_first=goes_first)
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    if 13 in p2_hand:
                        stats = direct_damage(p2_hand, p2_grave, p2untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 18 in p2_hand and 8 in p1_field or 77 in p1_field:
                        removal(p2_hand, p1_field, p2_grave, p1_grave, p2untapped_mana, mana, 'P2')
                    if len(p2_hand) < 7:
                        if 17 in p2_hand:
                            draw_card(p2_deck, p2_hand, p2_grave, mana, p2untapped_mana)
                    if p2_life >= 3 and 66 in p2_hand and len(p2_hand) < 6:
                        stats = tutor(p2_hand, p2_deck, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 9 in p2_hand:
                        stats = life_gain(p2_hand, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[1] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
            if p2no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck, p2no_summoning_sickness, "P2")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_p1 != p1_life and before_P2 == p2_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat", winner=True,
                               goes_first=goes_first)
                    return health

            # main phase two

            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    if 13 in p2_hand:
                        stats = direct_damage(p2_hand, p2_grave, p2untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 18 in p2_hand and 8 in p1_field or 77 in p1_field:
                        removal(p2_hand, p1_field, p2_grave, p1_grave, p2untapped_mana, mana, 'P2')
                    if len(p2_hand) < 7:
                        if 17 in p2_hand:
                            draw_card(p2_deck, p2_hand, p2_grave, mana, p2untapped_mana)
                    if p2_life >= 3 and 66 in p2_hand and len(p2_hand) < 6:
                        stats = tutor(p2_hand, p2_deck, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 9 in p2_hand:
                        stats = life_gain(p2_hand, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[1] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]

            p2_turns += 1
            hand_check(p2_hand, p2_grave)

            if p1_life < 20 and ticker == 1:
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker += 1

    if goes_first == 1:
        while True:
            # print()
            # print("Start of Round {}.".format(p2_turns +1))
            # print("Player2 Field {} Hand {} Graveyard {} Life Total {}".format(p2_field, p2_hand, p2_grave, p2_life))
            # print("Player1 Field {} Hand {} Graveyard {} Life Total {} ".format(p1_field, p1_hand, p1_grave, p1_life))
            if no_draw2 != 0:
                try:
                    p2new_deck, p2new_hand = draw(p2_deck, p2_hand)
                except TypeError:
                    stats = ["P1", p1_turns]
                    game_stats(p1_turns, "P1", mana, game_num, hand=None, method="Milled",
                               winner=True, goes_first=goes_first)
                    return stats
                if p2new_deck == []:
                    stats = ["P1", p1_turns]
                    game_stats(p1_turns, "P1", mana, game_num, hand=None,
                               method="Milled", winner=True, goes_first=goes_first)
                    return stats
            elif no_draw2 == 0:
                p2new_deck, p2new_hand = p2_deck, p2_hand

            p2start_num_creatures = p2_field.count(8) + p2_field.count(77)
            p2_hand, p2_deck, p2_field, p2add_to, p2untapped_mana = main_phase(p2new_hand, p2new_deck, p2_field, p2_grave, mana)
            p2now_num_creatures = p1_field.count(8) + p2_field.count(77)
            p2no_summoning_sickness = p2start_num_creatures - p2now_num_creatures
            p2_ss.append(p2add_to)
            mana_fed = check_snap_shot(p2_ss, p2_field)
            if mana_fed == 0:
                stats = ["P1", p1_turns]
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method="ManaStarved",
                           winner=True, goes_first=goes_first)
                return stats
            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    if 13 in p2_hand:
                        stats = direct_damage(p2_hand, p2_grave, p2untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 18 in p2_hand and 8 in p1_field or 77 in p1_field:
                        removal(p2_hand, p1_field, p2_grave, p1_grave, p2untapped_mana, mana, 'P2')
                    if len(p2_hand) < 7:
                        if 17 in p2_hand:
                            draw_card(p2_deck, p2_hand, p2_grave, mana, p2untapped_mana)
                    if p2_life >= 3 and 66 in p2_hand and len(p2_hand) < 6:
                        stats = tutor(p2_hand, p2_deck, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 9 in p2_hand:
                        stats = life_gain(p2_hand, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[1] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
            if p2no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck, p2no_summoning_sickness, "P2")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_p1 != p1_life and before_P2 == p2_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat", winner=True,
                               goes_first=goes_first)
                    return health

             # main phase two

            if p2untapped_mana is not None:
                p2current = p2untapped_mana[0] + p2untapped_mana[1] + p2untapped_mana[2]
                if p2current > 0:
                    if 13 in p2_hand:
                        stats = direct_damage(p2_hand, p2_grave, p2untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 18 in p2_hand and 8 in p1_field or 77 in p1_field:
                        removal(p2_hand, p1_field, p2_grave, p1_grave, p2untapped_mana, mana, 'P2')
                    if len(p2_hand) < 7:
                        if 17 in p2_hand:
                            draw_card(p2_deck, p2_hand, p2_grave, mana, p2untapped_mana)
                    if p2_life >= 3 and 66 in p2_hand and len(p2_hand) < 6:
                        stats = tutor(p2_hand, p2_deck, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]
                    if 9 in p2_hand:
                        stats = life_gain(p2_hand, p2_grave, p2untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[1] != p2_life:
                                p2_life = stats[0]
                            if stats[1] != p2untapped_mana:
                                p2untapped_mana = stats[1]

            p2_turns += 1
            hand_check(p2_hand, p2_grave)

            if p1_life < 20 and ticker2 == 1:
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker2 += 1

            # Player Evo's turn
            if no_draw2 == 0:
                no_draw2 += 1
            try:
                p1new_deck, p1new_hand = draw(p1_deck, p1_hand)
            except TypeError:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats
            if p1new_deck == []:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None, method="Milled",
                           winner=True, goes_first=goes_first)
                return stats

            p1start_num_creatures = p1_field.count(8) + p1_field.count(77)
            p1_hand, p1_deck, p1_field, p1add_to, p1untapped_mana = main_phase(p1new_hand, p1new_deck,
                                                                               p1_field, p1_grave, mana)
            p1now_num_creatures = p1_field.count(8) + p1_field.count(77)
            p1no_summoning_sickness = p1start_num_creatures - p1now_num_creatures

            p1_ss.append(p1add_to)
            mana_fed = check_snap_shot(p1_ss, p1_field)
            if mana_fed == 0:
                stats = ["P2", p2_turns]
                game_stats(p2_turns, "P2", mana, game_num, hand=None,
                           method="ManaStarved", winner=True, goes_first=goes_first)
                return stats
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    if 13 in p1_hand:
                        stats = direct_damage(p1_hand, p1_grave, p1untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 18 in p1_hand and 8 in p2_field or 77 in p2_field:
                        removal(p1_hand, p2_field, p1_grave, p2_grave, p1untapped_mana, mana, 'P1')
                    if len(p1_hand) < 7:
                        if 17 in p1_hand:
                            draw_card(p1_deck, p1_hand, p1_grave, mana, p1untapped_mana)
                    if p1_life >= 3 and 66 in p1_hand and len(p1_hand) < 6:
                        stats = tutor(p1_hand, p1_deck, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 9 in p1_hand and p1untapped_mana is not None:
                        stats = life_gain(p1_hand, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[1] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
            if p1no_summoning_sickness > -1:
                health = combat_phase(p1_field, p1_life, p1_turns, p1_deck, p2_field, p2_life, p2_turns, p2_deck,
                                      p1no_summoning_sickness, "P1")
                if health[0] != "P1" and health[0] != "P2":
                    before_p1 = p1_life
                    before_P2 = p2_life
                    p1_life = health[0]
                    p2_life = health[1]
                    if before_P2 != p2_life and before_p1 == p1_life and ticker == 0:
                        method = "Combat Damage"
                        ticker += 1
                else:
                    game_stats(health[1], health[0], mana, game_num, hand=None, method="Combat",
                               winner=True, goes_first=goes_first)
                    return health

            # main phase two
            if p1untapped_mana is not None:
                p1current = p1untapped_mana[0] + p1untapped_mana[1] + p1untapped_mana[2]
                if p1current > 0:
                    if 13 in p1_hand:
                        stats = direct_damage(p1_hand, p1_grave, p1untapped_mana, p2_life, mana)
                        if stats is not None:
                            if stats[0] != p2_life:
                                p2_life = stats[0]
                                if ticker == 0:
                                    method = "Lightning Bolt"
                                    ticker += 1
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 18 in p1_hand and 8 in p2_field or 77 in p2_field:
                        removal(p1_hand, p2_field, p1_grave, p2_grave, p1untapped_mana, mana, 'P1')
                    if len(p1_hand) < 7:
                        if 17 in p1_hand:
                            draw_card(p1_deck, p1_hand, p1_grave, mana, p1untapped_mana)
                    if p1_life >= 3 and 66 in p1_hand and len(p1_hand) < 6:
                        stats = tutor(p1_hand, p1_deck, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[0] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]
                    if 9 in p1_hand:
                        stats = life_gain(p1_hand, p1_grave, p1untapped_mana, p1_life, mana)
                        if stats is not None:
                            if stats[1] != p1_life:
                                p1_life = stats[0]
                            if stats[1] != p1untapped_mana:
                                p1untapped_mana = stats[1]

            p1_turns += 1
            hand_check(p1_hand, p1_grave)

            if p2_life < 20 and ticker2 == 0:
                game_stats(p1_turns, "P1", mana, game_num, hand=None, method=method, winner=None, goes_first=goes_first)
                ticker2 += 1


def status():
    p1_dice_roll = dice()
    p2_dice_roll = dice()
    goes_first = 0
    if p1_dice_roll < p2_dice_roll:
        goes_first = 1
    return goes_first


def out_of_all_games(cc, mana, num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo):
    # evo_wilds_wins = 0
    # non_evo_wins = 0
    games = 100
    while games >= 1:
        goes_first = status()
        if goes_first == 0:
            player_one = establish_field(cc, mana, games, goes_first, "P1", num_lands,
                                         removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo)
            if player_one is False:
                # non_evo_wins += 1
                games -= 1
            elif player_one:
                player_two = establish_field(cc, mana, games, goes_first, "P2", num_lands,
                                             removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs,)
                if player_two is False:
                    # evo_wilds_wins += 1
                    games -= 1
            if player_one and player_two:
                winner = play_the_game(player_one, player_two, mana, goes_first, games)
                # appends num of draws into win condition if player won
                if winner[0] == "P1":
                    # evo_wilds_wins += 1
                    # print("Evo wins {}".format(games))
                    games -= 1
                elif winner[0] == "P2":
                    # non_evo_wins += 1
                    # print("Non-Evo wins {}".format(games))
                    games -= 1
        if goes_first == 1:
            player_two = establish_field(cc, mana, games, goes_first, "P2", num_lands, removal,
                                         life_gain, tutor, draw_cards, combat_tricks, lil, bombs)
            if player_two is False:
                # evo_wilds_wins += 1
                games -= 1
            elif player_two:
                player_one = establish_field(cc, mana, games, goes_first, "P1", num_lands, removal,
                                             life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evo)
                if player_one is False:
                    # non_evo_wins += 1
                    games -= 1
            if player_two and player_one:
                winner = play_the_game(player_one, player_two, mana, goes_first, games)
                # appends num of draws into win condition if player won
                if winner[0] == "P1" and winner[1] != 0:
                    # evo_wilds_wins += 1
                    # print("Evo wins {}".format(games))
                    games -= 1
                elif winner[0] == "P2" and winner[1] != 0:
                    # non_evo_wins += 1
                    # print("Non-Evo wins {}".format(games))
                    games -= 1

    # print()
    # print("Stats for {} Mana Limited Deck \n".format(mana))
    # print("Evo Deck Wins {}".format(evo_wilds_wins))
    # print("Non Evo Deck Wins {}".format(non_evo_wins))

