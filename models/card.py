from dataclasses import dataclass

from constants import Rank, Suit


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{self.suit.name}:{self.rank}"
