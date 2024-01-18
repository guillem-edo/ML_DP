import os, sys

# vidas
vid = 10

# Definir palabra a encontrar
palabra = "Hola mundo"

# Jugador input
def new_player_choice():
    return input("Player choice: ")


# Comprobar
while vid != 0:
    player_choice = new_player_choice()
    
    if palabra.find(player_choice) != -1:
        print(f"letra correcta: {player_choice}")
    else:
        vid = vid -1
        print(f"Te has equivocado, te quedan {vid} vidas")