import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page  # Certifique-se de ter instalado esse extra


from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,atualizar_placar_pendente_palpite,buscar_jogos_ativos_Pendente,atualizar_placar_pendente

def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]

    
    
    
    
    
    
    
    
    

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

        st.title("Atualização de Placar - Rodada Ativa")

        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            st.markdown("### Jogos Ativos")
 

            # Armazenar alterações temporárias
            if "placares_temp" not in st.session_state:
                st.session_state.placares_temp = {}

            for i, jogo in enumerate(jogos, start=1):

                mandante = jogo["Mandante"]
                mandante_gol = jogo["Mandante_Gol"] or 0
                visitante_gol = jogo["Visitante_Gol"] or 0
                visitante = jogo["Visitante"]
                jogo_id = jogo["Id"]
                seq = jogo["Seq"]
                
                

                col1, col2, col3, col4 = st.columns([1, 0.5, 0.5, 1])
                #col1.write(jogo_id)
                #col2.write(seq)
                
                with col1:
                    st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=50)# Gols Mandante (como texto, para permitir vazio)
                    
                novo_mandante = col2.number_input(
                    label="",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"mandante_gol_{jogo_id}"
                )
                
                
                
                novo_visitante = col3.number_input(
                    label="",
                    min_value=0,
                    value=int(visitante_gol),
                    key=f"visitante_gol_{jogo_id}"
                )
                
                with col4:
                    st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=50)

                st.session_state.placares_temp[jogo_id] = {
                    "mandante_gol": novo_mandante,
                    "visitante_gol": novo_visitante,
                    "mandante": mandante,
                    "visitante": visitante
                }
 

                if st.button("Atualizar Todos"):
                    sucesso_total = True
                    for jogo_id, placar in st.session_state.placares_temp.items():
                        atualizado = atualizar_placar_pendente(seq, jogo_id, placar["mandante_gol"], placar["visitante_gol"])
                        atualizadox = atualizar_placar_pendente_palpite()

 

                    if sucesso_total:
                        st.info("Todos os placares foram atualizados com sucesso.")
                        st.success("Redirecionando para a página inicial...")
                         
                    else:
                        st.warning("Nem todos os placares foram atualizados com sucesso.")


                                







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
