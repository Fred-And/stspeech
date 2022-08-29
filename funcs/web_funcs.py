from cgitb import text
from dataclasses import replace
import os
import os.path
import pyaudio
import random as rd
import speech_recognition as sr
import streamlit as st
import numpy as np
import pandas as pd
import spacy
from io import BytesIO
import streamlit.components.v1 as components


### IMPORTS A RANDOM PIC FROM A THE AD FOLDER ###
def import_pic():
    adpath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/img/ad'
    pic = rd.choice(os.listdir(adpath))
    return str(pic)


### SPEECH RECOGNITION SCRIPT(ALREADY IMPLEMENTED TO STREAMLIT) ###
def new_speech_rec(path):
    rec = sr.Recognizer()

    with sr.AudioFile(path) as source:
        audio_data = rec.record(source)
        text = rec.recognize_google(audio_data,language="pt-BR")
        #os.remove("/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav")
    return text


### IMPORTS A RANDOM AUDIO FROM AUDIOS FOLDER ###
def import_audio():
    audio_path = '/Users/fred/Documents/Repos/Streamlit/fraseologia/audios'
    audio = rd.choice(os.listdir(audio_path))
    return str(audio)


### YELLOW CARDS ###
def card_1(title,subtitle,text,ani):
    return f"""
    {ani}
    <body>
        <div class="card border-0" style="height: 180px;">
            <div class="card-body bg-warning">
                <h5 class="card-title text-dark"><b>{title}</b></h5>
                <p class="card-text text-dark">{text}</p>
            </div>
        </div>
    </body>
    """


### DARK CARDS ###
def card_2(title,subtitle,text,ani):
    return f"""
    {ani}
    <body>
        <div class="card border-0" style="height: 180px;">
            <div class="card-body bg-dark">
                <h5 class="card-title text-warning"><b>{title}</b></h5>
                <p class="card-text text-warning">{text}</p>
            </div>
        </div>
    </body>
    """


### ACTIVATE BOOTSTRAP ###
def boot_activate():
    return st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
""",unsafe_allow_html=True)


### CENTERED LOGO ###
def center_logo():
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
def dyn_back():
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

### STRING COMPARISON ###
def string_comparison(speech,benchmark):
    nlp = spacy.load("pt_core_news_lg")

    t1 = speech
    t2 = benchmark

    t1 = nlp(t1)
    t2 = nlp(t2)

    similarity = t1.similarity(t2)

    return similarity


def audiorec_demo_app(func , type):

    if type == 1:
        type = st.session_state.alt_state['benchmark']
    elif type == 2:
        type = st.session_state.dist_state['benchmark']
    elif type == 3:
        type = st.session_state.freq_state['benchmark']
    else:
        type = st.session_state.head_state['benchmark']

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    # Custom REACT-based component for recording client audio in browser
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    # specify directory and initialize st_audiorec object functionality
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)

    # STREAMLIT AUDIO RECORDER Instance
    val = st_audiorec()
    #print(val)
    if isinstance(val, dict):
        with st.spinner('carregando...'):
            ind, val = zip(*val['arr'].items())
            ind = np.array(ind, dtype=int)  # convert to np array
            val = np.array(val)             # convert to np array
            sorted_ints = val[ind]
            stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
            #wav_bytes = stream.read()
            text = new_speech_rec(stream)
            similarity = string_comparison(text,type)
            st.text(f"O Correto: {type}")
            st.text(f"O que foi dito: {text}")
            st.text(f"O grau de similaridade: {similarity}")

            if similarity >= 0.8:
                st.text("Resposta certa!!")

            else:
                st.text("Resposta errada :(")

            func()






# def audiorec_demo_app(func):

#     if os.path.exists("/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav"):
#         os.remove("/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav")


#     parent_dir = os.path.dirname(os.path.abspath(__file__))
#     # Custom REACT-based component for recording client audio in browser
#     build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
#     # specify directory and initialize st_audiorec object functionality
#     st_audiorec = components.declare_component("st_audiorec", path=build_dir)

#     # STREAMLIT AUDIO RECORDER Instance
#     val = st_audiorec()

#     if isinstance(val, dict):  # retrieve audio data
#         with st.spinner('carregando...'):
#             ind, val = zip(*val['arr'].items())
#             ind = np.array(ind, dtype=int)  # convert to np array
#             val = np.array(val)             # convert to np array
#             sorted_ints = val[ind]
#             stream = BytesIO(b"".join([int(v).to_bytes(1, "big") for v in sorted_ints]))
#             wav_bytes = stream.read()
#             with open('/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav', mode='bx') as f:
#                 f.write(wav_bytes)


#     with st.spinner("carregando..."):
#         path = "/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav"
#         text = new_speech_rec(path)
#         similarity = string_comparison(text,st.session_state.alt_state['benchmark'])
#         print(f"O Correto: {st.session_state.alt_state['benchmark']}")
#         print(f"O que foi dito: {text}")
#         print(f"O grau de similaridade: {similarity}")
#         if similarity >= 0.8:
#             st.text("Resposta certa!!")

#         else:
#             st.text("Resposta errada :(")

#         func()

if __name__ == "__main__":
    print("Hello World")
