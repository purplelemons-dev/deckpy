from deckpy import Deck

deck = Deck()
deck.shuffle()
hands = deck.deal(num_hands=2, cards_per=2)

print(hands)
print(len(deck))
