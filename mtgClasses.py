import math
import random


class Mana:
    def __init__(self, land_type=1, num_lands=17, evo=0):
        if land_type < 1:
            raise ValueError("Only super secret decks can run with no mana.")
        self.land_type = land_type
        self.num_lands = num_lands
        self.evo = evo
        self.mana = []
        self.totals = math.floor(num_lands / land_type)
        m_types = [2, 3, 4, 5, 6]
        for z in range(evo):
            self.mana.append(10)
        for y in range(self.land_type):
            for x in range(self.totals-evo):
                self.mana.append(m_types[y])
        while len(self.mana) != num_lands:
            rando = random.randint(0, self.land_type-1)
            self.mana.append(m_types[rando])

    def __iter__(self):
        for lands in self.mana:
            yield lands


class Spells:
    def __init__(self, removal=2, life_gain=2, tutor=2, draw_cards=2, combat_tricks=4):
        self.total_spells = {18: removal, 9: life_gain, 66: tutor, 17: draw_cards, 13: combat_tricks}
        if removal < 0 or life_gain < 0 or tutor < 0 or draw_cards < 0:
            raise ValueError("You're going to need a positive number of spells.")
        self.removal = removal
        self.life_gain = life_gain
        self.tutor = tutor
        self.draw_cards = draw_cards
        self.combat_tricks = combat_tricks
        self.spells = []
        for value in self.total_spells:
            for _ in range(self.total_spells[value]):
                self.spells.append(value)

    def __iter__(self):
        for spells in self.spells:
            yield spells


class Creatures:
    def __init__(self, lil=9, bombs=2):
        if lil < 5 or bombs < 1:
            raise ValueError("You're going to need some creatures")
        self.lil = lil
        self.bombs = bombs
        self.total_creatures = {8: lil, 77: bombs}
        self.creatures = []
        for value in self.total_creatures:
            for _ in range(self.total_creatures[value]):
                self.creatures.append(value)

    def __iter__(self):
        for creatures in self.creatures:
            yield creatures


class Deck:
    def __init__(self, total_cards=40, mana=Mana(), spells=Spells(), creatures=Creatures()):
        if total_cards < 40:
            raise ValueError("40 is the lowest card amount in all formats.")
        self.total_cards = total_cards
        self.mana = mana
        self.spells = spells
        self.creatures = creatures
        self.cards = []
        self.cards.extend(mana)
        self.cards.extend(spells)
        self.cards.extend(creatures)

        if len(self.cards) < self.total_cards:
            raise ValueError("Check total card count.")

    def __iter__(self):
        random.shuffle(self.cards)
        for card in self.cards:
            yield card


class Hand:
    def __init__(self, deck, cc=7):
        self.cc = cc
        self.hand = []
        self.deck = deck
        try:
            for _ in range(self.cc):
                for card in self.deck:
                    self.hand.append(card)
                    break
        except TypeError:
            print("Dunno yet. Hand {}, deck {}, cc {}.".format(self.hand, self.deck, self.cc))

    def __iter__(self):
        for card in self.hand:
            yield card
