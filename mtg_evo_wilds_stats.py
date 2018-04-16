from mtg_start_file import *
from mtgSpells import draw, tutor, direct_damage, life_gain, removal, play_creature, draw_card


def play_land(mana, deck, hand, field, graveyard):
    d = field.count(2)
    e = field.count(3)
    f = field.count(4)
    snap_shot = [d, e, f]
    if mana == 1:
        field.append(2)
        hand.remove(2)
    if mana == 2:
        if 10 in hand:
            graveyard.append(10)
            hand.remove(10)
            if d >= e:
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif e >= d:
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif 2 in deck:
                deck.remove(2)
                field.append(2)
                return deck, hand, field, graveyard, snap_shot, 1
            elif 3 in deck:
                deck.remove(3)
                field.append(3)
                return deck, hand, field, graveyard, snap_shot, 1
        if d <= e:
            if 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard, snap_shot
        if e <= d:
            if 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard, snap_shot
        if 2 in hand:
            field.append(2)
            hand.remove(2)
            return deck, hand, field, graveyard, snap_shot
        if 3 in hand:
            field.append(3)
            hand.remove(3)
            return deck, hand, field, graveyard, snap_shot
        else:
            return deck, hand, field, graveyard, snap_shot
    elif mana == 3:
        if 10 in hand:
            graveyard.append(10)
            hand.remove(10)
            if e <= d and e <= f:
                if 3 in deck:
                    deck.remove(3)
                    field.append(3)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif d <= e and d <= f:
                if 2 in deck:
                    deck.remove(2)
                    field.append(2)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif f <= d and f <= e:
                if 4 in deck:
                    deck.remove(4)
                    field.append(4)
                    return deck, hand, field, graveyard, snap_shot, 1
            elif 2 in deck:
                deck.remove(2)
                field.append(2)
                return deck, hand, field, graveyard, snap_shot, 1
            elif 3 in deck:
                deck.remove(3)
                field.append(3)
                return deck, hand, field, graveyard, snap_shot, 1
            elif 4 in deck:
                deck.remove(4)
                field.append(4)
                return deck, hand, field, graveyard, snap_shot, 1
        if d <= e and d <= f:
            if 2 in hand:
                field.append(2)
                hand.remove(2)
                return deck, hand, field, graveyard, snap_shot
        if e <= d and e <= f:
            if 3 in hand:
                field.append(3)
                hand.remove(3)
                return deck, hand, field, graveyard, snap_shot
        if f <= d and f <= e:
            if 4 in hand:
                field.append(4)
                hand.remove(4)
                return deck, hand, field, graveyard, snap_shot
        if 2 in hand:
            field.append(2)
            hand.remove(2)
            return deck, hand, field, graveyard, snap_shot
        if 3 in hand:
            field.append(3)
            hand.remove(3)
            return deck, hand, field, graveyard, snap_shot
        if 4 in hand:
            field.append(4)
            hand.remove(4)
            return deck, hand, field, graveyard, snap_shot
        else:
            return deck, hand, field, graveyard, snap_shot


def check_field(hand, field, evo, mana):
    a = field.count(2)
    b = field.count(3)
    c = field.count(4)
    available_mana = [a, b, c]
    if mana == 2:
        if evo == 1 and a == 1 and b == 1 or a == 3 and b == 3:
            available_mana[0] -= 1
            return play_creature(hand, field, mana, available_mana)
        else:
            return play_creature(hand, field, mana, available_mana)
    elif mana == 3:
        if evo == 1 and a == 1 and b == 1 and c == 1 or a == 2 and b == 2 and c == 2:
                available_mana[0] -= 1
                return play_creature(hand, field, mana, available_mana)
        else:
            return play_creature(hand, field, mana, available_mana)


def check_creatures(battlefield):
    damage = 0
    small = battlefield.count(8)
    big = battlefield.count(77)
    if 8 in battlefield:
        damage += small
    elif 77 in battlefield:
        big *= 5
        damage += big
    return damage


def main_phase(hand, deck, field, graveyard, mana):
    was_evo_played = play_land(mana, deck, hand, field, graveyard)
    len_evo = len(was_evo_played)
    snap_shot = was_evo_played[4]
    if len_evo == 6:
        mana_left = check_field(hand, field, 1, mana)
        return hand, deck, field, snap_shot, mana_left
    else:
        mana_left = check_field(hand, field, 0, mana)
        return hand, deck, field, snap_shot, mana_left


def check_snap_shot(x, field):
    a = field.count(2)
    b = field.count(3)
    c = field.count(4)
    field_tots = a + b + c
    mana_stuck = 0
    for x, y in zip(x, x[1:]):
        if x == y:
            mana_stuck += 1
        elif x == 0 and y == 0:
            mana_stuck += 1
    if mana_stuck > 3 and field_tots <= 4:
        # print("Mana starved.")
        return 0
    else:
        return 1


def combat_phase(p1_field, p1_life_total, p1_turns, p1_deck, p2_field, p2_life_total, p2_turns, p2_deck, no_summoning_sickness, player):
    p1_creatures = check_creatures(p1_field)
    p2_creatures = check_creatures(p2_field)
    if player == "P1":
        p1_creatures -= no_summoning_sickness
    elif player == "P2":
        p2_creatures -= no_summoning_sickness
    if p1_creatures > p2_creatures:
        damage = (p1_creatures - p2_creatures) + 1
        p2_life_total -= damage
        # print("player 2 took damage")
    elif p1_creatures < p2_creatures:
        damage = (p2_creatures - p1_creatures) + 1
        p1_life_total -= damage
        # print("PLAYER 1 took damage")

    if p1_life_total <= 0:
        stats = ["P2", p2_turns]
        return stats
    if p2_life_total <= 0:
        stats = ["P1", p1_turns]
        return stats
    if len(p1_deck) == 0:
        stats = ["P2", p2_turns]
        return stats
    if len(p2_deck) == 0:
        stats = ["P1", p1_turns]
        return stats
    else:
        life_status = [p1_life_total, p2_life_total]
        return life_status
