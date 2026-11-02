import streamlit as st
from user_interface import ControlsTab, ChartsTab

def setup_UI():
    #configure page
    st.set_page_config(layout="wide")
    st.title("Team Bath Biodevices: Membrane Testing App")

    #create page tabs
    tab_controls, tab_charts = st.tabs(["Environmental Parameters", "Analysis"])

    with tab_controls:
        ControlsTab().render()

    with tab_charts:
        ChartsTab().render()


setup_UI()


