import json
from certifi import where
import requests
import random

def exercicio(nivel,assunto):
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com'
    altitude = requests.get(f'{api}/teoria/{nivel}/{assunto}/.json')
    altitudeDecode = altitude.json()
    altitudeList = list(altitudeDecode)
    tamanhoAltitude = len(altitudeDecode)
    rand = random.randint(0,tamanhoAltitude-1)
    escolhido = altitudeList[rand]
    exercicio = requests.get(f'{api}/teoria/{nivel}/{assunto}/{escolhido}/.json')
    exercicioDecode = exercicio.json()
    return exercicioDecode

def importmatriculas():
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com/'
    matricula = requests.get(f'{api}/matriculas/.json')
    matriculaDecode = matricula.json()
    return matriculaDecode

def importxponder():
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com/'
    xponder = requests.get(f'{api}/transponder/.json')
    xponderDecode = xponder.json()
    return xponderDecode


print(exercicio('nivel1','altitudes'))
