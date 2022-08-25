# IMPORTS #
import streamlit as st
import requests
import random
import os
import json
from funcs.web_funcs import boot_activate, center_logo, dyn_back,speech_rec, new_speech_rec, string_comparison, audiorec_demo_app


# ACTIVATE BOOTSTRAP #
boot_activate()

# LOGO CENTER FUNCTION #
center_logo()

# DYNAMIC BACKGROUND #
dyn_back()


# EXERCISE API REQUEST #

## REQUEST ALTITUDE EXERCISES ##
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

## REQUEST DISTANCES EXERCISES ##
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

## REQUEST FRQUENCIES EXERCISES ##
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

## REQUEST HEADING EXERCISES ##
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



#------------------------------------- SUBPAGES -------------------------------------#

## Each function down below represents a subpage that can be selected in the sidebar selector ##

### ALTITUDES SUBPAGE
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


    ### EXERCISE REQUEST ###

    ex_alt = exe_alt('nivel1','altitudes')

    if "alt_state" not in st.session_state:
        st.session_state.alt_state = ex_alt

    def rerun():
        st.session_state.alt_state = exe_alt('nivel1','altitudes')
        #os.remove("/Users/fred/Documents/Repos/Streamlit/fraseologia/wav_test.wav")


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

    ### RECORDING BUTTON ##
    audiorec_demo_app(rerun)

    ### INSTRUÇÕES ###
    st.sidebar.markdown("""Para realizar esse exercício,
     você deve observar a altitude apresentada na caixa e
     a partir disso, clicar no botão "Gravar" e falar
     a altitude de forma correta conforme previsto nos regulamentos.
     Após sua fala, um feedback com a correção irá aprecer.""")
    st.markdown("")



### DISTANCE SUBPAGE
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

    ### RECORDING BUTTON ###

    if st.button("Gravar"):
        text = speech_rec()
        print(text)
        print(st.session_state.alt_state['benchmark'])
        similarity = string_comparison(text,st.session_state.alt_state['benchmark'])
        print(similarity)

        if similarity >= 0.8:
            st.text("Resposta certa!!")

        else:
            st.text("Resposta errada :(")

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



### FREQUENCIES SUBPAGE
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

    ### RECORDING BUTTON ###

    if st.button("Gravar"):
        text = speech_rec()
        print(text)
        print(st.session_state.alt_state['benchmark'])
        similarity = string_comparison(text,st.session_state.alt_state['benchmark'])
        print(similarity)

        if similarity >= 0.8:
            st.text("Resposta certa!!")

        else:
            st.text("Resposta errada :(")

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



### HEADINGS SUBPAGE
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

    ### RECORDING BUTTON ###

    if st.button("Gravar"):
        text = speech_rec()
        print(text)
        print(st.session_state.alt_state['benchmark'])
        similarity = string_comparison(text,st.session_state.alt_state['benchmark'])
        print(similarity)

        if similarity >= 0.8:
            st.text("Resposta certa!!")

        else:
            st.text("Resposta errada :(")

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

#------------------------------------- THE END OF SUBPAGES -------------------------------------#

## PAGE INDEX + SIDEBAR

### INDEX
page_names_to_funcs = {
    "Altitudes": altitudes,
    "Distâncias": distances,
    "Frequências": frequencies,
    "Proas": headings,
}

### SIDEBAR

selected_page = st.sidebar.selectbox("Selecione o tipo de exercício:", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
