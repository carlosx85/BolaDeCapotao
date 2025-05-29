import mysql.connector
import streamlit as st
import pandas as pd


def conectar():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"],
        charset=st.secrets["mysql"]["charset"]  # Certifique-se de que está puxando 'utf8mb4'
    )

def validar_login(email, senha):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    consulta = "SELECT * FROM Usuario WHERE email = %s AND senha = %s"
    cursor.execute(consulta, (email, senha))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()

    if resultado:
        st.session_state["usuario_logado"] = {
            "seq": resultado["Seq"],
            "nome": resultado["Nome"],
            "email": resultado["email"]
        }
        st.session_state["pagina"] = "home"  # Troca para página home
        return True
    return False


def verificar_email_sn(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    consulta = "SELECT email_SN FROM Usuario WHERE Seq = %s"
    cursor.execute(consulta, (seq,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado["email_SN"] if resultado else None


