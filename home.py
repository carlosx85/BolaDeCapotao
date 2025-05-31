import streamlit as st
import time

from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,buscar_jogos_ativos,atualizar_placar,normalizar_nome

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


        jogos = buscar_jogos_ativos(usuario["seq"])

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            # Cabeçalhos da "tabela"
            st.markdown("### Jogos Ativos")
            header = st.columns([1, 1, 2.5, 2.5, 1.5, 1.5, 2])
            header[0].markdown("**Seq**")
            header[1].markdown("**ID**")
            header[2].markdown("**Mandante**")
            header[3].markdown("**Visitante**")
            header[4].markdown("**Placar**")
            header[5].markdown("**Placar**")
            header[6].markdown("**Ação**")

            for i, jogo in enumerate(jogos, start=1):
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                visitante = jogo["Visitante"]
                mandante_gol = jogo["Mandante_Gol"] or 0
                visitante_gol = jogo["Visitante_Gol"] or 0

                with st.container():
                    st.markdown("---")
                    col1, col2, col3 = st.columns([1, 2, 1])

                    # Escudo Mandante
                    with col1:
                        st.image(f"https://boladecapotao.com/times/{mandante.lower()}.png", width=50)

                    # Infos centrais
                    with col2:
                  
                        novo_mandante_gol = st.number_input(
                            "Gols", min_value=0, value=int(mandante_gol),
                            key=f"mandante_gol_{i}"
                        )
                        novo_visitante_gol = st.number_input(
                            "Gols", min_value=0, value=int(visitante_gol),
                            key=f"visitante_gol_{i}"
                        )
                        if st.button("Salvar", key=f"btn_{i}"):
                            sucesso = atualizar_placar(seq, novo_mandante_gol, novo_visitante_gol)
                            if sucesso:
                                st.success("Placar atualizado com sucesso!")

                    # Escudo Visitante
                    with col3:
                        st.image(f"https://boladecapotao.com/times/{visitante.lower()}.png", width=50)






        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
