import streamlit as st
import requests

def perfil_page():
    
   
    



    usuario = st.session_state.get("usuario_logado", {})

    st.title(f"👤 {usuario.get('nome', '---')}")

    # Foto padrão (quando não encontra no servidor)
    FOTO_PADRAO = f"https://boladecapotao.com/Palpiteiros/{usuario.get}.png"

    # Pega o nome do arquivo e remove barras/espacos extras
    nome_arquivo_foto = usuario.get("foto", "").strip().lstrip("/")

    if nome_arquivo_foto:
        url_foto = f"https://boladecapotao.com/Palpiteiros/{nome_arquivo_foto}"

        # Testa se a URL existe
        try:
            resposta = requests.head(url_foto, timeout=5)
            if resposta.status_code == 200:
                st.image(url_foto, width=150, caption=usuario.get("nome", "Usuário"))
            else:
                st.image(FOTO_PADRAO, width=150, caption="Sem foto")
        except requests.RequestException:
            st.image(FOTO_PADRAO, width=150, caption="Erro ao carregar foto")
    else:
        st.image(FOTO_PADRAO, width=150, caption="Sem foto cadastrada")

    # Dados do usuário
    st.write(f"**Nome:** {usuario.get('nome', '---')}")
    st.write(f"**ID:** {usuario.get('seq', '---')}")

    