import os, sys

# vidas
vid = 10

# Definir palabra a encontrar
palabra = "Hola mundo"

# Jugador input
player_choice = input("Player choice: ")

# Comprobar
if palabra.find(player_choice) != -1:
    print(f"letra correcta: {player_choice}")
else:
    vid = vid -1
    print(f"Te has equivocado, te quedan {vid} vidas")