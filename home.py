import streamlit as st

def home_page():
    usuario = st.session_state.get("usuario_logado", {})
    st.title(f"Bem-vindo, {usuario.get('nome', '')}!")
    st.write(f"Email: {usuario.get('email', '')}")

    if st.button("Logout"):
        st.session_state.clear()
        st.session_state["pagina"] = "login"
