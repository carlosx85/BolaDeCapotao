import streamlit as st
from login import login_page
from home import home_page

def main():
    if "pagina" not in st.session_state:
        st.session_state["pagina"] = "login"

    pagina = st.session_state["pagina"]

    if pagina == "login":
        login_page()
    elif pagina == "home":
        home_page()

if __name__ == "__main__":
    main()
