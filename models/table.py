from random import shuffle
from typing import Any, Callable

from .hand import Hand, AIHands


class Table:
    def __init__(self, num_players: int) -> None:
        human = Hand(is_human=True, label="human")
        self.players = [AIHands() for _ in range(num_players - 1)] + [human]
        self._turn = 0
        self._played = [False] * num_players
        shuffle(self.players)
