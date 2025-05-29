import streamlit as st
from database import validar_login
import main_menu  # importa para redirecionar sem recarregar


if "usuario" not in st.session_state:
    st.session_state.email = ""

# Inicializa estado
if "logado" not in st.session_state:
    st.session_state.logado = False

# Se logado, mostra tela principal
if st.session_state.logado:
    main_menu.show()

# Senão, mostra tela de login
else:
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
    nome = validar_login(email, senha)
    if nome:
        st.session_state.logado = True
        st.session_state.nome   = nome
        st.session_state.email  = email
        
        
        
        st.rerun()
    else:
        st.error("Usuário ou senha inválidos.")

