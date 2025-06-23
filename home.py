import streamlit as st
import time
from layout import mostrar_cabecalho_publico
from db import (
    ativar_rodada_01, rodada_inicio, atualizar_placar_pendente,
    atualizar_placar_pendente_palpite, buscar_jogos_ativos_preenchido,
    rodada_inicio_ativar, verificar_rodada_ativa, buscar_jogos_ativos_Pendente,
    verificar_email_sn, atualizar_email_sn_para_s, atualizar_email_sn_para_s1
)


def mostrar_perfil(usuario):
    st.subheader("👤 Perfil")
    st.write(f"Nome: **{usuario.get('nome', '')}**")
    st.write(f"ID: {usuario.get('seq', '')}")


def mostrar_rodada(usuario):
    email_sn = verificar_email_sn(usuario["seq"])
    
    if email_sn == "N":
        st.info("Deseja participar do Palpitrômito do Bola de Capotão?")
        if st.button("Eu quero participar"):
            with st.spinner("Processando..."):
                atualizar_email_sn_para_s(usuario["seq"]) 
                atualizar_email_sn_para_s1(usuario["seq"])
                for percent in range(100):
                    time.sleep(0.01)
                    st.progress(percent + 1, text="Atualizando...")
                time.sleep(1)
                ativar_rodada_01()
                st.success("Agora você está participando! Boa sorte! 🎉")
                st.rerun()
        return
    
    jogos = buscar_jogos_ativos_Pendente(usuario["seq"])
    
    if not jogos:
        rodadaativa = verificar_rodada_ativa(usuario["seq"])
        rodada_ativa = rodadaativa["Rodada"]
        rodada_inicio_ativar()
        rodadainiciox = rodada_inicio(usuario["seq"], rodada_ativa) 
        rodadaativa = rodadainiciox["Rodada_Ativa_SN"]

        st.badge(f"Rodada #{rodada_ativa}", icon="🏁", color="green")

        jogosx = buscar_jogos_ativos_preenchido(usuario["seq"])             

        for jogo in jogosx:
            pontos = jogo["Pontos"]
            mandante = jogo["Mandante"]
            visitante = jogo["Visitante"]
            palpite_mandante_gol = jogo["Palpite_Mandante_Gol"] or "-"
            palpite_visitante_gol = jogo["Palpite_Visitante_Gol"] or "-"
            mandante_gol = jogo["Mandante_Gol"] or ""
            visitante_gol = jogo["Visitante_Gol"] or ""

            st.markdown(
                f"""
                <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px;">
                    <img src="https://boladecapotao.com/times/{mandante.lower()}.png" width="30" />
                    <span style="font-size: 26px;">{palpite_mandante_gol} x {palpite_visitante_gol}</span>
                    <img src="https://boladecapotao.com/times/{visitante.lower()}.png" width="30" />
                    <span style="font-size: 26px;">{pontos or ''} pts</span>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.subheader("🔢 Atualizar Palpites")
        if "placares_temp" not in st.session_state:
            st.session_state.placares_temp = {}

        for jogo in jogos:
            mandante = jogo["Mandante"]
            visitante = jogo["Visitante"]
            jogo_id = jogo["Id"]
            seq = jogo["Seq"]
            mandante_gol = jogo["Mandante_Gol"] or 0
            visitante_gol = jogo["Visitante_Gol"] or 0

            col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])
            with col1:
                st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=50)
            novo_mandante = col2.number_input("", min_value=0, value=int(mandante_gol), key=f"m_{jogo_id}")
            novo_visitante = col3.number_input("", min_value=0, value=int(visitante_gol), key=f"v_{jogo_id}")
            with col4:
                st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=50)

            st.session_state.placares_temp[jogo_id] = {
                "mandante_gol": novo_mandante,
                "visitante_gol": novo_visitante,
                "mandante": mandante,
                "visitante": visitante
            }

        if st.button("Atualizar Todos"):
            for jogo_id, placar in st.session_state.placares_temp.items():
                atualizar_placar_pendente(seq, jogo_id, placar["mandante_gol"], placar["visitante_gol"])
            atualizar_placar_pendente_palpite()
            st.rerun()


def mostrar_dashboard():
    st.subheader("📊 DashBoard")
    st.info("Em construção...")


def sair():
    st.session_state.clear()
    st.success("Sessão encerrada.")
    st.stop()


def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]
    mostrar_cabecalho_publico(usuario)

    st.sidebar.title("Menu")
    pagina = st.sidebar.radio("Ir para:", ["Perfil", "Rodada", "DashBoard", "Sair"])

    if pagina == "Perfil":
        mostrar_perfil(usuario)
    elif pagina == "Rodada":
        mostrar_rodada(usuario)
    elif pagina == "DashBoard":
        mostrar_dashboard()
    elif pagina == "Sair":
        sair()
