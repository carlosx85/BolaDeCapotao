import streamlit as st
from layout import mostrar_cabecalho_publico
from db import validar_login

def login_page():
    if "usuario_logado" in st.session_state:
        st.session_state["pagina"] = "home"
        st.rerun()
        return

    mostrar_cabecalho_publico()
    email = st.text_input("Email", Value="carlos.santosx85@hotmail.com")
    senha = st.text_input("Senha", type="password" , value="3")

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
            st.rerun()  # Redireciona após login
        else:
            st.error("Email ou senha inválidos.")
