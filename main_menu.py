import streamlit as st
import header  # se tiver


if "email" not in st.session_state:
    st.session_state.email = ""



def show():
    header.show()   