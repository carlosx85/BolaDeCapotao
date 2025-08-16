import streamlit as st


def perfil_page():
   
    

    usuario = st.session_state.get("usuario_logado", {})
    
    st.title(f"👤 {usuario.get('nome', '---')}")

    # Exibe a foto de perfil
    nome_arquivo_foto = usuario.get("foto")  # ex.: "carlos.jpg"
    if nome_arquivo_foto:
                    st.markdown(
                        f"""
                        <div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 10px;">
                            <span style="font-size: 18px; font-weight: ;"> </span>
                            <img src="https://boladecapotao.com/times/{usuario}.png" width="30" />
 
                        </div>
                        """,
                        unsafe_allow_html=True        
        
        
    else:
        st.info("📷 Nenhuma foto cadastrada.")

    # Dados do usuário
    st.write(f"**Nome:** {usuario.get('nome', '---')}")
    st.write(f"**ID:** {usuario.get('seq', '---')}")
    
