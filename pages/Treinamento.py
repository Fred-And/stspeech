import streamlit as st
import speech_recognition as sr
import pyaudio
import requests
import random
import json
from funcs.web_funcs import boot_activate, center_logo, dyn_back, speech_rec


###ACTIVATE BOOTSTRAP###
boot_activate()

###LOGO CENTER FUNC###
center_logo()

###DYNAMIC BACKGROUND###
dyn_back()


### REQUEST DE EXERCÍCIOS

## REQUEST ALTITUDE ##
def exe_alt(level,sub):
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com'
    altitude = requests.get(f'{api}/teoria/{level}/{sub}/.json')
    altitude_decode = altitude.json()
    altitude_list = list(altitude_decode)
    altitude_len = len(altitude_decode)
    rand = random.randint(0,altitude_len-1)
    chosen = altitude_list[rand]
    exercise = requests.get(f'{api}/teoria/{level}/{sub}/{chosen}/.json')
    exercise_decode = exercise.json()
    return exercise_decode

## REQUEST DISTANCIAS ##
def exe_dist(level,sub):
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com'
    distance = requests.get(f'{api}/teoria/{level}/{sub}/.json')
    distance_decode = distance.json()
    distance_list = list(distance_decode)
    distance_len = len(distance_decode)
    rand = random.randint(0,distance_len-1)
    chosen = distance_list[rand]
    exercise = requests.get(f'{api}/teoria/{level}/{sub}/{chosen}/.json')
    exercise_decode = exercise.json()
    return exercise_decode

## REQUEST FREQUENCIAS ##
def exe_freq(level,sub):
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com'
    frequency = requests.get(f'{api}/teoria/{level}/{sub}/.json')
    frequency_decode = frequency.json()
    frequency_list = list(frequency_decode)
    frequency_len = len(frequency_decode)
    rand = random.randint(0,frequency_len-1)
    chosen = frequency_list[rand]
    exercise = requests.get(f'{api}/teoria/{level}/{sub}/{chosen}/.json')
    exercise_decode = exercise.json()
    return exercise_decode

## REQUEST PROA ##
def exe_heading(level,sub):
    api = 'https://questoesfraseologia-default-rtdb.firebaseio.com'
    heading = requests.get(f'{api}/teoria/{level}/{sub}/.json')
    heading_decode = heading.json()
    heading_list = list(heading_decode)
    heading_len = len(heading_decode)
    rand = random.randint(0,heading_len-1)
    chosen = heading_list[rand]
    exercise = requests.get(f'{api}/teoria/{level}/{sub}/{chosen}/.json')
    exercise_decode = exercise.json()
    return exercise_decode



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

    ex_alt = exe_alt('nivel1','altitudes')

    if "alt_state" not in st.session_state:
        st.session_state.alt_state = ex_alt

    def rerun():
        st.session_state.alt_state = exe_alt('nivel1','altitudes')


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
            text = rec.recognize_google(audio, language="pt-BR")
            print(text)
            print(st.session_state.alt_state['benchmark'])
            if text == st.session_state.alt_state['benchmark']:
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
def distances():


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

    ex_dist = exe_dist('nivel1','distancias')

    if "dist_state" not in st.session_state:
        st.session_state.dist_state = ex_dist

    def rerun():
        st.session_state.dist_state = exe_dist('nivel1','distancias')

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

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            text = rec.recognize_google(audio, language="pt-BR")
            print(text)
            print(st.session_state.dist_state['benchmark'])
            if text == st.session_state.dist_state['benchmark']:
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
def frequencies():


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

    ex_freq = exe_freq('nivel1','frequencias')

    if "freq_state" not in st.session_state:
        st.session_state.freq_state = ex_freq

    def rerun():
        st.session_state.freq_state = exe_freq('nivel1','frequencias')


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

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            text = rec.recognize_google(audio, language="pt-BR")
            print(text)
            print(st.session_state.freq_state['benchmark'])
            if text == st.session_state.freq_state['benchmark']:
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
def headings():


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

    ex_heading = exe_heading('nivel1','proas')

    if "proa_state" not in st.session_state:
        st.session_state.proa_state = ex_heading

    def rerun():
        st.session_state.proa_state = exe_heading('nivel1','proas')


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

    ### BOTÃO GRAVAR ###

    if st.button("Gravar"):
        rec = sr.Recognizer()
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            #st.write('gravando...')
            audio = rec.listen(mic)
            text = rec.recognize_google(audio, language="pt-BR")
            print(text)
            print(st.session_state.proa_state['benchmark'])
            if text == st.session_state.proa_state['benchmark']:
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
    "Distâncias": distances,
    "Frequências": frequencies,
    "Proas": headings,
}

selected_page = st.sidebar.selectbox("Selecione o tipo de exercício:", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
