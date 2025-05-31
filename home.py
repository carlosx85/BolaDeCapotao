import streamlit as st
import time
from db import verificar_email_sn, atualizar_email_sn_para_s,atualizar_email_sn_para_s1,buscar_jogos_ativos,atualizar_placar

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
            header[4].markdown("**Gols Mandante**")
            header[5].markdown("**Gols Visitante**")
            header[6].markdown("**Ação**")

            for i, jogo in enumerate(jogos, start=1):
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                visitante = jogo["Visitante"]
                mandante_gol = jogo["Placar"] or 0
                visitante_gol = jogo["Placar"] or 0

                col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 2.5, 2.5, 1.5, 1.5, 2])
                col1.write(seq)
                col2.write(jogo_id)
                col3.write(mandante)
                col4.write(visitante)

                novo_mandante_gol = col5.number_input(
                    label="",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"mandante_gol_{seq}_{i}"
                )
                novo_visitante_gol = col6.number_input(
                    label="",
                    min_value=0,
                    value=int(visitante_gol),
                    key=f"visitante_gol_{seq}_{i}"
                )

                if col7.button("Salvar", key=f"btn_{seq}_{i}"):
                    sucesso = atualizar_placar(seq, novo_mandante_gol, novo_visitante_gol)
                    if sucesso:
                        st.success(f"Placar atualizado: {mandante} {novo_mandante_gol} x {novo_visitante_gol} {visitante}")






        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
