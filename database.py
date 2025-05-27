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
    cursor = conexao.cursor(buffered=True)  # <-- corrigido aqui
    consulta = "SELECT * FROM Usuario WHERE email = %s AND senha = %s"
    cursor.execute(consulta, (email, senha))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is not None


