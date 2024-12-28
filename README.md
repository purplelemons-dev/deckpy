# DeckPy

my custom card deck library

## Example

```py
from deckpy import Deck

deck = Deck()
deck.shuffle()
hands = deck.deal(num_hands=2, cards_per=2)

print(hands)
print(len(deck))
```

Output:

```
[Deck([Card('3 of SPADES'), Card('7 of HEARTS')]), Deck([Card('J of DIAMONDS'), Card('2 of DIAMONDS')])]
48
```
