import os
import pyaudio
import random as rd
import speech_recognition as sr
import streamlit as st
from ast import Return
from numpy import append
import pandas as pd

enunciados = {
    'matricula':['PT-YNC','PT-GBK','PR-ACP','PS-FFE','PP-FNE','PS-WBC','PP-XMC','PT-FAA','PT-NYC','PR-RMA'],
    'aeros':['Bacacheri','Congonhas','Confins','Guarulhos','Curitiba','Belém','Brasília','Galeão','Santos Dumont','Porto Alegre'],
    'icao':['SBBI','SBSP','SBCF','SBGR','SBCT','SBBE','SBBR','SBGL','SBRJ','SBPA']}

df = pd.DataFrame(enunciados)

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
        with open('text.txt', 'w') as f:
            f.write(texto)
    return


###IMPORTS A RANDOM AUDIO FROM AUDIOS FOLDER###
def importaudio():
    audiopath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/audios'
    audio = rd.choice(os.listdir(audiopath))
    return str(audio)


### YELLOW CARDS ###
def card1(titulo,subtitulo,texto,ani):
    return f"""
    {ani}
    <body>
        <div class="card border-0" style="height: 14rem;">
            <div class="card-body bg-warning">
                <h5 class="card-title text-dark"><b>{titulo}</b></h5>
                <p></p>
                <p></p>
                <p class="card-text text-dark">{texto}</p>
            </div>
        </div>
    </body>
    """


### DARK CARDS ###
def card2(titulo,subtitulo,texto,ani):
    return f"""
    {ani}
    <div class="card border-0" style="height: 14rem;">
        <div class="card-body bg-dark">
            <h5 class="card-title text-warning"><b>{titulo}</b></h5>
            <p></p>
            <p></p>
            <p class="card-text text-warning">{texto}</p>
        </div>
    </div>
    """


###ACTIVATE BOOTSTRAP###
def bootactivate():
    return st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
