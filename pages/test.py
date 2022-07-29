import streamlit as st
import random as rd
import os

choices = []

### IMPORT A RANDOM AUDIO FOR THE EXERCISE ###
audiopath = '/Users/fred/Documents/Repos/Streamlit/fraseologia/audios'
audio = rd.choice(os.listdir(audiopath))
st.audio(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audios/{audio}')

### IMPORT SCRIPT BASED ON THE RANDM AUDIO IMPORTED ###
scriptname = f"{audio[:-4]}.txt" ### TRANSFORMING THE .mp3 STRING IN A .txt
with open(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audioscripts/{scriptname}', 'r') as scp:
    excript = scp.readlines()[1] # exercise script, without variables#
with open(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audioscripts/{scriptname}', 'r') as scp:
    benchmark = scp.readlines()[0] # full script that will be used as benchmark
with open(f'/Users/fred/Documents/Repos/Streamlit/fraseologia/audioscripts/{scriptname}', 'r') as scp:
    var = scp.readlines()[2]# correct variables
    varlist = var.split(",")
    choices.append(varlist)

### SELECT BOXES ###
with st.container():
    col1, col2, col3, col4, col5 = st.columns(5) #number o columns that I'll place the selectboxex #

    with col1:
        options = [
            " ",
            choices[0][1],
            choices[0][0],
            choices[0][2],
            choices[0][4],
            choices[0][3],
            ]
        #sb1 = st.selectbox('', options)
        sb1 = choices[0][0]

    with col2:
        options1 = [
            " ",
            choices[0][2],
            choices[0][0],
            choices[0][1],
            choices[0][4],
            choices[0][3],
            ]
        #sb2 = st.selectbox('', options1)
        sb2 = choices[0][1]

    with col3:
        options2 = [
            " ",
            choices[0][1],
            choices[0][4],
            choices[0][2],
            choices[0][0],
            choices[0][3],
            ]
        #sb3 = st.selectbox('', options2)
        sb3 = choices[0][2]

    with col4:
        options3 = [
            " ",
            choices[0][0],
            choices[0][1],
            choices[0][3],
            choices[0][4],
            choices[0][2],
            ]
        #sb4 = st.selectbox('',options3)
        sb4 = choices[0][3]

    with col5:
        options4 = [
            " ",
            choices[0][1],
            choices[0][2],
            choices[0][0],
            choices[0][4],
            choices[0][3],
            ]
        #sb5 = st.selectbox('',options4)
        sb5 = choices[0][4]
st.markdown(
    excript,
    unsafe_allow_html=True)
answer = excript.replace("___1___",sb1).replace("___2___",sb2).replace("___3___",sb3).replace("___4___",sb4).replace("___5___",sb5[:-1])

print(answer)
print()
if st.button("Enviar"):
    if answer == benchmark:
        st.write("Boa!! Parabéns")
    else:
        st.write("Não foi dessa vez")
else:
    st.write("Aguardando resposta")

if __name__ == "__main__":
    print(answer)
    print(benchmark)

    print (choices)

    print(answer == benchmark)
