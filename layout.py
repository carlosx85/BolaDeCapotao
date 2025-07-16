import streamlit as st
from db import  Info_Cabecalho

 

 



 

 
def mostrar_cabecalho_publico(usuario):
    
    # Pega o seq do usuário passado
    seq_usuario = usuario["seq"]

    # Busca as informações completas do usuário
    info = Info_Cabecalho(seq_usuario)

    # Exemplo: Rank e Pontos (você deve ajustar isso se quiser valores reais)
    rank = info.get("Rank", "?")     # se não existir, mostra "?"
    pontos = info.get("Pontos", "???")  # idem
 
       
    
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="50" style="margin-right: 15px;">
        <p style="margin: 0; font-size: 20px;">{usuario["evento"]} - {usuario["nome"]} {usuario["seq"]} </p>
         <h2 style="margin: 0; font-size: 20px;">    # 🏆  {rank} º  {pontos}pts</h2>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)
    

    
    
 