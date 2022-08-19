import streamlit as st
from funcs.webfuncs import importpic, srg, enunciado, dynback, centerlogo,bootactivate

###ACTIVATE BOOTSTRAP###
bootactivate()

###LOGO CENTER FUNC###
centerlogo()

###DYNAMIC BACKGROUND###
dynback()

### PAGE SELECTOR

def main_page():
    st.markdown("# Main Page")
    st.sidebar.markdown("# Main Page")

def page2():
    st.markdown("# Page 2")
    st.sidebar.markdown("# Page 2")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a Page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()