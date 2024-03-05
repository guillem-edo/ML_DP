# Calcular el Indice de Masa corporal.

import pandas as pd

peso = float(input("Introduce tu peso en kilogramos.\n Puedes ponerlo con decimales: "))
altura = float(input("Introduce tu altura\n Puedes añadir centimetros: "))

IMC = float(peso / altura **2)
print(f"Tu IMC es: {IMC}")

while not isinstance (peso,(int,float)):
    print("Tu peso está mal puesto,\n Porfavor, estate atento y pon numeros...")
    peso = float(input("Introduce nuevamente tu peso: "))

while not isinstance (altura,(int,float)):
    print("Tu altura está mal puesta.\n Por favor, introduce un número válido:")
    altura = float(input("Introduce otra vez tu altura\n Puedes añadir centimetros\n Ejemplo -- 1.80\n: "))