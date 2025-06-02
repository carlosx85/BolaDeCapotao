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


        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            # Cabeçalhos da "tabela"
            st.markdown(f"### Jogos Ativos")
            
            for i, jogo in enumerate(jogos, start=1):
                    
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                visitante = jogo["Visitante"]
                
                mandante_key  = f"mandante_gol_{seq}"
                visitante_key = f"visitante_gol_{seq}"
                # ■■■ FORÇA A LIMPEZA antes de exibir o input ■■■
                # Se a chave não existir, inicializa como string vazia
                if mandante_key not in st.session_state:
                    st.session_state[mandante_key] = ""
                if visitante_key not in st.session_state:
                    st.session_state[visitante_key] = ""

                with st.container():
                    st.markdown("---")
                    
                    # Colunas horizontais: escudo1 | gol1 | botão | gol2 | escudo2
                    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

                    # Escudo Mandante
                    with col1:
                        st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=100)# Gols Mandante (como texto, para permitir vazio)
                    
                    with col2:
                        mandante_key = f"mandante_gol_{seq}"
                        mandante_gol_str = st.text_input(
                            label="",
                            value=st.session_state[mandante_key],
                            placeholder="",
                            key=f"mandante_gol_{i}"
                        )

                    # Gols Visitante (como texto, para permitir vazio)
                    with col3:
                        visitante_key = f"visitante_gol_{seq}"
                        visitante_gol_str = st.text_input(
                            label="",
                            value=st.session_state[visitante_key],
                            placeholder="",
                            key=f"visitante_gol_{i}"
    )


                    # Escudo Visitante
                    with col4:
                        st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=100)
                        
                    
                    # Botão centralizado
                    with col5:
                        
 
                                
                        if st.button("Salvar", key=f"btn_{i}"):
                            if not mandante_gol_str.strip() or not visitante_gol_str.strip():
                                st.error("⚠️ Preencha todos os campos de gols.")
                            else:
                                try:
                                    novo_mandante_gol = int(mandante_gol_str)
                                    novo_visitante_gol = int(visitante_gol_str)

                                    sucesso  = atualizar_placar_pendente(seq, jogo_id, novo_mandante_gol, novo_visitante_gol)
                                    sucessox = atualizar_placar_pendente_palpite()
                                    
                                st.session_state["pagina_atual"] = "jogos"
                                                # ────────── ZERA OS DOIS INPUTS ──────────
                                st.session_state[mandante_key]  = ""
                                st.session_state[visitante_key] = ""
                                st.rerun()
                                                        

                                    
                                    
                                    if sucesso:
                                        st.success("✅ Placar atualizado com sucesso!")
                                        


                                except ValueError:
                                    st.error("⚠️ Os valores devem ser números inteiros.")

                                







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
