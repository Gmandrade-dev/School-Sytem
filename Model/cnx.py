import psycopg2
from psycopg2 import sql

# Parâmetros de conexão com o servidor (não com um banco específico)
host = "localhost"
user = "postgres"
password = "admin@"
port = 5432

# Nome do novo banco de dados
nome_banco = "db_escola"

# Conecta ao servidor PostgreSQL (no banco 'postgres', que sempre existe)
try:
    conn = psycopg2.connect(
        dbname="db_escola",  # banco padrão para conexão inicial
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True  # necessário para executar CREATE DATABASE fora de uma transação
    cursor = conn.cursor()

    # Cria o banco de dados
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(nome_banco)
    ))

    print(f"Banco de dados '{nome_banco}' criado com sucesso!")

except psycopg2.Error as e:
    print(f"Erro ao criar banco de dados: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()

