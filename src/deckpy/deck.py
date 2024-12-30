from .card import Card, Suit, Value
from random import shuffle


class Deck:
    # TODO: #1 implement a Hand class that deck inherits from
    def __init__(self, num_decks: int = 1, *, cards: list[Card] = None):
        self.cards = (
            cards
            if cards is not None
            else [Card(suit, value) for suit in Suit for value in Value] * num_decks
        )

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def __setitem__(self, key, value):
        self.cards[key] = value

    def __delitem__(self, key):
        del self.cards[key]

    def __iter__(self):
        return iter(self.cards)

    def __repr__(self):
        return f"Deck({self.cards})"

    def __add__(self, other):
        return Deck(cards=self.cards + other.cards)

    def __iadd__(self, other):
        self.cards += other.cards
        return self

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, num_hands: int, cards_per: int) -> list["Deck"]:
        if num_hands * cards_per > len(self.cards):
            raise ValueError("Not enough cards in deck to deal")

        # killer dealing code right here folks
        hands = [Deck(cards=[]) for _ in range(num_hands)]
        for _ in range(cards_per):
            for hand in hands:
                hand += Deck(cards=[self.cards.pop()])
                # so glad i implemented __iadd__

        return hands

    def draw(self, num_cards: int = 1) -> "Deck":
        return Deck(cards=[self.cards.pop() for _ in range(num_cards)])
