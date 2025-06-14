import streamlit as st
import time
from layout import mostrar_cabecalho_publico
from db import verificar_email_sn 


    
def home_page():
    mostrar_cabecalho_publico()  # Mostra o cabeçalho público
 

    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"] 
    email_sn = verificar_email_sn(usuario["seq"]) 
    

    


        
        
        
        
        
 
            
            
            