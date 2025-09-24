from typing import Any, Callable

from .hand import Hand, AIHands


class Table:
    def __init__(self, num_players: int) -> None:
        human = Hand(is_human=True, label="human")
        self.players = [human] + [AIHands() for _ in range(num_players - 1)]
        self._turn = 0
        self._played = [False] * num_players

    def current(self) -> tuple[int, Hand | AIHands]:
        return (self._turn, self.players[self._turn])

    def advance(self):
        self._turn = (self._turn + 1) % len(self.players)

    def perform_action(self, turn: int, action: Callable[[], Any]):
        assert turn == self._turn
        self._played[turn] = True
        action()
        self.advance()

    def all_hand_revel(self):
        return all(self._played)

    def reset_hand_round(self) -> None:
        self._played = [False] * len(self.players)
