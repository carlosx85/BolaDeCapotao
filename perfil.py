import streamlit as st





def perfil_page():
    st.title("👤 Perfil do dddUsuário")
    usuario = st.session_state.get("usuario_logado", {})
    st.write(f"Nome: **{usuario.get('nome', '---')}**")
    st.write(f"ID: **{usuario.get('seq', '---')}**")