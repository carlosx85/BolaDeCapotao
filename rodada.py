import streamlit as st
import requests
from db import get_rodadas 
 


def adm_rodada():
    st.write("Informações da rodada aqui.") 
    usuario = st.session_state.get("usuario_logado", {})
    st.title(f"👤 {usuario.get('nome', '---')}")
    
 
    rodadas = get_rodadas()

    for rodada in rodadas:
        rodada_nome = f"Rodada {rodada['Rodada']} - {rodada['StatusRodada']}"
        if rodada["Rodada_Ativa_SN"] == "S":
            rodada_nome += " ✅ (Ativa)"