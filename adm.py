import streamlit as st
import requests
from datetime import datetime
from db import atualizar_status_rodada_ativar,atualizar_status_rodada_desativar

def carregar_rodada():
    return list(range(1, 39))


def adm_page():  

    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")

  

    # Carregar listas com cache
    rodadas = carregar_rodada()
     

    # Tipos de despesa



    # Seleção de mês e ano 
 
 # Tipos de despesa
    opcoes = ["Ativo" , "Encerrado", "Pendente"]
    tipo = st.selectbox("Selecione o Status:", opcoes)

    rodada = st.selectbox("Selecione a Rodada:", rodadas)

 

    if st.button("Efetuar o pagamento"):
        if tipo.strip() == "":
            st.error("O campo 'Tipo' é obrigatório.")
        else:            
            atualizar_status_rodada_desativar()
            atualizar_status_rodada_ativar(tipo,rodada)

            st.success("✅ Pagamento efetuado com sucesso!")
    