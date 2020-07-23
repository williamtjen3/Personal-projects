import math
import random


class Card:

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        try:
            string = self.value+self.suit[0]
            return string
        except TypeError:
            string = str(self.value)+self.suit[0]
            return string

    def suit(self):
        return self.suit

    def value(self):
        return self.value


class Deck(Card):

    def __init__(self, player_no):
        self.cards = []
        self.build(player_no)
        self.shuffle()

    def show(self):
        for i in self.cards:
            print(i)

    def build(self, player_no):
        for i in range(math.ceil(player_no/4)):
            for suit in ["spade", "heart", "clover", "diamond"]:
                for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]:
                    self.cards.append(Card(suit, val))

    def shuffle(self):
        self.cards = random.shuffle(self.cards)


class Player:
    pass
