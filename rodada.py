import streamlit as st
import requests


def rodada():  
    
    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")