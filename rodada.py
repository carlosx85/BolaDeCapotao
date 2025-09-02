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
        if palpite_raw == "pendente":
            palpite_texto = "Palpitou? 🔴"
        else:
            palpite_texto = "Palpitou? ✅"

        rodada_nome = (
            f"Rodada {rodada['Rodada']} "
            f"({rodada['StatusRodada']}) "
            f"{rodada['Palpite']}   {palpite_texto}"
        )

        with st.expander(rodada_nome, expanded=False):
            # condição correta
            if status_raw == "ativo" and status_raw == "pendente":
                st.write("👉 **Mostrar**")

                # busca só quando precisa
                jogosx = get_jogos(id_usuario, rodada["Rodada"])

                if jogosx:
                    for jogo in jogosx:
                        pontos = jogo["Pontos"]
                        mandante = jogo["Mandante"]
                        visitante = jogo["Visitante"]

                        palpite_mandante_gol = jogo["Palpite_Mandante_Gol"] if jogo["Palpite_Mandante_Gol"] is not None else "-"
                        palpite_visitante_gol = jogo["Palpite_Visitante_Gol"] if jogo["Palpite_Visitante_Gol"] is not None else "-"
                        mandante_gol = jogo["Mandante_Gol"] if jogo["Mandante_Gol"] is not None else ""
                        visitante_gol = jogo["Visitante_Gol"] if jogo["Visitante_Gol"] is not None else ""

                        st.markdown(
                            f"""
                            <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px;">
                                <img src="https://boladecapotao.com/times/{mandante.lower()}.png" width="30" />
                                <span style="font-size: 18px;">{palpite_mandante_gol} x {palpite_visitante_gol}</span>
                                <img src="https://boladecapotao.com/times/{visitante.lower()}.png" width="30" />
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            else:
                st.write("🚫 **Não Mostrar**")

