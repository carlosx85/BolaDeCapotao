import streamlit as st
import requests
from db import get_rodadas,get_jogos
import pandas as pd
 


def adm_rodada():
    st.write("Informações da rodada aqui.") 
    usuario = st.session_state.get("usuario_logado", {})
    st.title(f"👤 {usuario.get('nome', '---')}")
    st.write(f"**ID:** {usuario.get('seq', '---')}")
    
 
    rodadas = get_rodadas()

    for rodada in rodadas:
        rodada_nome = f"Rodada {rodada['Rodada']} - {rodada['StatusRodada']}"
        if rodada["Rodada_Ativa_SN"] == "S":
            rodada_nome += " ✅ (Ativa)"
            
            
                # Expander por rodada
        with st.expander(rodada_nome, expanded=False):
            jogos = get_jogos(rodada["Rodada"])   # ou rodada["Seq"] se for o campo certo
            if jogos:
                df = pd.DataFrame(jogos)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Nenhum jogo ativo para esta rodada.")