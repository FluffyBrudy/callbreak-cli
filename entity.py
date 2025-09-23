import random
from typing import Callable, Iterable
from dataclasses import dataclass
from constants import Suit, Rank


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: Rank

    def __str__(self) -> str:
        return f"{self.suit.name}:{self.rank}"


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


class Hand:
    def __init__(self, is_human=False) -> None:
        self.is_human = is_human
        self.cards = []

    def add(self, card: Card):
        self.cards.append(card)

    def reveal(self, choice: int) -> Card:
        return self.cards.pop(choice)

    def __str__(self) -> str:
        return ", ".join(
            [f"({i}) {card.__str__()}" for i, card in enumerate(self.cards)]
        )


class Dealer:
    def __init__(self, deck: Deck, num_players: int = 2) -> None:
        assert 2 <= num_players <= 4
        self.deck = deck
        self.human = Hand(is_human=True)
        self._cards_each = len(Rank)

    def deal(self, players: list[Hand]):
        player = 0
        assert len(self.deck.cards) == self._cards_each * 4
        for _ in range(self._cards_each * len(players)):
            card = self.deck.draw(n=1)
            players[player].add(card)  # type: ignore
            player = (player + 1) % len(players)


class Table:
    def __init__(self, num_players: int) -> None:
        human = Hand(is_human=True)
        self.players = [human] + [Hand() for _ in range(num_players - 1)]
        self._turn = 0
        self._played = [False] * num_players

    def current(self):
        return self.players[self._turn]

    def advance(self):
        self._turn = (self._turn + 1) % len(self.players)

    def perform_action(self, turn: int, action: Callable, *args, **kwargs):
        assert turn == self._turn
        result = action(*args, **kwargs)
        self._played[turn] = True
        self.advance()
        return result

    def all_hand_revel(self):
        return all(self._played)

    def reset_hand_round(self) -> None:
        self._played = [False] * len(self.players)


class AIHands(Hand):
    def __init__(self, is_human=False) -> None:
        super().__init__(is_human)

    def choose_reveal_card(self):
        pass

    def decide(self, other_cards: Iterable[Card]):
        pass
