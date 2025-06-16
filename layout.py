import streamlit as st

 
def mostrar_cabecalho_publico(usuario):
     
    
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="50" style="margin-right: 15px;">
        <p style="margin: 0; font-size: 14px;">Usuário: {usuario["nome"]} | Seq: {usuario["seq"]}</p>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)