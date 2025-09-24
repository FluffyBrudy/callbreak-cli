from typing import Optional
from constants import Rank
from models.card import Card
from models.deck import Deck
from models.hand import AIHands
from models.table import Table
from utils import deal
import os, time


class Game:
    def __init__(self) -> None:
        self.table = Table(num_players=4)
        self.deck = Deck()
        self.deck.shuffle()
        deal(self.deck, self.table.players)

        self.subrounds = 0
        self.max_subround = len(Rank)

        self.subround_hands: dict[str, Optional[Card]] = {
            p.label: None for p in self.table.players
        }

    def run_subround(self):
        self.subround_hands = {p.label: None for p in self.table.players}
        leading_card: Optional[Card] = None
        played_cards = []

        for turn, player in enumerate(self.table.players):
            print(f"Player {turn}'s turn:")
            if isinstance(player, AIHands):
                print(player)
                card = player.choose_reveal_card(leading_card, played_cards)
            else:
                print("Your hand:")
                print(player.choose_revealable_cards(leading_card))
                while True:
                    try:
                        choice = int(input("select card index to play: "))
                        if not (0 <= choice < len(player.cards)):
                            print("invalid index.")
                            continue

                        if (
                            choice,
                            player.cards[choice],
                        ) not in player.choose_revealable_cards(leading_card):
                            print("that card cannot be revealed, choose another.")
                            continue

                        card = player.reveal(choice)
                        break
                    except ValueError:
                        print("please enter a valid integer.")

            print(f"Player {turn} played: {card}\n")
            self.subround_hands[player.label] = card
            played_cards.append(card)
            if turn == 0:
                leading_card = card
        if input("press to continue") or True:
            if os.system("clear") != 0:
                os.system("cls")
            print("loading...")
            time.sleep(1)
        self.subrounds += 1
        return self.subround_hands


if __name__ == "__main__":
    game = Game()
    for _ in range(game.max_subround):
        results = game.run_subround()
        print("Subround results:")
        for player_label, card in results.items():
            print(f"{player_label}: {card}")
