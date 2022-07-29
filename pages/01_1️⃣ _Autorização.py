from enum import auto
import streamlit as st
import random as rd
from funcs.webfuncs import importaudio, centerlogo, autoriza

def main():

    centerlogo()

    titulo = st.container()

    ### CENTERED TITLE ###
    with titulo:
        st.markdown("""
        <html>
        <head>
        <style>
            h1{text-align: center;}
        </style>
        </head>
        <body>
            <h1><b>Autorização!</b></h1>
        </body>
        """,unsafe_allow_html=True)
        st.header('Ouça o áudio a seguir e preencha da melhor maneira:',)

    st.text('')
    # audiok = importaudio()
    # st.audio(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audios/{audiok}')

    # with st.container():
    #     col1, col2, col3, col4, col5 = st.columns(5)
    #     with col1:
    #         options = [
    #             'seleções',
    #             'opções',
    #             'caixa',
    #             'sobrecaixas'
    #             ]
    #         sb1 = st.selectbox('', options)

    #     with col2:
    #         options1 = [
    #             'aluno',
    #             'instruendo',
    #             'pupilo',
    #             'ser sem luz'
    #             ]
    #         sb2 = st.selectbox('', options1)

    #     with col3:
    #         options2 = [
    #             'pior',
    #             'mais horrivel'
    #             ,'melhor'
    #             ]
    #         sb3 = st.selectbox('', options2)

    #     with col4:
    #         options3 = [1,2]
    #         sb4 = st.selectbox('',options3)
        
    #     with col5:
    #         options4 = [3,4]
    #         sb5 = st.selectbox('',options4)
    autoriza()

        


if __name__ == "__main__":
     main()

