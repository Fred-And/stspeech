import streamlit as st
from funcs.webfuncs import importpic, srg, enunciado, dynback, centerlogo,bootactivate
from pratico.autorizacao import autorizacaopage
###ACTIVATE BOOTSTRAP###
bootactivate()

###LOGO CENTER FUNC###
centerlogo()

###DYNAMIC BACKGROUND###
dynback()

### PAGE SELECTOR
autorizacaopage()

def main_page():
    st.markdown("# Main Page")
    st.sidebar.markdown("# Main Page")

def autorizacao():
     st.markdown("# Autorização")
     st.sidebar.markdown("# Autorização")
     #autorizacaopage()


page_names_to_funcs = {
    "Main Page": main_page,
    "Autorização": autorizacao,
}

selected_page = st.sidebar.selectbox("Select a Page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()