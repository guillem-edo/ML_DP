# IMPORTANTE
# Instalar adecuadamente las librerias correspondientes si no están instaladas .

# pip install requests 
# pip install schedule


import requests
import schedule
import time

def obtener_datos(api_url):
    headers = {
        'Authorization': 'Bearer TU_TOKEN_DE_ACCESO',
        'Accept': 'application/json',
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error en la solicitud: {response.status_code}"

def tarea_programada():
    api_url = 'https://api.empresa.com/datos'
    datos = obtener_datos(api_url)
    print(datos)
    # Añadir mas codigo para procesar o almacenar los datos obtenidos

# Programa la tarea para que se ejecute cada minuto
schedule.every(1).minutes.do(tarea_programada)

while True:
    schedule.run_pending()
    time.sleep(1)