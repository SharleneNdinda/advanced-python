"""The Python interpreter is the only frequent caller of most special methods.

We use special methods to leverage the Python Data Model. This is when we want
our classes to behave like normal Python data objects.
"""

import collections


Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """Get the total number of cards in a deck"""
        return len(self._cards)

    def __getitem__(self, postition):
        """Get the card located at a given position."""
        return self._cards[postition]


# rank cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
