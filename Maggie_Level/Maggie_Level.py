import requests
import time
import json
from requests.models import Response
import threading
import csv


while True:
  URL: str = "https://thesimpsonsquoteapi.glitch.me/quotes"
  respuesta: Response = requests.get (url = URL)
  datos = respuesta.json ()
  frase:str = datos [0]["quote"]
  personaje:str = datos [0]["character"]
  frase_personaje: list [frase,personaje]
  print (f'La frase de {personaje} es: {frase}')
  time.sleep (30)
    
  #Generar los csv y que se guarden en las carpetas
  data = {"quote":frase, "character":personaje}
  #Carpeta general
  with open ('Maggie_Level/General/General.csv', 'a', newline='') as a:
    a=csv.DictWriter(a,data.keys())
    a.writerow(data)
  #Carpeta Homer
  if personaje == "Homer Simpson":
    with open ('Maggie_Level/Homer/Homer.csv', 'a', newline='') as s:
      a=csv.DictWriter(s,data.keys())
      a.writerow(data)
  #Carpeta Lisa
  elif personaje == "Lisa Simpson":
    with open ('Maggie_Level/Lisa/Lisa.csv', 'a', newline='') as d:
      a=csv.DictWriter(d,data.keys())





