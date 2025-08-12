import streamlit as st
from login import login_page
from home import home_page

# Páginas extras
def perfil_page():
    st.title("👤 Perfil do Usuário")
    usuario = st.session_state.get("usuario_logado", {})
    st.write(f"Nome: **{usuario.get('nome', '---')}**")
    st.write(f"ID: **{usuario.get('seq', '---')}**")

def rodada_page():
    st.title("⚽ Rodada")
    st.write("Informações da rodada aqui.")

def dashboard_page():
    st.title("📊 Dashboard")
    st.write("Gráficos e relatórios aqui.")

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    # Se não logado, sempre vai para login
    if "usuario_logado" not in st.session_state and st.session_state["pagina"] != "login":
        st.session_state["pagina"] = "login"

    # Página atual
    pagina = st.session_state["pagina"]

    if pagina == "login":
        login_page()  # login_page deve definir usuario_logado e pagina="home" se login for ok

    else:
        # Sidebar só aparece após login
        st.sidebar.title(f"Olá, {st.session_state['usuario_logado']['nome']} 👋")
        opcao = st.sidebar.radio(
            "Navegar para:",
            ("Perfil", "Home", "Rodada", "Dashboard", "Sair"),
            index=["Perfil", "Home", "Rodada", "Dashboard", "Sair"].index(pagina)
        )
        st.session_state["pagina"] = opcao.lower()  # controla pelo nome em minúsculo

        # Roteamento
        if opcao == "Perfil":
            perfil_page()
        elif opcao == "Home":
            home_page()
        elif opcao == "Rodada":
            rodada_page()
        elif opcao == "Dashboard":
            dashboard_page()
        elif opcao == "Sair":
            st.session_state.pop("usuario_logado", None)
            st.session_state["pagina"] = "login"
            st.success("Você saiu do sistema.")
            st.rerun()

if __name__ == "__main__":
    main()
