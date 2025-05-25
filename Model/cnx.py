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
        connectando = psycopg2.connect(**cnx)
        connectando.autocommit = True
        print("ConexÃ£o estabelecida com sucesso!")
        return connectando
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def criar_tabela_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                matricula SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                cpf VARCHAR(100),
                email VARCHAR(100),
                senha VARCHAR(100)
            )
        ''')
        print("Tabela 'alunos' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()


def criar_tabela_disciplinas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS disciplinas (
                id_disciplina SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                descricao TEXT
            )
        ''')
        print("Tabela 'cursos' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()




# criar_tabela_aluno()