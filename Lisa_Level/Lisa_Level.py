import shutil
import requests
import time
import urllib.request
import os
import json

while True:
    time.sleep (30)
    respuesta = requests.get ('https://thesimpsonsquoteapi.glitch.me/quotes')
    respuesta.json()
    frase=respuesta.json()[0]['quote']
    personaje=respuesta.json()[0]['character']
    imagen=respuesta.json()[0]['image']
    frase_personaje = ['frase':frase,'personaje':personaje]
    if not (os.path.exists(personaje)):
        r=urllib.request.urlopen (imagen)
        

