import streamlit as st


def perfil_page():
   
    

    # Recupera o dicionário do usuário logado
    usuario = st.session_state.get("usuario_logado", {})

    # Pega o nome do arquivo de foto
    nome_arquivo_foto = usuario.get("foto")

    if nome_arquivo_foto:
        # Monta a URL da imagem
        url_foto = f"https://boladecapotao.com/Palpiteiros/{nome_arquivo_foto}"
        
        # Exibe a imagem
        st.image(url_foto, caption=usuario.get("nome", ""), width=150)
    else:
        st.write("Usuário sem foto cadastrada.")