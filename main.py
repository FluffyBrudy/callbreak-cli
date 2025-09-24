from typing import Optional
from constants import Rank
from models.card import Card
from models.deck import Deck
from models.hand import AIHands
from models.table import Table
from utils import deal


def get_int_input(message: str):
    while True:
        try:
            choice = int(input(message))
            return choice
        except ValueError:
            print("Enter a valid number.")


class Game:
    def __init__(self) -> None:
        self.table = Table(num_players=2)
        self.deck = Deck()
        self.deck.shuffle()
        deal(self.deck, self.table.players)

        self.subrounds = 0
        self.max_subround = len(Rank)

        self.subround_hands: dict[str, Optional[Card]] = {
            p.label: None for p in self.table.players
        }

    def run_subround(self):
        """Run a single subround (trick)"""
        self.subround_hands = {p.label: None for p in self.table.players}
        leading_card: Optional[Card] = None
        played_cards = []

        for turn, player in enumerate(self.table.players):
            print(f"\nPlayer {turn}'s turn:")
            if isinstance(player, AIHands):
                if leading_card:
                    card = player.choose_reveal_card(leading_card, played_cards)
                else:
                    card = player.choose_reveal_card(player.cards[0], [])
            else:
                print("Your hand:")
                print(player)
                choice = get_int_input("Select card index to play: ")
                card = player.reveal(choice)

            print(f"Player {turn} played: {card}")
            self.subround_hands[player.label] = card
            played_cards.append(card)
            if turn == 0:
                leading_card = card

        self.subrounds += 1
        return self.subround_hands


if __name__ == "__main__":
    game = Game()
    for _ in range(game.max_subround):
        results = game.run_subround()
        print("\nSubround results:")
        for player_label, card in results.items():
            print(f"{player_label}: {card}")
