from enum import Enum
from dataclasses import dataclass

TOTAL_CARDS = 52

class Suit(enum, str):
    SPADE="spade"
    HEART="heart"
    DIAMOND="diamond"
    CLUB="club"

class Rank(enum, int):
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
