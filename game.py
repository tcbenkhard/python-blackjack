from enum import Enum
from typing import List, Optional

from card import Card
from deck import Deck


class Result(Enum):
    BROKE = "BROKE"
    WIN = 'WIN'
    LOSS = 'LOSS'
    TIE = 'TIE'
    BLACKJACK_TIE = 'BLACKJACK TIE'
    BLACKJACK_WIN = 'BLACKJACK'


class Player:
    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def take_card(self, card: Card):
        self.hand.append(card)

    def get_score(self):
        return sum([card.get_value() for card in self.hand])

    def get_cards(self):
        return [str(card) for card in self.hand]


class PlayerBrokenException(Exception):
    def __init__(self, player: Player):
        super().__init__(f"Player {player.name} broken ({player.get_score()})!")


class GameFinishedException(Exception):
    pass


class Game:
    def __init__(self, players: List[Player]):
        self.players = players
        self.deck = Deck()
        self.deck.shuffle()
        self.current_player_index = 0
        self.dealer = Player("Dealer")
        self.dealer.take_card(self.deck.take())
        for player in self.players:
            player.take_card(self.deck.take())

    def get_current_player(self):
        return self.players[self.current_player_index]

    def deal_card(self):
        card = self.deck.take()
        self.get_current_player().take_card(card)
        if self.get_current_player().get_score() > 21:
            raise PlayerBrokenException(self.get_current_player())

    def next_player(self):
        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            raise GameFinishedException()

    def has_next_player(self):
        return self.current_player_index < len(self.players) - 1

    def dealer_should_take(self):
        return self.dealer.get_score() < 17

    def get_dealer_status(self) -> Optional[Result]:
        if self.dealer.get_score() > 21:
            return Result.BROKE
        if self.dealer.get_score() == 21:
            return Result.BLACKJACK_WIN
        return None

    def get_player_result(self, player: Player) -> Result:
        if player.get_score() > 21:
            return Result.BROKE
        elif self.dealer.get_score() > 21:
            if player.get_score() == 21:
                return Result.BLACKJACK_WIN
            return Result.WIN
        else:
            if player.get_score() == 21:
                if self.dealer.get_score() == 21:
                    return Result.BLACKJACK_TIE
                else:
                    return Result.BLACKJACK_WIN
            else:
                if player.get_score() > self.dealer.get_score():
                    return Result.WIN
                elif player.get_score() == self.dealer.get_score():
                    return Result.TIE
                else:
                    return Result.LOSS
