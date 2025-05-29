import streamlit as st
from layout import mostrar_cabecalho_publico
from db import validar_login

def login_page():
    # Exibe cabeçalho só se o usuário não estiver logado
    mostrar_cabecalho_publico()
    
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    
    

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()  # <- só roda depois que tudo deu certo
        else:
            st.error("Email ou senha inválidos.")

