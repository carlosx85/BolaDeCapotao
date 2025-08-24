import streamlit as st
import requests
from datetime import datetime

def carregar_meses():
    return list(range(1, 38))
 
 

def adm_page():  

    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")


    mes_atual = datetime.now().month
 

    # Carregar listas com cache
    meses = carregar_meses()
 

    # Tipos de despesa
    opcoes = [" " , "Lavagem dos Coletes", "Compra de Bola", "Compra de Coletes", "Material de Farmácia"]
    tipo_despesa = st.selectbox("Selecione o Tipo de Despesa:", opcoes)

    # Seleção de mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
    with col2:
 
 

    if st.button("Efetuar o pagamento"):
        if tipo_despesa.strip() == "":
            st.error("O campo 'Tipo de Despesa' é obrigatório.")
        else:
            atualizar_valor_despesa(mes,   tipo_despesa )
            st.success("✅ Pagamento efetuado com sucesso!")
    