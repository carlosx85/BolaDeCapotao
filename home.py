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
 




        st.title("Atualização de Placar - Rodada Ativa")

        jogos = buscar_jogos_ativos()

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            st.markdown("### Jogos Ativos")
            header = st.columns([1, 1, 2.5, 2.5, 1.5, 1.5])
            header[0].markdown("**ID**")
            header[1].markdown("**Seq**")
            header[2].markdown("**Mandante**")
            header[3].markdown("**Visitante**")
            header[4].markdown("**Gols Mandante**")
            header[5].markdown("**Gols Visitante**")

            # Armazenar alterações temporárias
            if "placares_temp" not in st.session_state:
                st.session_state.placares_temp = {}

            for i, jogo in enumerate(jogos, start=1):
                jogo_id = jogo["Id"]
                seq = jogo["Seq"]
                mandante = jogo["Mandante"]
                visitante = jogo["Visitante"]
                mandante_gol = jogo["Mandante_Gol"] or 0
                visitante_gol = jogo["Visitante_Gol"] or 0

                col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 2.5, 2.5, 1.5, 1.5])
                col1.write(jogo_id)
                col2.write(seq)
                col3.write(mandante)
                col4.write(visitante)

                novo_mandante = col5.number_input(
                    label="",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"mandante_gol_{jogo_id}"
                )
                novo_visitante = col6.number_input(
                    label="",
                    min_value=0,
                    value=int(visitante_gol),
                    key=f"visitante_gol_{jogo_id}"
                )

                st.session_state.placares_temp[jogo_id] = {
                    "mandante_gol": novo_mandante,
                    "visitante_gol": novo_visitante,
                    "mandante": mandante,
                    "visitante": visitante
                }

            if st.button("Atualizar Todos"):
                sucesso_total = True
                for jogo_id, placar in st.session_state.placares_temp.items():
                    atualizado = atualizar_placar_pendente(placar["seq"],jogo_id, placar["mandante_gol"], placar["visitante_gol"])
                    atualizadox = atualizar_placar_pendente_palpite()
                    
                    if atualizado:
                        st.success(f"{placar['mandante']} {placar['mandante_gol']} x {placar['visitante_gol']} {placar['visitante']}")
                    else:
                        sucesso_total = False
                if sucesso_total:
                    st.info("Todos os placares foram atualizados com sucesso.")
                else:
                    st.warning("Alguns placares não foram atualizados. Verifique os erros acima.")

                                







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
