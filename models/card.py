from dataclasses import dataclass

from constants import Rank, Suit, Icon


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        suit = self.suit.value.upper()
        rank = self.rank.name.upper()
        icon = suit + "_" + rank
        return Icon[icon].value

    def __repr__(self) -> str:
        suit = self.suit.value.upper()
        rank = self.rank.name.upper()
        icon = suit + "_" + rank
        return Icon[icon].value
