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
        # Interface principal
        st.title("Atualização de Gols do Mandante - Rodada Ativa")

        jogos = buscar_jogos_ativos()

        if not jogos:
            st.warning("Nenhum jogo ativo encontrado.")
        else:
            # Cabeçalhos da "tabela"
            st.markdown("### Jogos Ativos")
            header_cols = st.columns([1, 1, 3, 2, 2])
            header_cols[0].markdown("**Seq**")
            header_cols[1].markdown("**ID**")
            header_cols[2].markdown("**Mandante**")
            header_cols[3].markdown("**Gols**")
            header_cols[4].markdown("**Ação**")

            for i, jogo in enumerate(jogos, start=1):
                seq = jogo["Seq"]
                jogo_id = jogo["Id"]
                mandante = jogo["Mandante"]
                mandante_gol = jogo["Mandante_Gol"] or 0

                col1, col2, col3, col4, col5 = st.columns([1, 1, 3, 2, 2])

                col1.write(seq)
                col2.write(jogo_id)
                col3.write(mandante)
                novo_gol = col4.number_input(
                    label="",
                    min_value=0,
                    value=int(mandante_gol),
                    key=f"gol_{seq}_{i}
                )
                if col5.button("Salvar", key=f"btn_{seq}_{i}"):
                sucesso = atualizar_mandante_gol(seq, novo_gol)
                if sucesso:
                        st.success(f"Atualizado: {mandante} ({seq}) -> {novo_gol} gol(s)")






        
        
        
        
        
    else:
        st.error("Não foi possível verificar seu status de participação.")
        
        
 
