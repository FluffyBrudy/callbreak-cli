from dataclasses import dataclass
from constants import Suit, Rank


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank


class Deck:
    def __init__(self):
        pass
