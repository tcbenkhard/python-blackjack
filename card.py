from enum import Enum


class Suit(Enum):
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    DIAMONDS = 'Diamonds'
    HEARTS = 'Hearts'


class Rank(Enum):
    TWO = 'Two'
    THREE = 'Three'
    FOUR = 'Four'
    FIVE = 'Five'
    SIX = 'Six'
    SEVEN = 'Seven'
    EIGHT = 'Eight'
    NINE = 'Nine'
    TEN = 'Ten'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'
    ACE = 'Ace'


class Card:
    CARD_VALUES = {
        Rank.TWO: 2,
        Rank.THREE: 3,
        Rank.FOUR: 4,
        Rank.FIVE: 5,
        Rank.SIX: 6,
        Rank.SEVEN: 7,
        Rank.EIGHT: 8,
        Rank.NINE: 9,
        Rank.TEN: 10,
        Rank.JACK: 10,
        Rank.QUEEN: 10,
        Rank.KING: 10,
        Rank.ACE: 10,
    }

    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        return self.CARD_VALUES[self.rank]

    def __str__(self):
        return f'{self.rank.value} of {self.suit.value}'
