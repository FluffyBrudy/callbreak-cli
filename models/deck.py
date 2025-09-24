import random
from constants import Suit, Rank
from models.card import Card


class Deck:
    def __init__(self):
        self.cards = self.__full_card()

    def __full_card(self):
        return [Card(s, r) for s in Suit for r in Rank]  # type: ignore

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        if n > 1:
            return tuple(drawn)
        else:
            return drawn[0]

    def is_empty(self):
        return len(self.cards) == 0
