import streamlit as st

def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado para acessar esta página.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]
    st.title(f"Bem-vindo, {usuario['nome']}!")
