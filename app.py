import streamlit as st
from login import login_page
from home import home_page
# from cadastro import cadastro_page

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    if st.session_state["pagina"] == "login":
        login_page()
    elif st.session_state["pagina"] == "home":
        home_page()
    # elif st.session_state["pagina"] == "cadastro":
    #     cadastro_page()

if __name__ == "__main__":
    main()
