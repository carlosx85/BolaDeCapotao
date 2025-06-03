import streamlit as st
import time
import pandas as pd
import urllib.parse
from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,atualizar_placar_pendente_palpite,buscar_jogos_ativos_Pendente,atualizar_placar_pendente
from db import buscar_jogos_ativos_Pendente
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


        st.title("Formulário de Resultados dos Jogos")

        df_jogos =    buscar_jogos_ativos_Pendente(usuario["seq"])

        for idx, row in df_jogos.iterrows():
            with st.form(key=f"form_{row['ID']}"):
                st.markdown(f"### Jogo ID {row['ID']}")

                cols = st.columns([2, 1, 2])

                mandante_img_url = f"https://boladecapotao.com/times/{urllib.parse.quote(row['Mandante'].lower())}.png"
                visitante_img_url = f"https://boladecapotao.com/times/{urllib.parse.quote(row['Visitante'].lower())}.png"

                # Coluna 1: Mandante
                with cols[0]:
                    st.image(mandante_img_url, width=100, caption=row['Mandante'])
                    gols_mandante = st.number_input("Gols Mandante", min_value=0, value=row['Mandante_Gol'], key=f"mandante_{row['ID']}")

                # Coluna 2: "X"
                with cols[1]:
                    st.markdown("<h3 style='text-align: center;'>X</h3>", unsafe_allow_html=True)

                # Coluna 3: Visitante
                with cols[2]:
                    st.image(visitante_img_url, width=100, caption=row['Visitante'])
                    gols_visitante = st.number_input("Gols Visitante", min_value=0, value=row['Visitante_Gol'], key=f"visitante_{row['ID']}")

                # Botão de salvar
                if st.form_submit_button("Salvar"):
                    atualizar_placar_pendente(row['ID'], gols_mandante, gols_visitante)
                    atualizar_placar_pendente_palpite(row['ID'], gols_mandante, gols_visitante)
                    st.success("Resultado salvo com sucesso!")


                                







        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
