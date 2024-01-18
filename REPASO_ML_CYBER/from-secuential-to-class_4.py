import os, sys

class game():

    def __init__(self):
        # vidas
        self.vid = 10
        # Definir palabra a encontrar
        self.palabra = "Hola mundo"

    # Jugador input
    def new_player_choice(self):
        return input("Player choice: ")

    def validate_user_choice(self, player_choice):
        if self.palabra.find(player_choice) != -1:
            print(f"letra correcta: {player_choice}")
        else:
            self.vid = self.vid -1
            print(f"Te has equivocado, te quedan {self.vid} vidas")

    def run_game(self):
        # Comprobar
        while self.vid != 0:
            player_choice = self.new_player_choice()
            self.validate_user_choice(player_choice)

# RUN GAME
game_manager = game()
game_manager.run_game()