import streamlit as st
from layout import mostrar_cabecalho_publico
from db import validar_login

 
    

    # Só mostra o cabeçalho quando NÃO está logado
st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="150">
            <p style="font-size: 12px; margin-top: 5px;">Bola de Capotãox</p>
        </div>
        """,
        unsafe_allow_html=True
    )



def login_page():
    mostrar_cabecalho_publico()

    st.title("Login")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
            st.experimental_rerun()  # <-- Força a troca para home
        else:
            st.error("Email ou senha inválidos.")

    

