import streamlit as st
import speech_recognition as sr
import pyaudio
import requests
import random
import json
from funcs.webfuncs import bootactivate, centerlogo, dynback, srg


###ACTIVATE BOOTSTRAP###
bootactivate()

###LOGO CENTER FUNC###
centerlogo()

###DYNAMIC BACKGROUND###
dynback()


### REQUEST DE EXERCÍCIOS

## REQUEST ALTITUDE ##
def exealt(nivel,assunto):
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

## REQUEST DISTANCIAS ##
def exedist(nivel,assunto):
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

## REQUEST FREQUENCIAS ##
def exefreq(nivel,assunto):
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

## REQUEST PROA ##
def exeproa(nivel,assunto):
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
####------------------------------------- SUBPÁGINAS -------------------------------------####

### SUBPÁGINA DE ALTITUDES
def altitudes():


    ### PAGE TITLE
    st.markdown(
        """
        <html>
        <head>
        <style>
            h1{text-align: center; transition: color 1s;}
            h1:hover{color: #FFC107;}
            h2{text-align: center; text-decoration-color: #FF0C107;}
        </style>
        </head>
        <body>
            <h1><b>Altitudes!</b></h1>
        </body>
        """, unsafe_allow_html=True)


    ### REQUEST DE EXERCÍCIO ###

    exalt = exealt('nivel1','altitudes')

    if "alt_state" not in st.session_state:
        st.session_state.alt_state = exalt

    def rerun():
        st.session_state.alt_state = exealt('nivel1','altitudes')


    ### CONTAINER DO ENUNCIADO ###
    # if "load_state" not in st.session_state:
    #     st.session_state.load_state = False
    #
    # if st.button("Gerar exercício") or st.session_state.load_state:
    #     st.session_state.load_state = True
    #     gerarquestao()

    st.markdown(
    """
    <html>
    <head>
    <style>
        .four{
        color: #333333;
        border-radius: 25px;
        background: #ffc107;
        width: 400px;
        height: 125px;
        padding: 0px;
        text-align: center;
        font-size: 80px;
        margin: auto;
        }
    </style>
    </head>
    <body>
        <p class="four">
            <b>%s</b>
        </p>
    </body>
    </html>
    """%st.session_state.alt_state['enunciado'],unsafe_allow_html=True
    )

    ### BLANK SPACE ###
    st.text("")

    st.text("")

    #st.session_state.load_state['benchmark']

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(texto)
            print(st.session_state.alt_state['benchmark'])
            if texto == st.session_state.alt_state['benchmark']:
                st.text('Resposta certa!!!')
            else:
                st.text('Resposta errada :(')

            st.button('Próxima!', on_click = rerun())


    else:
        st.markdown(
        """
        <html>
        <head>
        <style>
            .tree{
                font-size:20px;
            }
        </style>
        </head>
        <body>
            <p class="tree"> <b>Pressione o botao para gravar </p>
        </body>
        </html>
        """,unsafe_allow_html=True)


    ### INSTRUÇÕES ###
    st.sidebar.markdown("""Para realizar esse exercício,
     você deve observar a altitude apresentada na caixa e
     a partir disso, clicar no botão "Gravar" e falar
     a altitude de forma correta conforme previsto nos regulamentos.
     Após sua fala, um feedback com a correção irá aprecer.""")
    st.markdown("")



### SUBPÁGINA DE DISTANCIAS
def distancias():


    ### PAGE TITLE
    st.markdown(
        """
        <html>
        <head>
        <style>
            h1{text-align: center; transition: color 1s;}
            h1:hover{color: #FFC107;}
            h2{text-align: center; text-decoration-color: #FF0C107;}
        </style>
        </head>
        <body>
            <h1><b>Distâncias!</b></h1>
        </body>
        """, unsafe_allow_html=True)


    ### REQUEST DE EXERCÍCIO ###

    exdist = exedist('nivel1','distancias')

    if "dist_state" not in st.session_state:
        st.session_state.dist_state = exdist

    def rerun():
        st.session_state.dist_state = exedist('nivel1','distancias')


    ### CONTAINER DO ENUNCIADO ###
    # if "load_state" not in st.session_state:
    #     st.session_state.load_state = False
    #
    # if st.button("Gerar exercício") or st.session_state.load_state:
    #     st.session_state.load_state = True
    #     gerarquestao()

    st.markdown(
    """
    <html>
    <head>
    <style>
        .four{
        color: #333333;
        border-radius: 25px;
        background: #ffc107;
        width: 400px;
        height: 125px;
        padding: 0px;
        text-align: center;
        font-size: 80px;
        margin: auto;
        }
    </style>
    </head>
    <body>
        <p class="four">
            <b>%s</b>
        </p>
    </body>
    </html>
    """%st.session_state.dist_state['enunciado'],unsafe_allow_html=True
    )

    ### BLANK SPACE ###
    st.text("")

    st.text("")

    #st.session_state.load_state['benchmark']

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(texto)
            print(st.session_state.dist_state['benchmark'])
            if texto == st.session_state.dist_state['benchmark']:
                st.text('Resposta certa!!!')
            else:
                st.text('Resposta errada :(')

            st.button('Próxima!', on_click = rerun())


    else:
        st.markdown(
        """
        <html>
        <head>
        <style>
            .tree{
                font-size:20px;
            }
        </style>
        </head>
        <body>
            <p class="tree"> <b>Pressione o botao para gravar </p>
        </body>
        </html>
        """,unsafe_allow_html=True)


    ### INSTRUÇÕES ###
    st.sidebar.markdown("""Para realizar esse exercício,
     você deve observar a altitude apresentada na caixa e
     a partir disso, clicar no botão "Gravar" e falar
     a altitude de forma correta conforme previsto nos regulamentos.
     Após sua fala, um feedback com a correção irá aprecer.""")
    st.markdown("")



