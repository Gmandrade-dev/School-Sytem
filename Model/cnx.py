import psycopg2

bdlocal= {
    'host': 'localhost',
    'dbname': 'db_escola',
    'user': 'postgres',
    'password': 'admin@',
    'port': 5432
}
bdonline = {
    'host': 'ballast.proxy.rlwy.net',
    'dbname': 'railway',
    'user': 'postgres',
    'password': 'TPuBdQJuTZkbhXrXNmgTXHNFIdMDUHUN',
    'port': 57581
}


def conectar():
    try:
        connectando = psycopg2.connect(**bdlocal)
        connectando.autocommit = True
        #print("Conexão estabelecida com sucesso!")
        return connectando
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


def criar_tabela_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table IF NOT EXISTS aluno (
                matricula serial primary key,
                cpf varchar(14) unique not null,
                nome varchar(100) not null,
                email varchar(100) unique not null,
                senha varchar(100) not null,
                status boolean default true
            )
        ''')
        print("Tabela 'aluno' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()


def criar_tabela_disciplina():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table IF NOT EXISTS disciplina (
                id_disciplina serial primary key,
                nome varchar(100) not null,
                matricula_professor int not null,
                foreign key (matricula_professor) references professor(matricula) on delete cascade
            )
        ''')
        print("Tabela 'disciplina' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()


def criar_tabela_professor():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table IF NOT EXISTS professor (
                matricula serial primary key,
                cpf varchar(14) unique not null,
                nome varchar(100) not null,
                email varchar(100) unique not null,
                senha varchar(100) not null,
                status boolean default true
            )
        ''')
        print("Tabela 'professor' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()


def criar_tabela_aluno_disciplina():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table IF NOT EXISTS aluno_disciplina (
                id_aluno_disciplina serial primary key,
                matricula_aluno int not null,
                id_disciplina int not null,
                foreign key (matricula_aluno) references aluno(matricula) on delete cascade,
                foreign key (id_disciplina) references disciplina(id_disciplina) on delete cascade,
                unique (matricula_aluno, id_disciplina)
            )
        ''')
        print("Tabela 'aluno_disciplina' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()


def criar_tabela_nota():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table IF NOT EXISTS nota (
                id_nota serial primary key,
                matricula_aluno int not null,
                id_disciplina int not null,
                nota1 numeric(5,2),
                nota2 numeric(5,2),
                nota3 numeric(5,2),
                media numeric(5,2) generated always as 
                ((coalesce(nota1, 0) + coalesce(nota2, 0) + coalesce(nota3, 0)) / 3) stored,
                foreign key (matricula_aluno) references aluno(matricula) on delete cascade,
                foreign key (id_disciplina) references disciplina(id_disciplina) on delete cascade,
                unique (matricula_aluno, id_disciplina)
            )
        ''')
        print("Tabela 'nota' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    finally:
        cursor.close()



