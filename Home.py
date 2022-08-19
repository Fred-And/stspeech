import streamlit as st
from funcs.webfuncs import card1, card2, bootactivate, dynback

###ACTIVATE BOOTSTRAP###
bootactivate()

###DYNAMIC BACKGOUND###
dynback()

###COLUMNS FOR THE LOGO POSITIONING###
col1, col2, col3 = st.columns(3)

###HEADER WITH LOGO

#blank space
with col1:
    st.write(' ')

#LOGO is here#
with col2:
    st.image('img/logo.png')

#Blank space
with col3:
    st.write(' ')

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
        <h1><b>Módulo Prático!</b></h1>
    </body>
    """,unsafe_allow_html=True)

### ABOUT ###
st.markdown(
    '''
    <style>
        .one{text-align: center;}
        .two{
            border-radius: 25px;
            background: #ffc107;
            width: 700px;
            height: 10px;
        }
        .tree{
            text-align: center;
            color: #ffc107 ;
            border-radius: 25px;
            background: #212529;
            width: 700px;
            height: 60px;
        }
    </style>
    <body>
        <p class="one">Bem vindo(a) ao módulo prático de Fraseologia do curso. <br> Aqui você irá encontrar diversas abas, cada uma com uma finalidade de treinamento.</p>
        <p class="two"></p>
        <p class="tree">Em cada uma delas você será instruído a realizar <u>exercícios de fixação</u> <br>para melhorarseu desempenho nas comunicações aeronáuticas.</p>
    </body>''',unsafe_allow_html=True
    )

### 6 BOXES WITH PRODUCT FEATURES ###
col4, col5, col6 = st.columns(3)

### AUTORIZAÇAO E CIRCUITO DE TRÁFEGO CARDS ###
with col4:
    st.markdown(
        card1(
            'Autorização:',
            'Solo',
            'Exercícios para praticar o recebimento de autorizações ATC.',
            """
            <style>
                .card{
                    transition: transform .2s;
                }
                .card:hover{
                    transform: scale(1.1);
                }
            </style>"""
            ),
        unsafe_allow_html=True
        )
    st.text('')
    st.markdown(
        card2(
            'Circuito de tráfego:',
            'Voo',
            'Exercícios para treinar a fraseologia de entrada, saída e evoluções em circuitos de tráfego visual.',
            """
            <style>
                .card{
                    transition: transform .2s;
                }
                .card:hover{
                    transform: scale(1.1);
                }
            </style>"""
            ),
        unsafe_allow_html=True
        )
    st.text("")

### TORRE E SOLO CARDS ###
with col5:
    st.markdown(card2('Solo:','Solo','Exercícios com o objetivo de treinar a fraseologia de movimentações no solo.',""),unsafe_allow_html=True)
    st.text("")
    st.markdown(card1('Torre:','Voo/Solo','Fraseologia básica de TWR com autorizações de pouso, decolagem, condicionais etc.',""),unsafe_allow_html=True)
    st.text("")

### VOO VFR E VOO IFR CARDS###
with col6:
    st.markdown(card1('Voo IFR:','Voo','Fraseologia básica de um voo por instrumentos com situações de SID, STAR e IAP.',""),unsafe_allow_html=True)
    st.text("")
    st.markdown(card2('Voo VFR:','Voo','Fraseologia básica de um voo visual com situações de reporte de posições.',""),unsafe_allow_html=True)
    st.text("")

### PAGE SELECTOR
