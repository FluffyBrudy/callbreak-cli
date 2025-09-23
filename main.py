from constants import Rank
from entity import Deck, Table
from utils import deal


def get_int_input(message: str):
    while True:
        try:
            choice = int(input(message))
            return choice
        except ValueError:
            print("enter number")


def main():
    table = Table(num_players=2)
    deck = Deck()
    deal(deck, table.players)

    subround = 0
    total_subrounds = len(Rank)

    while subround < total_subrounds:
        player = table.current()
        if player.is_human:
            print(player)
            choice = get_int_input("enter choice: ")

        subround += 1


main()
