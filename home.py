import streamlit as st
import time
from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,buscar_rodada_ativa_seq

def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]
    st.title(f"Bem-vindo, {usuario['nome']}!")
    
    
    
    
    
    
    
    
    

    email_sn = verificar_email_sn(usuario["seq"])

    if email_sn == "N":
        st.info("Você ainda não está participando.")
        if st.button("Participar"):
            with st.spinner("Processando..."):
                atualizar_email_sn_para_s(usuario["seq"])   
                  
                atualizar_email_sn_para_s1(usuario["seq"])
                progress_text = "Operação em Atualização!!! Aguarde"
                my_bar = st.progress(0, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.02)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(2)
                
                my_bar.empty()
            st.success("Agora você está participando!")
            st.balloons()            
            st.rerun()          
            
            
    elif email_sn == "S":     
        
        
        
        
    
        try:
            dados = buscar_rodada_ativa_seq(seq)

            if not dados:
                st.warning("Nenhum dado encontrado.")
                return                   
           

            for i, item in enumerate(dados, start=1):
                seq = item.get("Seq", "—")              

                
                
                st.markdown(f"""
                    <div style="font-size: 12px;">
                        <b>{i}. {seq} 
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
