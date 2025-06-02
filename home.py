import streamlit as st
import time

from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,atualizar_placar_pendente_palpite,buscar_jogos_ativos_Pendente,atualizar_placar_pendente

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

        # No topo do seu arquivo/home_page, antes de buscar os jogos:
        if st.session_state.get("limpar_campos"):
            for jogo in buscar_jogos_ativos_Pendente(usuario["seq"]):
                seq = jogo["Seq"]
                st.session_state[f"mandante_gol_{seq}"] = ""
                st.session_state[f"visitante_gol_{seq}"] = ""
            st.session_state["limpar_campos"] = False
            st.rerun()

        # Depois, sua lógica original, ajustada para NÃO usar value=st.session_state.get(...)
        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            st.markdown("### Jogos Ativos")

            for jogo in jogos:
                seq     = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante   = jogo["Mandante"]
                visitante  = jogo["Visitante"]

                mandante_key  = f"mandante_gol_{seq}"
                visitante_key = f"visitante_gol_{seq}"

                with st.container():
                    st.markdown("---")
                    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

                    # Escudo Mandante
                    with col1:
                        st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=100)

                    # Gols Mandante (texto), sem o parâmetro value
                    with col2:
                        mandante_gol_str = st.text_input(
                            label="",
                            key=mandante_key
                        )

                    # Gols Visitante (texto), sem o parâmetro value
                    with col3:
                        visitante_gol_str = st.text_input(
                            label="",
                            key=visitante_key
                        )

                    # Escudo Visitante
                    with col4:
                        st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=100)

                    # Botão Salvar
                    with col5:
                        if st.button("Salvar", key=f"btn_{seq}"):
                            if not mandante_gol_str.strip() or not visitante_gol_str.strip():
                                st.error("⚠️ Preencha todos os campos de gols.")
                            else:
                                try:
                                    novo_mandante_gol  = int(mandante_gol_str)
                                    novo_visitante_gol = int(visitante_gol_str)

                                    sucesso = atualizar_placar_pendente(
                                        seq, jogo_id, novo_mandante_gol, novo_visitante_gol
                                    )
                                    atualizar_placar_pendente_palpite()

                                    if sucesso:
                                        st.session_state["limpar_campos"] = True
                                        st.success("✅ Placar atualizado com sucesso!")

                                    st.rerun()

                                except ValueError:
                                    st.error("⚠️ Os valores devem ser números inteiros.")

                                        







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
