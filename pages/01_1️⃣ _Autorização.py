from enum import auto
import streamlit as st
import random as rd
from funcs.webfuncs import importaudio, centerlogo, autoriza, dynback

def main():

    centerlogo()
    dynback()

    ### TITLE ###
    with st.title(""):
        st.markdown("""
        <html>
        <head>
        <style>
            h1{text-align: center; transition: color 1s;}
            h1:hover{color: #FFC107;}
        </style>
        </head>
        <body>
            <h1><b>Autorização</b></h1>
        </body>
        """,unsafe_allow_html=True)

    ### BODY ###
    st.markdown("""
        <html>
        <head>
        </head>
        <style>
            .a{height: 30px;}
            .b{text-align: center;}
        </style>
        <body>
            <p></p>
            <p class="b"><b>Ouça o áudio a seguir, depois responda as questões</b></p>
            <div class="a"></div>
        </body
        </html>
        """,
        unsafe_allow_html=True
    )


    autoriza()




if __name__ == "__main__":
     main()