""",unsafe_allow_html=True)


### CENTERED LOGO ###
def centerlogo():
    col1, col2, col3 = st.columns(3)

    ###HEADER WITH LOGO
    with col1:
        st.write(' ')

    with col2:
        st.image('img/logo.png')

    with col3:
        st.write(' ')
    return


### Dynamic Background ###
def dynback():
    return st.markdown(
    """
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <style>
        body {
            margin: 0;
            height: 100vh;
            font-weight: 100;
            background: radial-gradient(#a23982,#1f1013);
            overflow-y: hidden;
            -webkit-animation: fadeIn 1 1s ease-out;
            -moz-animation: fadeIn 1 1s ease-out;
            -o-animation: fadeIn 1 1s ease-out;
            animation: fadeIn 1 1s ease-out;
        }


        .light {
            position: absolute;
            width: 0px;
            opacity: .75;
            background-color: white;
            box-shadow: #FFC107 0px 0px 20px 2px;
            opacity: 0;
            top: 100vh;
            bottom: 0px;
            left: 0px;
            right: 0px;
            margin: auto;
        }

        .x1{
            -webkit-animation: floatUp 4s infinite linear;
            -moz-animation: floatUp 4s infinite linear;
            -o-animation: floatUp 4s infinite linear;
            animation: floatUp 4s infinite linear;
            -webkit-transform: scale(1.0);
            -moz-transform: scale(1.0);
            -o-transform: scale(1.0);
            transform: scale(1.0);
        }

        .x2{
            -webkit-animation: floatUp 7s infinite linear;
            -moz-animation: floatUp 7s infinite linear;
            -o-animation: floatUp 7s infinite linear;
            animation: floatUp 7s infinite linear;
            -webkit-transform: scale(1.6);
            -moz-transform: scale(1.6);
            -o-transform: scale(1.6);
            transform: scale(1.6);
            left: 15%;
        }

        .x3{
            -webkit-animation: floatUp 2.5s infinite linear;
            -moz-animation: floatUp 2.5s infinite linear;
            -o-animation: floatUp 2.5s infinite linear;
            animation: floatUp 2.5s infinite linear;
            -webkit-transform: scale(.5);
            -moz-transform: scale(.5);
            -o-transform: scale(.5);
            transform: scale(.5);
            left: -15%;
        }

        .x4{
            -webkit-animation: floatUp 4.5s infinite linear;
            -moz-animation: floatUp 4.5s infinite linear;
            -o-animation: floatUp 4.5s infinite linear;
            animation: floatUp 4.5s infinite linear;
            -webkit-transform: scale(1.2);
            -moz-transform: scale(1.2);
            -o-transform: scale(1.2);
            transform: scale(1.2);
            left: -34%;
        }

        .x5{
            -webkit-animation: floatUp 8s infinite linear;
            -moz-animation: floatUp 8s infinite linear;
            -o-animation: floatUp 8s infinite linear;
            animation: floatUp 8s infinite linear;
            -webkit-transform: scale(2.2);
            -moz-transform: scale(2.2);
            -o-transform: scale(2.2);
            transform: scale(2.2);
            left: -57%;
        }

        .x6{
            -webkit-animation: floatUp 3s infinite linear;
            -moz-animation: floatUp 3s infinite linear;
            -o-animation: floatUp 3s infinite linear;
            animation: floatUp 3s infinite linear;
            -webkit-transform: scale(.8);
            -moz-transform: scale(.8);
            -o-transform: scale(.8);
            transform: scale(.8);
            left: -81%;
        }

        .x7{
            -webkit-animation: floatUp 5.3s infinite linear;
            -moz-animation: floatUp 5.3s infinite linear;
            -o-animation: floatUp 5.3s infinite linear;
            animation: floatUp 5.3s infinite linear;
            -webkit-transform: scale(3.2);
            -moz-transform: scale(3.2);
            -o-transform: scale(3.2);
            transform: scale(3.2);
            left: 37%;
        }

        .x8{
            -webkit-animation: floatUp 4.7s infinite linear;
            -moz-animation: floatUp 4.7s infinite linear;
            -o-animation: floatUp 4.7s infinite linear;
            animation: floatUp 4.7s infinite linear;
            -webkit-transform: scale(1.7);
            -moz-transform: scale(1.7);
            -o-transform: scale(1.7);
            transform: scale(1.7);
            left: 62%;
        }

        .x9{
            -webkit-animation: floatUp 4.1s infinite linear;
            -moz-animation: floatUp 4.1s infinite linear;
            -o-animation: floatUp 4.1s infinite linear;
            animation: floatUp 4.1s infinite linear;
            -webkit-transform: scale(0.9);
            -moz-transform: scale(0.9);
            -o-transform: scale(0.9);
            transform: scale(0.9);
            left: 85%;
        }

        @-webkit-keyframes floatUp{
            0%{top: 100vh; opacity: 0;}
            25%{opacity: 1;}
            50%{top: 0vh; opacity: .8;}
            75%{opacity: 1;}
            100%{top: -100vh; opacity: 0;}
        }
        @-moz-keyframes floatUp{
            0%{top: 100vh; opacity: 0;}
            25%{opacity: 1;}
            50%{top: 0vh; opacity: .8;}
            75%{opacity: 1;}
            100%{top: -100vh; opacity: 0;}
        }
        @-o-keyframes floatUp{
            0%{top: 100vh; opacity: 0;}
            25%{opacity: 1;}
            50%{top: 0vh; opacity: .8;}
            75%{opacity: 1;}
            100%{top: -100vh; opacity: 0;}
        }
        @keyframes floatUp{
            0%{top: 100vh; opacity: 0;}
            25%{opacity: 1;}
            50%{top: 0vh; opacity: .8;}
            75%{opacity: 1;}
            100%{top: -100vh; opacity: 0;}
        }

    </style>
    <body>
            <div class='light x1'></div>
            <div class='light x2'></div>
            <div class='light x3'></div>
            <div class='light x4'></div>
            <div class='light x5'></div>
            <div class='light x6'></div>
            <div class='light x7'></div>
            <div class='light x8'></div>
            <div class='light x9'></div>
    </body>
    </html>

    """,
    unsafe_allow_html=True)


### AUTORIZAÇÃO PAGE BACKEND ###
def autoriza():
    audiopath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/audios'
    audio = rd.choice(os.listdir(audiopath))
    st.audio(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audios/{audio}')

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            options = [
                'seleções',
                'opções',
                'caixa',
                'sobrecaixas'
                ]
            sb1 = st.selectbox('', options)

        with col2:
            options1 = [
                'aluno',
                'instruendo',
                'pupilo',
                'ser sem luz'
                ]
            sb2 = st.selectbox('', options1)

        with col3:
            options2 = [
                'pior',
                'mais horrivel'
                ,'melhor'
                ]
            sb3 = st.selectbox('', options2)

        with col4:
            options3 = [1,2]
            sb4 = st.selectbox('',options3)

        with col5:
            options4 = [3,4]
            sb5 = st.selectbox('',options4)

    st.markdown(
        f"""<h6>Este é apenas um teste de como colocar
        <b><u>{sb1}</u></b> avulsas no meio do texto para que o
        <b><u>{sb2}</u></b> possa preencher as lacunas da
        <b><u>{sb3}</u></b> maneira possível</h6>""",
        unsafe_allow_html=True)


if __name__ == "__main__":
    print(df)
