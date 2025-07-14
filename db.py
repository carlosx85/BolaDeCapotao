import mysql.connector
import streamlit as st
import pandas as pd
import unicodedata
import requests
from bs4 import BeautifulSoup


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
            "evento": resultado["Evento"],
            "eventoabreviado": resultado["Evento_Abreviado"],
            "email": resultado["email"]
        }
        st.session_state["pagina"] = "home"  # Troca para página home
        return True
    return False


def verificar_email_sn(seq):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    consulta = "SELECT evento,evento_abreviado,nome,email,telefone,email_SN FROM Usuario WHERE Seq = %s"
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
    

def ativar_rodada_01():
    conexao = conectar()
    cursor = conexao.cursor()
    atualizax = "UPDATE Jogos SET StatusRodada = 'Ativo' WHERE Rodada LIKE '1'" 
    cursor.execute(atualizax,)
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
        SELECT Seq,Mandante_Gol,Rodada,Seq,StatusRodada,MAX(Rodada_Ativa_SN) AS Rodada_Ativa_SN FROM Jogos_Inicio  WHERE  Seq =%s AND Rodada = %s          
    """
    cursor.execute(query, (seq,rodada_ativa))
    resultados = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultados    


def rodada_inicio_ativar():
    conexao = conectar()
    cursor = conexao.cursor()
    atualiza = "UPDATE Jogos SET Rodada_ATiva_SN = 'S'  WHERE StatusRodada = 'Ativo' AND Mandante_Gol >=0 and Rodada_ATiva_SN = 'N';"
    cursor.execute(atualiza, ())
    conexao.commit()
    cursor.close()
    conexao.close()


def atualizar_online():
    conexao = conectar()
    cursor = conexao.cursor()
    st.write("xxxx")
    
    Rodada_Atual=1

    urlx= f'https://www.api-futebol.com.br/campeonato/campeonato-brasileiro/2025'
    url= f'https://www.api-futebol.com.br/campeonato/campeonato-brasileiro/2025/rodada/{Rodada_Atual}'

    headers ={}
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    import pandas as pd

    # Supondo que as variáveis já estejam preenchidas com os elementos extraídos pelo BeautifulSoup
    Mandante   = soup.find_all('div', {'class': 'text-right'})
    Visitante  = soup.find_all('div', {'class': 'text-left'})
    Placar     = soup.find_all('div', {'class': 'small text-center'})

    # Extrair o texto de cada elemento encontrado
    mandante_list = [element.get_text(strip=True) for element in Mandante if element.get_text(strip=True) not in ['', 'N/A']]
    visitante_list = [visitante.get_text(strip=True) for visitante in Visitante]
    placar_list = [placar.get_text(strip=True) for placar in Placar]
    max_length = max(len(mandante_list), len(visitante_list), len(placar_list))


    # Preencher listas menores com valores vazios para igualar o comprimento
    mandante_list  += [''] * (max_length - len(mandante_list))
    visitante_list += [''] * (max_length - len(visitante_list))
    placar_list    += [''] * (max_length - len(placar_list))

    # Criar um dicionário com as listas ajustadas para formar um DataFrame
    data = {
        'Mandante': mandante_list,
        'Placar': placar_list,
        'Visitante': visitante_list,
        'Rodada':  Rodada_Atual  
    }

    # Criar um DataFrame com as informações
    df = pd.DataFrame(data)
    
    apagar = f'TRUNCATE TABLE Jogos_Resultado'
    cursor.execute(apagar)
    
    for index, row in df.iterrows():
    sqlx= f'INSERT INTO Jogos_Resultado ( Mandante,Placar,Visitante,Data) VALUES (%s,%s,%s,Now())'
    valx=(row['Mandante'],row['Placar'],row['Visitante'])
    cursor.execute(sqlx,valx)
    conexao.commit()






