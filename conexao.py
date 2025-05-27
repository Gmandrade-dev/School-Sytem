import psycopg2
import pandas as pd

# Configurações para conectar ao banco padrão (postgres), que permite criar outros bancos
host = 'localhost'
user = 'postgres'      # substitua pelo seu usuário do PostgreSQL
password = 'admin@'    # substitua pela sua senha
port = 5432
 
# Função para conectar ao banco de dados db_escola
def conectar():
    try:
        connectando = psycopg2.connect(
            host=host,
            dbname='db_escola',   # banco padrão que permite criar outros
            user=user,
            password=password,
            port=port
        )
        connectando.autocommit = True
        print("Conexão estabelecida com sucesso!")
        return connectando
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None



