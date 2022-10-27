import shutil
import requests
import time
import os
import json
import csv
import errno

while True:
    time.sleep (30)
    respuesta = requests.get ('https://thesimpsonsquoteapi.glitch.me/quotes')
    respuesta.json()
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]['image']
    frase_personaje = ['frase':frase,'personaje':personaje]
    #Ahora creamos un directorio para cada personaje
    try:
        os.mkdir(f'General/{personaje}')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    #Ahora vamos a guardar cada imagen en su carpeta
    url = imagen
    nombre_Imagen = "Lisa_Level"
    

