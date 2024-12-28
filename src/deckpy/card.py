from enum import Enum


class Suit(Enum):
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"
    SPADES = "spades"


class ValueMeta(type):
    def __iter__(cls):
        for i in [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]:
            yield Value(i)


class Value(metaclass=ValueMeta):
    def __init__(self, value: str):
        self._value = value

    @property
    def value(self):
        return (
            {str(i): i for i in range(2, 11)}[self._value]
            if self._value.isdigit()
            else {"J": 11, "Q": 12, "K": 13, "A": 14}[self._value]
        )

    def __lt__(self, other):
        if isinstance(other, Value):
            return self.value < other.value
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Value):
            return self.value == other.value
        return NotImplemented

    def __repr__(self):
        return f"Value({self._value})"


class Card:

    def __init__(self, suit: Suit, value: Value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"Card('{self.value._value} of {self.suit.name}')"

    def __lt__(self, card):
        assert self.suit == card.suit, "Cards must be of the same suit"
        return self.value < card.value

    def __eq__(self, card):
        return self.suit == card.suit and self.value == card.value
