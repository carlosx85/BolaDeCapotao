import streamlit as st
import requests
from db import get_rodadas 
 


def adm_rodada():
    st.write("Informações da rodada aqui.") 
    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")
    
 