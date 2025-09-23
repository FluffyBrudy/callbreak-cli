from enum import Enum

TOTAL_CARDS = 52


class Suit(str, Enum):
    SPADE = "spade"
    HEART = "heart"
    DIAMOND = "diamond"
    CLUB = "club"


class Rank(int, Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Precedence(Enum):
    HIGHER = 1
    EQUAL = 0
    LOWER = -1
