import streamlit as st
from db import  Info_Cabecalho,Info_Rodada,Info_Rodada_Ativa

 
def mostrar_cabecalho_publico(usuario):
    
    # Pega o seq do usuário passado
    seq_usuario = usuario["seq"]

    # Busca as informações completas do usuário
    
    info = Info_Cabecalho(seq_usuario)

    rank = info["Rank"] or 0
    pontos = info["Pontos"] or 0
    
    
    rodada = Info_Rodada()
    rodadax = rodada["Rodada"]

    rodada_ativa = Info_Rodada_Ativa()
    rodadax_Ativa = rodada_ativa["Rodada"]    
 
       
     
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="50" style="margin-right: 15px;">
        <p style="margin: 0; font-size: 16px;">{usuario["evento"]} - {usuario["nome"]}   </p>
          <h2 style="margin: 0; font-size: 16px;">  &nbsp; &nbsp; &nbsp;     🏆 #{rank}º [{pontos}] pts  ֎ {rodadax_Ativa}/{rodadax}</h2>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
    
    
    st.page_link("your_app.py", label="Home", icon="🏠")
    st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
    st.page_link("http://www.google.com", label="Google", icon="🌎")    
    

    
    
 