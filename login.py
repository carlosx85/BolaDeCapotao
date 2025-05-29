import streamlit as st
from layout import mostrar_cabecalho_publico
from db import validar_login

 

def login_page():
    # Se já estiver logado, redireciona para a home
    if "usuario_logado" in st.session_state:
        st.session_state["pagina"] = "home"
        st.rerun()
        return

    # Cabeçalho público (só aparece se não estiver logado)
    mostrar_cabecalho_publico()
    
    st.title("Login")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
            st.session_state["pagina"] = "home"  # Atualiza a página
            st.rerun()  # Redireciona imediatamente para home
        else:
            st.error("Email ou senha inválidos.")
