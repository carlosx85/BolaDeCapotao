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


def atualizar_email_sn_para_s(seq):
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "INSERT INTO Jogos ( Seq, Nome, Rodada, Mandante, Visitante, Casa, Fora, Data_Participacao ) SELECT Usuario.Seq, Usuario.Nome, Jogos_Origem.Rodada, Jogos_Origem.Mandante, Jogos_Origem.Visitante, Jogos_Origem.Casa, Jogos_Origem.Fora,NOW() FROM Usuario, Jogos_Origem WHERE Usuario.Seq  = %s ORDER BY Jogos_Origem.Mandante"
    cursor.execute(atualiza, (seq,))
    conexao.commit()
    cursor.close()
    conexao.close()
    
def atualizar_email_sn_para_s1(seq):
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Usuario SET email_SN = 'S' WHERE Seq = %s"
    cursor.execute(atualiza, (seq,))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    
    
    
# database.py

def buscar_rodada_ativa_seq(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT  * FROM Jogos WHERE StatusRodada LIKE 'Ativo' AND Seq =  %s         
    """
    cursor.execute(query, (seq, ))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados



def atualizar_seq_rodada(seq,id):
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Usuario SET email_SN = 'S' WHERE Seq = %s and  ID = %s and  StatusRodada LIKE 'Ativo'"
    cursor.execute(atualiza, (seq,id))
    conexao.commit()
    cursor.close()
    conexao.close()




