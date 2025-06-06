import mysql.connector
import streamlit as st
import pandas as pd
import unicodedata


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

def buscar_jogos_ativos_Pendente(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT  * FROM Jogos WHERE StatusRodada LIKE 'Ativo' AND Seq =  %s  AND  Palpite LIKE 'Pendente'        
    """
    cursor.execute(query, (seq, ))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados


def buscar_jogos_ativos_Pendente_OK(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT  * FROM Jogos WHERE StatusRodada LIKE 'Ativo' AND Seq =  %s  AND  Palpite <> 'Pendente'        
    """
    cursor.execute(query, (seq, ))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados





def atualizar_mandante_gol(seq,id):
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Usuario SET email_SN = 'S' WHERE Seq = %s and  ID = %s and  StatusRodada LIKE 'Ativo'"
    cursor.execute(atualiza, (seq,id))
    conexao.commit()
    cursor.close()
    conexao.close()
    
    
def atualizar_placar_pendente(seq,jogo_id,mandante_gol, visitante_gol):
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Jogos SET Palpite_Mandante_Gol = %s, Palpite_Visitante_Gol = %s WHERE Seq = %s AND id = %s "
    cursor.execute(atualiza, (mandante_gol, visitante_gol, seq,jogo_id))
    conexao.commit()
    cursor.close()
    conexao.close()
    
def atualizar_placar_pendente_palpite():
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Jogos SET Palpite = CASE WHEN Palpite_Mandante_Gol = Palpite_Visitante_Gol THEN 'Empate'    WHEN Palpite_Mandante_Gol > Palpite_Visitante_Gol THEN Mandante  WHEN Palpite_Mandante_Gol < Palpite_Visitante_Gol THEN Visitante     ELSE 'Pendente' END WHERE StatusRodada LIKE 'Ativo';"
    cursor.execute(atualiza, ())
    conexao.commit()
    cursor.close()
    conexao.close()
    
    
import unicodedata
def normalizar_nome(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
    return nome.lower().replace(" ", "-")


def verificar_rodada_ativa(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    consulta = "SELECT Nome,Rodada,StatusRodada FROM  Jogos WHERE Seq = %s AND  StatusRodada = 'Ativo' GROUP BY Nome,Rodada,StatusRodada"
    cursor.execute(consulta, (seq,))
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def buscar_jogos_ativos_preenchido(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT  * FROM Jogos WHERE StatusRodada LIKE 'Ativo' AND Seq =  %s  AND  Palpite <> 'Pendente'        
    """
    cursor.execute(query, (seq, ))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados
    

def rodada_inicio(seq,rodada_ativa):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    query = """
        SELECT Mandante_Gol,Rodada,Seq,StatusRodada FROM Jogos_Inicio  WHERE Mandante_Gol >=0 AND Seq =%s AND Rodada = %s        
    """
    cursor.execute(query, (seq,rodada_ativa ))
    resultados = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultados    






