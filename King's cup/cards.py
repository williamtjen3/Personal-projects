suits = ["spade", "heart", "clover", "diamond"]

vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]


class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __repr__(self):
        try:
            return self.value+self.suit[0]
        except TypeError:
            return str(self.value)+self.suit[0]


class Deck(Card):

    def __init__(self, deck=1):
        self


class Player:
    pass
