# IMPORTS #
import streamlit as st
import requests
import random
import json
from funcs.web_funcs import boot_activate, center_logo, dyn_back, speech_rec, string_comparison


# ACTIVATE BOOTSTRAP #
boot_activate()

# LOGO CENTER FUNCTION #
center_logo()

# DYNAMIC BACKGROUND #
dyn_back()


def main_page():
    st.markdown("# Main Page")
    st.markdown("<b>This page is still being built! I apologize for the inconvenience and appreciate your comprehension</b>", unsafe_allow_html=True)
    st.sidebar.markdown("# Main Page")

def clearance():
     st.markdown("# Clearance")
     st.markdown("Same here pal...sorry. If you want some action, head to the 'Treinamento' page on the upper left-hand corner ")
     st.sidebar.markdown("# Clearance")


page_names_to_funcs = {
    "Main Page": main_page,
    "Clearance": clearance,
}

selected_page = st.sidebar.selectbox("Select a Page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
