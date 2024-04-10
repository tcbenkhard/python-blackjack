import copy

import game
from game import Player, Game, PlayerBrokenException


class CliRunner:
    def start(self):
        players = self._get_players()
        games_played = []
        keep_playing = True

        while keep_playing:
            current_game = Game(copy.deepcopy(players))
            all_players_finished = False
            while not all_players_finished:
                try:
                    self._print_current_player(current_game)
                    self._print_player_status(current_game.get_current_player())
                    self._deal_cards(current_game)
                except PlayerBrokenException:
                    print("You are broken!")
                finally:
                    if current_game.has_next_player():
                        current_game.next_player()
                    else:
                        all_players_finished = True

            self._deal_dealer(current_game)
            self._print_results(current_game)

            another_game = input("\nDo you want to play another game? (y/n)")
            keep_playing = another_game == "y"
            games_played.append(current_game)
        print(f"\nYou've played {len(games_played)} game{'s' if len(games_played) > 1 else ''}.")

    def _deal_dealer(self, game):
        print("\nAll players finished, dealing to dealer")
        while game.dealer_should_take():
            game.dealer.take_card(game.deck.take())
            self._print_player_status(game.dealer)

    def _print_results(self, game):
        print("\nResults:")
        self._print_dealer_result(game)
        print()
        self._print_player_results(game)

    def _get_players(self):
        player_name = input("What is your name? ")
        player = Player(player_name)
        players = [player]
        add_additional = input("Do you want to add additional players? (y/n)")
        while add_additional == "y":
            name = input("What is the player's name? ")
            players.append(Player(name))
            add_additional = input("Do you want to add additional players? (y/n)")
        return players

    def _print_player_status(self, player):
        print(f"{player.name} has {player.get_cards()} ({player.get_score()} points).")

    def _print_current_player(self, game):
        print(f"\nCurrent player is {game.get_current_player().name}")

    def _print_dealer_result(self, game):
        print(f"Dealer: {game.dealer.get_score()} points {f"({game.get_dealer_status().value})" if game.get_dealer_status() else ""}")

    def _print_player_result(self, game, player):
        result = game.get_player_result(player)
        print(f"{player.name}: {player.get_score()} points ({result.value})")

    def _print_player_results(self, game):
        for player in game.players:
            self._print_player_result(game, player)

    def _deal_cards(self, game):
        take = input('Do you want another card? (y/n)')
        while take == "y":
            game.deal_card()
            print(
                f'You have {game.get_current_player().get_cards()} ({game.get_current_player().get_score()} points)')
            take = input('Do you want another card? (y/n)')