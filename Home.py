import streamlit as st
from funcs.web_funcs import card_1, card_2, boot_activate, dyn_back

###ACTIVATE BOOTSTRAP###
boot_activate()

###DYNAMIC BACKGOUND###
dyn_back()

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
            padding: 06px;
        }
    </style>
    <body>
        <p class="one">Bem vindo(a) ao módulo prático de Fraseologia do curso. <br> Aqui você irá encontrar diversas abas, cada uma com uma finalidade de treinamento.</p>
        <p class="two"></p>
        <p class="tree">Em cada uma delas você será instruído a realizar <u>exercícios de fixação</u> <br>para melhorarseu desempenho nas comunicações aeronáuticas.</p>
    </body>''',unsafe_allow_html=True
    )

### 6 BOXES WITH PRODUCT FEATURES ###
col4, col5 = st.columns(2)

### AUTORIZAÇAO E CIRCUITO DE TRÁFEGO CARDS ###
with col4:
    st.markdown(
        card_1(
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

    #st.text("")

### TORRE E SOLO CARDS ###
with col5:
    st.markdown(card_2('Solo:','Solo','Exercícios com o objetivo de treinar a fraseologia de movimentações no solo.',""),unsafe_allow_html=True)
    st.text("")
    #st.markdown(card1('Torre:','Voo/Solo','Fraseologia básica de TWR com autorizações de pouso, decolagem, condicionais etc.',""),unsafe_allow_html=True)
    #st.text("")
