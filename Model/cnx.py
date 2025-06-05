import psycopg2

bdlocal= {
    'host': 'localhost',
    'dbname': 'db_escola',
    'user': 'postgres',
    'password': 'admin@',
    'port': 5432
}
# bdonline = {
#     'host': 'ballast.proxy.rlwy.net',
#     'dbname': 'railway',
#     'user': 'postgres',
#     'password': 'TPuBdQJuTZkbhXrXNmgTXHNFIdMDUHUN',
#     'port': 57581
# }


def conectar():
    try:
        connectando = psycopg2.connect(**bdlocal)
        connectando.autocommit = True
        # print("Conexão estabelecida com sucesso!")
        return connectando
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None