### SUBPÁGINA DE FREQUENCIAS
def frequencias():


    ### PAGE TITLE
    st.markdown(
        """
        <html>
        <head>
        <style>
            h1{text-align: center; transition: color 1s;}
            h1:hover{color: #FFC107;}
            h2{text-align: center; text-decoration-color: #FF0C107;}
        </style>
        </head>
        <body>
            <h1><b>Frequências!</b></h1>
        </body>
        """, unsafe_allow_html=True)


    ### REQUEST DE EXERCÍCIO ###

    exfreq = exefreq('nivel1','frequencias')

    if "freq_state" not in st.session_state:
        st.session_state.freq_state = exfreq

    def rerun():
        st.session_state.freq_state = exefreq('nivel1','frequencias')



    ### CONTAINER DO ENUNCIADO ###
    # if "load_state" not in st.session_state:
    #     st.session_state.load_state = False
    #
    # if st.button("Gerar exercício") or st.session_state.load_state:
    #     st.session_state.load_state = True
    #     gerarquestao()

    st.markdown(
    """
    <html>
    <head>
    <style>
        .four{
        color: #333333;
        border-radius: 25px;
        background: #ffc107;
        width: 400px;
        height: 125px;
        padding: 0px;
        text-align: center;
        font-size: 80px;
        margin: auto;
        }
    </style>
    </head>
    <body>
        <p class="four">
            <b>%s</b>
        </p>
    </body>
    </html>
    """%st.session_state.freq_state['enunciado'],unsafe_allow_html=True
    )

    ### BLANK SPACE ###
    st.text("")

    st.text("")

    #st.session_state.load_state['benchmark']

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(texto)
            print(st.session_state.freq_state['benchmark'])
            if texto == st.session_state.freq_state['benchmark']:
                st.text('Resposta certa!!!')
            else:
                st.text('Resposta errada :(')

            st.button('Próxima!', on_click = rerun())


    else:
        st.markdown(
        """
        <html>
        <head>
        <style>
            .tree{
                font-size:20px;
            }
        </style>
        </head>
        <body>
            <p class="tree"> <b>Pressione o botao para gravar </p>
        </body>
        </html>
        """,unsafe_allow_html=True)


    ### INSTRUÇÕES ###
    st.sidebar.markdown("""Para realizar esse exercício,
     você deve observar a altitude apresentada na caixa e
     a partir disso, clicar no botão "Gravar" e falar
     a altitude de forma correta conforme previsto nos regulamentos.
     Após sua fala, um feedback com a correção irá aprecer.""")
    st.markdown("")



### SUBPÁGINA DE PROAS
def proas():


    ### PAGE TITLE
    st.markdown(
        """
        <html>
        <head>
        <style>
            h1{text-align: center; transition: color 1s;}
            h1:hover{color: #FFC107;}
            h2{text-align: center; text-decoration-color: #FF0C107;}
        </style>
        </head>
        <body>
            <h1><b>Proas!</b></h1>
        </body>
        """, unsafe_allow_html=True)


    ### REQUEST DE EXERCÍCIO ###

    exproa = exeproa('nivel1','proas')

    if "proa_state" not in st.session_state:
        st.session_state.proa_state = exproa

    def rerun():
        st.session_state.proa_state = exeproa('nivel1','proas')

    ### CONTAINER DO ENUNCIADO ###
    # if "load_state" not in st.session_state:
    #     st.session_state.load_state = False
    #
    # if st.button("Gerar exercício") or st.session_state.load_state:
    #     st.session_state.load_state = True
    #     gerarquestao()

    st.markdown(
    """
    <html>
    <head>
    <style>
        .four{
        color: #333333;
        border-radius: 25px;
        background: #ffc107;
        width: 400px;
        height: 125px;
        padding: 0px;
        text-align: center;
        font-size: 80px;
        margin: auto;
        }
    </style>
    </head>
    <body>
        <p class="four">
            <b>%s</b>
        </p>
    </body>
    </html>
    """%st.session_state.proa_state['enunciado'],unsafe_allow_html=True
    )

    ### BLANK SPACE ###
    st.text("")

    st.text("")

    #st.session_state.load_state['benchmark']

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            print(texto)
            print(st.session_state.proa_state['benchmark'])
            if texto == st.session_state.proa_state['benchmark']:
                st.text('Resposta certa!!!')
            else:
                st.text('Resposta errada :(')

            st.button('Próxima!', on_click = rerun())


    else:
        st.markdown(
        """
        <html>
        <head>
        <style>
            .tree{
                font-size:20px;
            }
        </style>
        </head>
        <body>
            <p class="tree"> <b>Pressione o botao para gravar </p>
        </body>
        </html>
        """,unsafe_allow_html=True)


    ### INSTRUÇÕES ###
    st.sidebar.markdown("""Para realizar esse exercício,
     você deve observar a altitude apresentada na caixa e
     a partir disso, clicar no botão "Gravar" e falar
     a altitude de forma correta conforme previsto nos regulamentos.
     Após sua fala, um feedback com a correção irá aprecer.""")
    st.markdown("")

####------------------------------------- FIM DAS SUBPÁGINAS -------------------------------------####

### INDEX DE PÁGINAS + FUNÇÃO PARA RODAR
page_names_to_funcs = {
    "Altitudes": altitudes,
    "Distâncias": distancias,
    "Frequências": frequencias,
    "Proas": proas,
}

selected_page = st.sidebar.selectbox("Selecione o tipo de exercício:", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
