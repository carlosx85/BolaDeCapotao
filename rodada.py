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
        # Define ícone do palpite
        if rodada["Palpite"] == "Pendente":
            palpite_texto = "Palpitou? 🔴"
        else:
            palpite_texto = "Palpitou? ✅"



        # Texto final
        rodada_nome = (
            f"Rodada {rodada['Rodada']} "
            f"({rodada['StatusRodada']}) "
            f"{rodada['Palpite']}   {palpite_texto} → {mostrar_texto}"
        )

        with st.expander(rodada_nome, expanded=False):
            st.write(f"Detalhes da rodada {rodada['Rodada']} aqui...")
                        # Condição Mostrar / Não Mostrar
            if rodada["StatusRodada"] == "Ativo" and rodada["Palpite"] == "Pendente":
                mostrar_texto = "Mostrar"
            else:
                mostrar_texto = "Não Mostrar"

            
            
            
            
            
            
            
 