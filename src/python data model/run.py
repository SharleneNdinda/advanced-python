from card_deck import FrenchDeck
from card_deck import spades_high
from vector import Vector


# create card deck
deck = FrenchDeck()
print(len(deck))  # 52
print(deck[0])  # Card(rank='2', suit='spades,')

# list cards in rank
for card in sorted(deck, key=spades_high):
    print(card)

# Vector calls
v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)
print(abs(v1))
