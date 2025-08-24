import streamlit as st
from login import login_page
from home import home_page
from perfil import perfil_page


# Páginas extras
def rodada_page():
    st.title("⚽ Rodada")
    st.write("Informações da rodada aqui.")
    
def adm_page():
    st.title("⚙️ Administração")
    st.write("Área restrita para administradores.")

def dashboard_page():
    st.title("📊 Dashboard")
    st.write("Gráficos e relatórios aqui.")

def main():
    # inicializa página
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    # se não estiver logado, força login
    if "usuario_logado" not in st.session_state and st.session_state["pagina"] != "login":
        st.session_state["pagina"] = "login"

    # fluxo: se for login, mostra login_page (ela deve setar usuario_logado e pagina="home")
    if st.session_state["pagina"] == "login":
        login_page()
        return

    usuario = st.session_state.get("usuario_logado", {})

    # --- Sidebar ---
    st.sidebar.title(f"Olá, {usuario.get('nome','Usuário')} 👋")

    # Menu padrão
    pages = [
        ("perfil", "Perfil"),
        ("home", "Home"),
        ("rodada", "Rodada"),
        ("dashboard", "Dashboard"),
    ]

    # Só adiciona "Adm" se for admin
    if usuario.get("adm") == "S":
        pages.append(("adm", "Administração"))

    # Sempre por último o "Sair"
    pages.append(("sair", "Sair"))

    # cria lista de labels
    labels = [label for _, label in pages]

    # encontra índice atual baseado na key
    current_key = st.session_state.get("pagina", "home")
    current_index = next((i for i, (k, _) in enumerate(pages) if k == current_key), 1)

    chosen_label = st.sidebar.radio("Navegar para:", labels, index=current_index)

    # converte label para key
    chosen_index = labels.index(chosen_label)
    chosen_key = pages[chosen_index][0]

    # atualiza página
    st.session_state["pagina"] = chosen_key

    # roteamento
    if chosen_key == "perfil":
        perfil_page()
    elif chosen_key == "home":
        home_page()
    elif chosen_key == "rodada":
        rodada_page()
    elif chosen_key == "dashboard":
        dashboard_page()
    elif chosen_key == "adm":
        adm_page()
    elif chosen_key == "sair":
        st.session_state.pop("usuario_logado", None)
        st.session_state["pagina"] = "login"
        st.success("Você saiu do sistema.")
        st.rerun()

if __name__ == "__main__":
    main()
