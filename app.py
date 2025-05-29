import streamlit as st
from login import login_page
from home import home_page

 

    # Só mostra o cabeçalho quando NÃO está logado
st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="150">
            <p style="font-size: 12px; margin-top: 5px;">Bola de Capotãox</p>
        </div>
        """,
        unsafe_allow_html=True
    )

 

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    pagina_atual = st.session_state["pagina"]

    if pagina_atual == "login":
        login_page()
    elif pagina_atual == "home":
        if "usuario_logado" in st.session_state:
            home_page()
        else:
            st.warning("Você precisa estar logado.")
            st.session_state["pagina"] = "login"
    # elif pagina_atual == "cadastro":
    #     cadastro_page()

if __name__ == "__main__":
    main()
