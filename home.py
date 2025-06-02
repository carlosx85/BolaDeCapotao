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
        
                
        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            st.markdown(f"Bem-vindo, {usuario['nome']}!")

            for i, jogo in enumerate(jogos, start=1):
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                visitante = jogo["Visitante"]

                mandante_key = f"mandante_gol_{seq}"
                visitante_key = f"visitante_gol_{seq}"

                # Inicializa valores em branco, se necessário
                st.session_state.setdefault(mandante_key, "")
                st.session_state.setdefault(visitante_key, "")

                with st.container():
                    st.markdown("---")
                    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

                    with col1:
                        st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=100)

                    with col5:
                        st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=100)

                    # Toda a entrada de dados e botão dentro do formulário
                    with st.form(key=f"form_{seq}", clear_on_submit=True):
                        with col2:
                            mandante_gol_str = st.text_input(
                                label="",
                                value=st.session_state[mandante_key],
                                placeholder="Gols",
                                key=f"{mandante_key}_input"
                            )

                        with col4:
                            visitante_gol_str = st.text_input(
                                label="",
                                value=st.session_state[visitante_key],
                                placeholder="Gols",
                                key=f"{visitante_key}_input"
                            )

                        with col3:
                            submit = st.form_submit_button("Salvar")

                        if submit:
                            if not mandante_gol_str.strip() or not visitante_gol_str.strip():
                                st.error("⚠️ Preencha todos os campos de gols.")
                            else:
                                try:
                                    novo_mandante_gol = int(mandante_gol_str)
                                    novo_visitante_gol = int(visitante_gol_str)

                                    sucesso = atualizar_placar_pendente(seq, jogo_id, novo_mandante_gol, novo_visitante_gol)
                                    atualizar_placar_pendente_palpite()

                                    # Limpa os valores no session_state
                                    st.session_state[mandante_key] = ""
                                    st.session_state[visitante_key] = ""

                                    if sucesso:
                                        st.success("✅ Placar atualizado com sucesso!")

                                    # Atualiza a tela
                                    st.rerun()

                                except ValueError:
                                    st.error("⚠️ Os valores devem ser números inteiros.")



                
                
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
