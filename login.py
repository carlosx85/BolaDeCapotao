import streamlit as st
from db import validar_login

def login_page():
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
        else:
            st.error("Email ou senha inválidos.")

    st.markdown("---")
    if st.button("Ir para Cadastro"):
        st.session_state["pagina"] = "cadastro"
