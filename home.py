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
            dados = buscar_rodada_ativa_seq(usuario["seq"])

            if not dados:
                st.warning("Nenhum dado encontrado.")
                return                   
           
            safe_key = f"seq_{str(seq).replace('-', '_').replace(' ', '_')}"
            
            
            for i, item in enumerate(dados, start=1):
                seq = str(item.get("Seq")) if item.get("Seq") is not None else f"sem_seq_{i}"     
                id = item.get("Id", "—")   
                mandante = item.get("Mandante", "—")     
                mandante_gol = item.get("Mandante_Gol", 0)     
                 
                novo_gol = st.number_input(
                    f"{i}. {mandante} (Seq: {seq}) - Gols:",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"gol_{safe_key}"
                )

                if st.button(f"Salvar gols para {mandante}", key=f"btn_{safe_key}"):

                
                
                # Botão para salvar a alteração
                if st.button(f"Salvar gols para {mandante}", key=f"btn_{seq}"):
                    
                
                
                
                
                
                st.markdown(f"""
                    <div style="font-size: 12px;">
                        <b>{i}.  {seq} {id} {mandante} {mandante_gol}
                    </div>
                """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro ao buscar dados: {e}")
        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
