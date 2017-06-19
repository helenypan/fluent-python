import collections
from random import choice


Card = collections.namedtuple('Card', ['rank','suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    # FrenchDeck.ranks.index(val): get the index of val in the list (FrenchDeck.ranks)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
# print(choice(deck))

# pick just the aces by starting on index 12 and skpping 13 cards at a time
# print(deck[12::13],"\n")
#
# for d in reversed(deck):
#     print(d)
#
# for d in deck:
#     print(d)

# "in" works with FrenchDeck class because it is iterable
# print(Card("Q",'hearts') in deck)

# sorted (iterable[, cmp[, key[, reverse]]])
# key: Optional. A function of one argument that is used to extract a comparison key from each list element.
# The default value is None (compare the elements directly).
for card in sorted(deck, key=spades_high):
    print(card)

for card in deck:
    print(card, spades_high(card))