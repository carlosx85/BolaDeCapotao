import streamlit as st
import base64

if "usuario" not in st.session_state:
    st.session_state.usuario = ""

 
def show():
    header_html = f"""
    <div style="display: flex; align-items: center; padding: 10px 0 5px 0;">
        <img src="https://boladecapotao.com/bet/images/BolaDeCapotao.png" width="50" style="margin-right: 15px;">
        <h5 style="margin: 0;">Racha do Parque  ({st.session_state.usuario})</h5>
    </div>
    <hr style="margin-top: 5px; margin-bottom: 15px;">
    """
    st.markdown(header_html, unsafe_allow_html=True)
    
    

    st.markdown("""
        <style>
            body {
                background-color: #053048;
            }
            [data-testid="stAppViewContainer"] {
                background-color: #black;
            }
            [data-testid="stHeader"], [data-testid="stToolbar"] {
                background: none;
            }
            [data-testid="stSidebar"] {
                background-color: #black;
            }
        </style>
    """, unsafe_allow_html=True)

  
