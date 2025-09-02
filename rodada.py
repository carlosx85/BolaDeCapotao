import streamlit as st
import requests
from db import get_rodadas,get_jogos,buscar_jogos_ativos_preenchido
import pandas as pd
 


def adm_rodada():
    st.write("Informações da rodada aqui.") 
    usuario = st.session_state.get("usuario_logado", {})
    st.title(f"👤 {usuario.get('nome', '---')}")
    st.write(f"**ID:** {usuario.get('seq', '---')}")
    id_usuario = usuario.get("seq", None)
    
 
    rodadas = get_rodadas(id_usuario)

    for rodada in rodadas:
        if rodada["Palpite"] == "Pendente":
            palpite_texto = "Palpitou? 🔴"
        else:
            palpite_texto = "Palpitou? ✅"
        
        rodada_nome = f"Rodada {rodada['Rodada']} ({rodada['StatusRodada']}) {rodada['Palpite']}   {palpite_texto}"
        
      
            
            
            
            
            
            
        
        with st.expander(rodada_nome, expanded=False):
