from typing import Iterable, Optional

from constants import Rank, Suit
from utils import compare_card, format_hand
from .card import Card


class Hand:
    _count = 0

    def __init__(self, is_human=False, label: Optional[str] = None) -> None:
        self.label = label or f"player{Hand._count}"
        self.is_human = is_human
        self.cards = []

        Hand._count += 1

    def add(self, card: Card):
        self.cards.append(card)

    def reveal(self, choice: int) -> Card:
        return self.cards.pop(choice)

    def choose_revealable_cards(self, leading_card: Optional[Card]):
        if leading_card is None:
            return [(i, card) for i, card in enumerate(self.cards)]
        same_suits = [
            (i, card)
            for i, card in enumerate(self.cards)
            if card.suit == leading_card.suit
        ]
        if len(same_suits) > 0:
            return same_suits
        spade_suite = [
            (i, card) for i, card in enumerate(self.cards) if card.suit == Suit.SPADE
        ]
        if len(spade_suite) > 0:
            return spade_suite
        return [(i, card) for i, card in enumerate(self.cards)]

    def __repr__(self) -> str:
        return format_hand(self.cards)

    def __str__(self) -> str:
        return format_hand(self.cards)


class AIHands(Hand):
    def __init__(self, label: Optional[str] = None) -> None:
        super().__init__(is_human=False, label=label)

    def choose_reveal_card(
        self, leading_card: Card | None, other_cards: Iterable[Card]
    ):
        if leading_card is None:
            min_choice = sorted(self.cards, key=lambda card: card.rank.value)
            card = self._omit_ace_if_possible(min_choice)
            return card

        same_suits = [card for card in self.cards if card.suit == leading_card.suit]
        other_suits = [card for card in self.cards if card.suit != leading_card.suit]

        card = None
        if same_suits:
            card = self._decide(same_suits, leading_card, other_cards)
        elif other_suits:
            card = self._decide(other_suits, leading_card, other_cards)

        if card is None:
            other_choices = sorted(self.cards, key=lambda card: card.rank.value)
            card = self._omit_ace_if_possible(other_choices)
        return self.reveal(self.cards.index(card))

    def _decide(
        self, cards: list[Card], leading_card: Card, other_cards: Iterable[Card]
    ) -> Card | None:
        choices = []
        for card in cards:
            for other_card in other_cards:
                is_higher = compare_card(card, other_card, leading_card)
                if is_higher:
                    choices.append(card)
        if len(choices) > 0:
            choices.sort(key=lambda card: card.rank.value)
            return self._omit_ace_if_possible(choices)
        return None

    def _omit_ace_if_possible(self, sorted_cards: list[Card]):
        if sorted_cards[0].rank == Rank.ACE:
            if len(sorted_cards) > 1:
                return sorted_cards[1]
        return sorted_cards[0]
