from constants import Precedence, Rank, Suit
from entity import Card, Deck, Hand


def deal(deck: Deck, players: list[Hand]):
    cards_each = len(Rank)

    player_idx = 0
    for _ in range(cards_each * len(players)):
        card = deck.draw()
        players[player_idx].add(card)  # type: ignore
        player_idx = (player_idx + 1) % len(players)


def compare_card(src: Card, target: Card, leading_suit: Card, /):
    """comapres source and return boolean if src has higher precedence"""
    suit_precedence = comapre_suit(src.suit, target.suit, leading_suit.suit)
    if suit_precedence == Precedence.EQUAL:
        return compare_value(src.rank, target.rank)
    if suit_precedence == Precedence.HIGHER:
        return True
    return False


def comapre_suit(src: Suit, target: Suit, leading_suit: Suit) -> Precedence:
    if src.value == target.value:
        return Precedence.EQUAL
    if src.value == "spade":
        return Precedence.HIGHER
    if target.value == "spade":
        return Precedence.LOWER
    if src.value == leading_suit.value:
        return Precedence.HIGHER
    if target.value == leading_suit.value:
        return Precedence.LOWER
    return Precedence.LOWER


def compare_value(src: Rank, dest: Rank):
    return src.value == Rank.ACE.value or src.value > dest.value


if __name__ == "__main__":
    card1 = Card(Suit.DIAMOND, Rank.TWO)
    card2 = Card(Suit.HEART, Rank.ACE)

    print(compare_card(card1, card2, card2))
