import os
import pyaudio
import random as rd
import speech_recognition as sr
import streamlit as st
import requests
import random
import json
from ast import Return
from numpy import append



###CREATES AS QUESTION TITLE###
def enunciado():

    aeroporto = [] # AIRPORT
    matricula = [] # TAIL NUMBER
    atc = [] # ATC TO BE CALLED
    posad = [] # WHERE I AM IN THE AD

    def aeros():
        my_file = open("database/aeros.txt", "r")
        data = my_file.read()
        data_into_list = data.split(",")
        #aeroporto = []
        aeroporto.append(data_into_list)
        lenaeroporto = len(aeroporto[0])
        my_file.close()
        return

    def matriculas():
        my_file = open("database/matriculas.txt", "r")
        data = my_file.read()
        data_into_list = data.split(",")
        #matricula = []
        matricula.append(data_into_list)
        lenmatriculas = len(matricula[0])
        my_file.close()
        return

    def atcp():
        my_file = open("database/posicoes.txt", "r")
        data = my_file.read()
        data_into_list = data.split(",")
        #posop = []
        atc.append(data_into_list)
        lenatc = len(atc[0])
        my_file.close()
        return

    def posicao():
        my_file = open("database/posiad.txt", "r")
        data = my_file.read()
        data_into_list = data.split(",")
        posad.append(data_into_list)
        lenposad = len(posad[0])
        my_file.close()
        return

    aeros()
    matriculas()
    atcp()
    posicao()

    lenmatriculas = len(matricula[0])
    lenatc = len(atc[0])
    lenaeroporto = len(aeroporto[0])
    lenposad = len(posad[0])

    ### Elements to be used in execises ###
    enunciado = [
        matricula[0][rd.randrange(lenmatriculas)], #0
        aeroporto[0][rd.randrange(lenaeroporto)],  #1
        atc[0][rd.randrange(lenatc)],              #2
        posad[0][rd.randrange(lenposad)]           #3
        ]
    return enunciado


###IMPORTS A RANDOM PIC FROM A THE AD FOLDER###
def importpic():
    adpath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/img/ad'
    pic = rd.choice(os.listdir(adpath))
    return str(pic)


###SPEECH RECOGNITION SCRIPT(ALREADY IMPLEMENTED TO STREAMLIT)###
def srg():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        st.write('gravando...')
        audio = rec.listen(mic)
        texto = rec.recognize_google(audio, language="pt-BR")
        #print(texto)
        #with open('text.txt', 'w') as f:
            #f.write(texto)
    return texto

###IMPORTS A RANDOM AUDIO FROM AUDIOS FOLDER###
def importaudio():
    audiopath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/audios'
    audio = rd.choice(os.listdir(audiopath))
    return str(audio)


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

if __name__ == "__main__":
    print(234)