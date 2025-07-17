import streamlit as st
from db import  Info_Cabecalho

 

 



 

 
def mostrar_cabecalho_publico(usuario):
    
    # Pega o seq do usuário passado
    seq_usuario = usuario["seq"]

    # Busca as informações completas do usuário
    info = Info_Cabecalho(seq_usuario)
    
    rank = info.get("Rank", 0)
    pontos = info.get("Pontos", 0)
 
       
    
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="50" style="margin-right: 15px;">
        <p style="margin: 0; font-size: 20px;">{usuario["evento"]} - {usuario["nome"]} {usuario["seq"]} </p>
         <h2 style="margin: 0; font-size: 20px;">    # 🏆  {rank or 0}º   pts</h2>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)
    

    
    
 