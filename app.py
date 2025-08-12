import streamlit as st
from login import login_page
from home import home_page
from perfil import perfil_page
from rodada import rodada_page
from dashboard import dashboard_page

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    # Se não estiver logado, mostra apenas login
    if st.session_state["pagina"] == "login":
        login_page()
        return

    # Sidebar só aparece após login
    st.sidebar.title(f"Olá, {st.session_state['usuario_logado']['nome']} 👋")

    opcao = st.sidebar.radio(
        "Navegar para:",
        ("Perfil", "Home", "Rodada", "Dashboard", "Sair"),
        index=["Perfil", "Home", "Rodada", "Dashboard", "Sair"].index(
            st.session_state["pagina"].capitalize()
        )
    )

    if opcao == "Sair":
        st.session_state.pop("usuario_logado", None)
        st.session_state["pagina"] = "login"
        st.rerun()
    else:
        st.session_state["pagina"] = opcao.lower()

    # Roteamento — executa no mesmo clique
    if opcao == "Perfil":
        perfil_page()
    elif opcao == "Home":
        home_page()
    elif opcao == "Rodada":
        rodada_page()
    elif opcao == "Dashboard":
        dashboard_page()

if __name__ == "__main__":
    main()
