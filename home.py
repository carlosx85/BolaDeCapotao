import streamlit as st
from db import verificar_email_sn, atualizar_email_sn_para_s

def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]
    st.title(f"Bem-vindo, {usuario['nome']}!")

    email_sn = verificar_email_sn(usuario["seq"])

    if email_sn == "N":
        st.info("Você ainda não está participando.")
        if st.button("Participar"):
            atualizar_email_sn_para_s(usuario["seq"])
            st.success("Agora você está participando!")
            st.rerun()
    elif email_sn == "S":
        st.success("Você já está participando!")
    else:
        st.error("Não foi possível verificar seu status de participação.")
