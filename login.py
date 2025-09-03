import streamlit as st
from db import validar_login

def login_page():
    if "usuario_logado" in st.session_state:
        st.session_state["pagina"] = "home"
        st.rerun()
        return

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


    email = st.text_input("Email", value="carlos.santosx85@hotmail.com")
    senha = st.text_input("Senha", type="password" , value="3")
    st.session_state.clear()
    if st.button("Entrar"):
        if validar_login(email, senha):
            st.success("Login realizado com sucesso!")
            
            st.rerun()  # Redireciona após login
        else:
            st.error("Email ou senha inválidos.")
