from email.mime import image
import shutil
import requests
import time
import os
import json
import csv
import errno

#Diccionario para el contador de las palabras 
Contador_Palabras = {}
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
        os.mkdir(f'Personajes/{personaje}')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    #Ahora vamos a guardar cada imagen en su carpeta
    url = imagen
    nombre_imagen = "Lisa_Level/" + personaje + "/" + personaje + ".png"
    r = requests.get(imagen, STREAM=True)
    with open (nombre_imagen, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw,f)
    #Ahora quitamos los simbolos de las frases, y realizamos el conteo creando un archivo.txt
    simbolos = ["¿","?","¡","!",",",".",":",";"]
    for caracter in simbolos:
        frase2 = frase.replace(caracter,'')
    frase_sin_signos = frase2.split()
    for w in frase_sin_signos :
        if w in Contador_Palabras:
            palabra = Contador_Palabras [w]
            Contador_Palabras [w] = palabra + 1
        else:
            Contador_Palabras [w] = 1
    with open ('Cuenta_Palabras.txt', 'w', newline='') as archivo:
        for clave, valor in Contador_Palabras.items():
            archivo.write(f'\n{clave}: {valor}')
    #Por último, generamos los csv en la carpeta personaje para guardar las frase de cada personaje
    data = {"quote":frase,"character":personaje}
    nombre_csv = "Lisa_Leve/l" + personaje + "/" + personaje + ".csv"
    with open (nombre_csv, 'a', newline ='') as f
        a=csv.DictWriter (f,data.keys())
        a.writerow(data)
        

   