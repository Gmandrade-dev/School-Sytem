import psycopg2
import pandas as pd

# Configurações para conectar ao banco padrão (postgres), que permite criar outros bancos
host = 'localhost'
user = 'postgres'      # substitua pelo seu usuário do PostgreSQL
password = 'admin@'    # substitua pela sua senha
port = 5432
 
# Etapa 1: Conecta ao banco padrão 'postgres' para criar o banco 'db_escola'
try:
    conexao_inicial = psycopg2.connect(
        host=host,
        dbname='postgres',   # banco padrão que permite criar outros
        user=user,
        password=password,
        port=port
    )
    conexao_inicial.autocommit = True # Necessário para comandos como CREATE DATABASE
    cursor_inicial = conexao_inicial.cursor()
 
   # Cria o banco de dados 'db_escola'
    cursor_inicial.execute("CREATE DATABASE db_escola")
    print("Banco de dados 'db_escola' criado com sucesso!")
 
except psycopg2.errors.DuplicateDatabase:
   print("O banco de dados 'db_escola' já existe. Pulando criação.")
except Exception as erro:
   print("Erro ao criar banco de dados:", erro)
finally:
   # Fecha a conexão inicial
   if cursor_inicial:
      cursor_inicial.close()
   if conexao_inicial:
      conexao_inicial.close()

# Etapa 2: Conecta ao banco de dados 'db_escola' para criar a tabela



