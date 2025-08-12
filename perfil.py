import streamlit as st


def perfil_page():
    st.title("👤 Perfil do Usuário")

    usuario = st.session_state.get("usuario_logado", {})

    # Exibe a foto de perfil
    nome_arquivo_foto = usuario.get("foto")  # ex.: "carlos.jpg"
    if nome_arquivo_foto:
        url_foto = f"https://boladecapotao.com/Palpiteiros/{nome_arquivo_foto}"
        st.image(url_foto, width=150, caption=usuario.get("nome", "Usuário"))
    else:
        st.info("📷 Nenhuma foto cadastrada.")

    # Dados do usuário
    st.write(f"**Nome:** {usuario.get('nome', '---')}")
    st.write(f"**ID:** {usuario.get('seq', '---')}")
