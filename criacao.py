import psycopg2

host = 'localhost'
user = 'postgres'      
password = 'admin@'    
port = 5432

# Etapa 1: Conecta ao banco ao banco 'db_escola'
try:
    conexao_inicial = psycopg2.connect(
        host=host,
        dbname='postgres',   # nosso banco geral que permite criar outros bancos
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

# Etapa 2: Conecta ao banco para criar as tabelas'
def conectar():
    try:
        connectando = psycopg2.connect(
            host=host,
            dbname='db_escola',   # nosso banco que criamos
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

# Etapa 3: criar as tabelas no banco 'db_escola'
def criar_tabela_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table aluno (
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
    


def criar_tabela_professor():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table professor (
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
    


def criar_tabela_disciplina():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table disciplina (
                id_disciplina serial primary key,
                nome varchar(100) not null,
                matricula_professor int not null,
                foreign key (matricula_professor) references professor(matricula) on delete cascade
            )
        ''')
        print("Tabela 'disciplina' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")
    


def criar_tabela_aluno_disciplina():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table aluno_disciplina (
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
    


def criar_tabela_nota():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            create table nota (
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



# Etapa 4: Inserir dados em aluno e professor
def inserir_dados_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO aluno (matricula, cpf, nome, email, senha, status) VALUES
                ('1', '12345678901', 'João Silva', 'joao@gmail.com', 'aluno', true),
                ('2', '12345678902', 'Patrick Kobi', 'kobi@gmail.com', 'kobi', true),
                ('3', '12345678903', 'Yuri Berna', 'yuri@gmail.com', 'yuri', true),
                ('4', '12345678904', 'Guilherme Barbosa', 'barbosa@gmail.com', 'barbosa', true),
                ('5', '12345678905', 'Osvaldo Neto', 'neto@gmail.com', 'neto', true),
                ('6', '12345678906', 'Arlindo Neto', 'neto2@gmail.com', 'neto2', true),
                ('7', '123456789014', 'Aluno Teste', 'aluno@gmail.com', '123456', true);
        ''')
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_dados_professor():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO professor (matricula, cpf, nome, email, senha, status) VALUES
                ('1', '12345678901', 'João Santos', 'santos@gmail.com', 'joao', true),
                ('2', '12345678902', 'Walter Kobi', 'walter@gmail.com', 'kobi123', true),
                ('3', '12345678903', 'Yuri Olavo', 'olavo@gmail.com', 'yuri123', true),
                ('4', '12345678904', 'Guilherme Andrade', 'gui@gmail.com', 'barbosa123', true),
                ('5', '12345678905', 'Sobrinho Neto', 'neto3@gmail.com', 'neto123', true),
                ('6', '12345678906', 'Arlindo Neto', 'arlindo2@gmail.com', 'neto321', true),
                ('7', '123456789014', 'Professor Teste', 'professor@gmail.com', '123456', true);
        ''')
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")


# Etapa 5: criar todas as tabelas e inserir dados iniciais
criar_tabela_aluno()   
criar_tabela_professor()
criar_tabela_disciplina()
criar_tabela_aluno_disciplina()
criar_tabela_nota()
print("Todas as tabelas criadas com sucesso!")
inserir_dados_aluno()
inserir_dados_professor()
print("Dados iniciais inseridos com sucesso!")




