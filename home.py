import streamlit as st
import time
import pandas as pd
import urllib.parse

from db import buscar_jogos_pendentes,verificar_rodada_ativa,verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,atualizar_placar_pendente_palpite,buscar_jogos_ativos_Pendente,atualizar_placar_pendente

def home_page():
    if "usuario_logado" not in st.session_state:
        st.warning("Você precisa estar logado.")
        st.session_state["pagina"] = "login"
        st.rerun()
        return

    usuario = st.session_state["usuario_logado"]  
    

    email_sn = verificar_email_sn(usuario["seq"])   
   
    
    dados_rodada = verificar_rodada_ativa(usuario["seq"]) 
    rodada = dados_rodada["Rodada"]
 
 
 
    
    
    

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
            st.success("Agora você está participando!" )
            st.balloons()            
            st.rerun()          
            
            
    elif email_sn == "S":            
         

         
        jogos = buscar_jogos_ativos_Pendente(usuario["seq"])

        if not jogos:
            
        # Página Principal
            st.title(f"Rodada {rodada} Preenchida pelo usuário :sunglasses:")
            
            


            df_jogos = buscar_jogos_pendentes()

            if df_jogos.empty:
                st.info("Nenhum jogo pendente.")
                return

            for _, row in df_jogos.iterrows():
                with st.form(key=f"form_{row['ID']}"):
                    # Layout em linha com 5 colunas: escudo, input, input, escudo, botão
                    cols = st.columns([1, 0.5, 0.5, 1, 0.5])

                    mandante_img = f"https://boladecapotao.com/times/{urllib.parse.quote(row['Mandante'].lower())}.png"
                    visitante_img = f"https://boladecapotao.com/times/{urllib.parse.quote(row['Visitante'].lower())}.png"

                    with cols[0]:
                        st.image(mandante_img, width=80)

                    with cols[1]:
                        gols_mandante = st.number_input(
                            "", min_value=0, value=row["Mandante_Gol"],
                            key=f"gm_{row['ID']}"
                        )

                    with cols[2]:
                        gols_visitante = st.number_input(
                            "", min_value=0, value=row["Visitante_Gol"],
                            key=f"gv_{row['ID']}"
                        )

                    with cols[3]:
                        st.image(visitante_img, width=80)

                    with cols[4]:
                        salvar = st.form_submit_button("Salvar")

                    if salvar:
                        salvar_gols(row["ID"], gols_mandante, gols_visitante)
                        st.success("Resultado salvo com sucesso!")
                    
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
          
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
                    atualizado = atualizar_placar_pendente(seq,jogo_id, placar["mandante_gol"], placar["visitante_gol"])


                if sucesso_total:
                    atualizadox = atualizar_placar_pendente_palpite()
                    st.rerun() 
                    st.info("Todos os placares foram atualizados com sucesso.")
                else:
                    st.info("Todos os placares foram atualizados com sucesso.")

                                







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
