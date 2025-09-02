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
        # Pegamos os valores originais do banco
        status_raw = str(rodada["StatusRodada"]).strip().lower()
        palpite_raw = str(rodada["Palpite"]).strip().lower()

        # Só montamos o texto de exibição
        if palpite_raw == "Pendente":
            palpite_texto = "Palpitou? 🔴"
        else:
            palpite_texto = "Palpitou? ✅"

        rodada_nome = (
            f"Rodada {rodada['Rodada']} "
            f"({rodada['StatusRodada']}) "
            f"{rodada['Palpite']}   {palpite_texto}"
        )

        with st.expander(rodada_nome, expanded=False):
            if status_raw == "Ativo" and palpite_raw == "Pendente":
                st.write("👉 **Mostrar**")
            else:
                st.write(f"🚫 **Não Mostrar** ({rodada['StatusRodada']})")


            
            
            
            
            
            


                
                
            else:
                st.info("Nenhum jogo ativo para esta rodada.")