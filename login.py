import streamlit as st
from db import validar_login

def login_page():
    
    
        # Só mostra o cabeçalho quando NÃO está logado
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="150">
            <p style="font-size: 12px; margin-top: 5px;">Bola de Capotão</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
        else:
            st.error("Email ou senha inválidos.")

    st.markdown("---")

