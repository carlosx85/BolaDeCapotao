import streamlit as st

def mostrar_cabecalho_publico():
    if "usuario_logado" not in st.session_state:
        st.markdown(
            """
            <div style="text-align: center;">
                <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="150">
                <p style="font-size: 12px; margin-top: 5px;">Bola de Capotão</p>
            </div>
            """,
            unsafe_allow_html=True
        )
