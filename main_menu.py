import streamlit as st
from modules.principal import show as principal_show
from modules.cadastro import show as cadastro_show
from modules.financeiro import show as financeiro_show
from modules.pagamento import show as pagamento_show
from modules.despesa import show as despesa_show 
import header  # se tiver


if "usuario" not in st.session_state:
    st.session_state.usuario = ""

def show():
    header.show()   


    menu = st.sidebar.radio("Menu", ["Principal", "Cadastro", "Financeiro", "Pagamento", "Despesa", "Sair"])


    if menu == "Principal":
        principal_show()
    elif menu == "Cadastro":
        cadastro_show()
    elif menu == "Financeiro":
        financeiro_show()
    elif menu == "Pagamento":
        pagamento_show()
    elif menu == "Despesa":
        despesa_show()
    elif menu == "Sair":
        st.session_state.logado = False
        st.session_state.usuario = ""
        st.rerun()
        
 

