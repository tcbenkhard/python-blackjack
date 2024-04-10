import random

from card import Suit, Rank, Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Suit:
            for rank in Rank:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.deck)

    def take(self):
        return self.deck.pop()