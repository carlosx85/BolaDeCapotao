import streamlit as st
import requests
from datetime import datetime
from db import atualizar_rodada

def carregar_rodada():
    return list(range(1, 38))


def adm_page():  

    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")


    mes_atual = datetime.now().month
  

    # Carregar listas com cache
    rodadas = carregar_rodada()
     

    # Tipos de despesa
    opcoes = ["Ativo" , "Encerrado", "Pendente"]
    tipo = st.selectbox("Selecione o Status:", opcoes)

    # Seleção de mês e ano 
 
    rodada = st.selectbox("Rodada", rodadas, index=rodadas.index(mes_atual) if mes_atual in rodadas else 0)
 

 

    if st.button("Efetuar o pagamento"):
        if tipo_despesa.strip() == "":
            st.error("O campo 'Tipo de Despesa' é obrigatório.")
        else:
            atualizar_rodada(rodada, tipo)
            st.success("✅ Pagamento efetuado com sucesso!")
    