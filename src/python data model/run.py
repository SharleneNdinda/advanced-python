from card_deck import FrenchDeck, spades_high

# create card deck
deck = FrenchDeck()
print(len(deck))  # 52
print(deck[0])  # Card(rank='2', suit='spades,')

# list cards in rank
for card in sorted(deck, key=spades_high):
    print(card)
