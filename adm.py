import streamlit as st
import requests

def adml_page():  

    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")



    