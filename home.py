import streamlit as st
import pandas as pd
import time

# ========== SUA HOME EXISTENTE ==========
from layout import mostrar_cabecalho_publico
from db import (
    Info_Rodada_Pontos_Seq, Info_Cabecalho, Info_Rank,
    atualizar_online, ativar_rodada_01, rodada_inicio,
    atualizar_placar_pendente, atualizar_placar_pendente_palpite,
    buscar_jogos_ativos_preenchido, rodada_inicio_ativar, verificar_rodada_ativa,
    buscar_jogos_ativos_Pendente, verificar_email_sn,
    atualizar_email_sn_para_s, atualizar_email_sn_para_s1
)

def home_page():
    usuario = st.session_state.get("usuario_logado", {"nome": "Visitante"})
    mostrar_cabecalho_publico(usuario)

    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "Home"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"] 
    email_sn = verificar_email_sn(usuario["seq"]) 

    if email_sn == "N":
        st.info("Deseja participar do Palpitrômito do Bola de Capotão?")
        if st.button("Eu quero participar."):
            with st.spinner("Processando..."):
                atualizar_email_sn_para_s(usuario["seq"]) 
                atualizar_email_sn_para_s1(usuario["seq"])
                my_bar = st.progress(0, text="Operação em Atualização!!! Aguarde")
                for percent_complete in range(100):
                    time.sleep(0.02) 
                    my_bar.progress(percent_complete + 1, text="Operação em Atualização!!! Aguarde")
                time.sleep(2)
                my_bar.empty()
            ativar_rodada_01()          
            st.rerun() 
            st.balloons()
            st.success("Agora você está participando do Palpitrômito do Bola de Capotão! Boa sorte!")  

    elif email_sn == "S": 
        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])
        if not jogos:
            rodadaativa = verificar_rodada_ativa(usuario["seq"])
            rodada_ativa = rodadaativa["Rodada"]
            rodada_inicio_ativar()
            rodadainiciox = rodada_inicio(usuario["seq"], rodada_ativa) 
            rodadaativa = rodadainiciox["Rodada_Ativa_SN"]
            atualizar_online(rodada_ativa) 

            if rodadaativa == 'N':  
                st.badge(f"Rodada Ativa **# {rodada_ativa}**", icon=":material/check:", color="green")
                jogosx = buscar_jogos_ativos_preenchido(usuario["seq"])      
                for jogo in jogosx:
                    palpite_mandante_gol = jogo["Palpite_Mandante_Gol"] or "-"
                    palpite_visitante_gol = jogo["Palpite_Visitante_Gol"] or "-"
                    mandante = jogo["Mandante"]
                    visitante = jogo["Visitante"] 
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px;">
                            <img src="https://boladecapotao.com/times/{mandante.lower()}.png" width="30" />
                            <span>{palpite_mandante_gol} x {palpite_visitante_gol}</span>
                            <img src="https://boladecapotao.com/times/{visitante.lower()}.png" width="30" />
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                infox = Info_Rodada_Pontos_Seq(usuario["seq"], rodada_ativa)
                pontosa = infox["Pontos"] or 0 
                st.badge(f"Rodada Ativa **# {rodada_ativa}** 🚀 {pontosa} Pts", icon=":material/check:", color="green")   

                jogosx = buscar_jogos_ativos_preenchido(usuario["seq"]) 
                for jogo in jogosx:
                    mandante_gol = jogo["Mandante_Gol"] or ""
                    visitante_gol = jogo["Visitante_Gol"] or ""
                    mandante = jogo["Mandante"]
                    visitante = jogo["Visitante"] 
                    pontos = jogo["Pontos"] or ""
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px;">
                            <span>{mandante_gol} x {visitante_gol}</span>
                            <img src="https://boladecapotao.com/times/{mandante.lower()}.png" width="30" />
                            <span>{jogo["Palpite_Mandante_Gol"] or "-"} x {jogo["Palpite_Visitante_Gol"] or "-"}</span>
                            <img src="https://boladecapotao.com/times/{visitante.lower()}.png" width="30" />
                            <span>{pontos}</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        else:
            st.markdown("### Jogos Ativos")
            if "placares_temp" not in st.session_state:
                st.session_state.placares_temp = {}
            for jogo in jogos:
                mandante_gol = jogo["Mandante_Gol"] or 0
                visitante_gol = jogo["Visitante_Gol"] or 0
                jogo_id = jogo["Id"]
                seq = jogo["Seq"]
                col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])
                with col1:
                    st.image(f"https://boladecapotao.com/times/{jogo['Mandante'].lower()}.png", width=50)
                    st.markdown(jogo["Mandante"])
                novo_mandante = col2.number_input("", min_value=0, value=int(mandante_gol), key=f"mandante_gol_{jogo_id}")
                novo_visitante = col3.number_input("", min_value=0, value=int(visitante_gol), key=f"visitante_gol_{jogo_id}")
                with col4:
                    st.image(f"https://boladecapotao.com/times/{jogo['Visitante'].lower()}.png", width=50)
                    st.markdown(jogo["Visitante"])
                st.session_state.placares_temp[jogo_id] = {
                    "mandante_gol": novo_mandante,
                    "visitante_gol": novo_visitante
                }
            if st.button("Atualizar Todos"):
                for jogo_id, placar in st.session_state.placares_temp.items():
                    atualizar_placar_pendente(seq, jogo_id, placar["mandante_gol"], placar["visitante_gol"])
                atualizar_placar_pendente_palpite()
                st.rerun()
                st.info("Todos os placares foram atualizados com sucesso.")

        # Ranking
        def cor_rank(rank):
            return {
                1: "background-color: green; color: white",
                2: "background-color: yellow; color: black",
                3: "background-color: blue; color: white"
            }.get(rank, "background-color: red; color: white")

        def aplicar_estilo(df):
            return df.style.applymap(cor_rank, subset=["Rank"]).hide(axis="index")

        st.write("🏅 Ranking de Classificação")
        df = pd.DataFrame(Info_Rank())
        st.dataframe(aplicar_estilo(df), use_container_width=True)

# ========== OUTRAS PÁGINAS ==========
def rodada_page():
    st.title("⚽ Página da Rodada")
    st.write("Conteúdo da Rodada...")

def dashboard_page():
    st.title("📊 Dashboard")
    st.write("Gráficos e indicadores...")

# ========== MENU LATERAL ==========
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

st.sidebar.title("📌 Menu")
opcao = st.sidebar.radio(
    "Navegar para:",
    ("Home", "Rodada", "Dashboard", "Sair"),
    index=["Home", "Rodada", "Dashboard", "Sair"].index(st.session_state.pagina)
)
st.session_state.pagina = opcao

# Roteamento
if st.session_state.pagina == "Home":
    home_page()
elif st.session_state.pagina == "Rodada":
    rodada_page()
elif st.session_state.pagina == "Dashboard":
    dashboard_page()
elif st.session_state.pagina == "Sair":
    st.session_state.clear()
    st.success("Você saiu do sistema.")
    st.stop()
