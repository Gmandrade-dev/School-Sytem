import psycopg2

cnx= {
    'host': 'ballast.proxy.rlwy.net',
    'dbname': 'railway',
    'user': 'postgres',
    'password': 'TPuBdQJuTZkbhXrXNmgTXHNFIdMDUHUN',
    'port': 57581
}

def conectar():
    try:
        connectando= psycopg2.connect(**cnx)
        connectando.autocommit = True
        print("Conexão estabelecida com sucesso!")
        return connectando
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


conectar()