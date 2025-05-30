import streamlit as st
import time
from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,buscar_jogos_ativos,atualizar_mandante_gol

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
        
        
        
        
    
        # Interface principal
        st.title("Atualização de Gols do Mandante - Rodada Ativa")

        jogos = buscar_jogos_ativos(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            for i, jogo in enumerate(jogos, start=1):
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                mandante_gol = jogo["Mandante_Gol"] or 0

                # Input para editar o número de gols
                novo_gol = st.number_input(
                    f"{i}. {mandante} (ID: {jogo_id}, Seq: {seq}) - Gols do Mandante",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"gol_{seq}"
                )

                # Botão para atualizar
                if st.button(f"Salvar gols para {mandante} (Seq: {seq})", key=f"btn_{seq}"):
                    sucesso = atualizar_mandante_gol(seq, novo_gol)
                    if sucesso:
                        st.success(f"Gols atualizados para {mandante} com sucesso!")


 
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
