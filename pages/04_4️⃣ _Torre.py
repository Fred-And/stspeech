import streamlit as st
from funcs.webfuncs import importpic, srg, enunciado

logo = st.container()

with logo:
    st.image('img/logo.png', use_column_width=True)

# ### MAIN PICTURE ###
# with mainpic:
#     strpic = importpic()
#     st.image(f'img/ad/{strpic}',caption= varenunci[1],use_column_width=True)

# ### QUESTION TITLE ###
# with enunci:
#     st.text(f'Você, {varenunci[0]}, está {varenunci[3]} do aeroporto de(o): {varenunci[1]} e deve contactar a posição: {varenunci[2]}. ')


# ### ACTION BUTTON ###
# if st.button('responder'):
#     gravar = srg()
#     benchmark = f'{varenunci[0]}{varenunci[2]} {varenunci[1]} {varenunci[3]} solicita instruções de partida'
#     #benchmark01 = "testando"
#     with open('text.txt') as f:
#         resposta = str(f.readlines(0))

#     resform = resposta[2:-2]
#     # print(resposta[1:2])
#     if resform == benchmark:
#         st.text("Resposta Correta")
#         with open('text.txt', 'w'):
#             pass

#     else:
#         st.text(f"Você disse {resform}, o correto seria: {benchmark}")
#         with open('text.txt', 'w'):
#             pass
# else:
#     st.write('aguardando')