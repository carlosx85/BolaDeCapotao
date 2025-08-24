import streamlit as st
import requests

def adm_page():  

    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")


    mes_atual = datetime.now().month
    ano_atual = datetime.now().year

    # Carregar listas com cache
    meses = carregar_meses()
    anos = carregar_anos()

    # Tipos de despesa
    opcoes = [" " , "Lavagem dos Coletes", "Compra de Bola", "Compra de Coletes", "Material de Farmácia"]
    tipo_despesa = st.selectbox("Selecione o Tipo de Despesa:", opcoes)

    # Seleção de mês e ano
    col1, col2, _ = st.columns([2, 4, 6])
    with col1:
        mes = st.selectbox("Mês", meses, index=meses.index(mes_atual) if mes_atual in meses else 0)
    with col2:
        ano = st.selectbox("Ano", anos, index=anos.index(ano_atual) if ano_atual in anos else 0)

    # Inputs de valor e descrição
    valor = st.number_input("Digite o Valor da Despesa:",min_value=0, step=1, format="%d")
    descricao = st.text_input("Descrição", max_chars=100)

    if st.button("Efetuar o pagamento"):
        if tipo_despesa.strip() == "":
            st.error("O campo 'Tipo de Despesa' é obrigatório.")
        else:
            atualizar_valor_despesa(mes, ano, tipo_despesa, descricao, valor)
            st.success("✅ Pagamento efetuado com sucesso!")
    