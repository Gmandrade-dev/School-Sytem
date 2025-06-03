import random
import faker
from criacao import conectar, inserir_dados_professor, inserir_dados_aluno

fake = faker.Faker('pt_BR')

# Inserir múltiplos professores
def inserir_varios_professores(qtd=20):
    for i in range(qtd):
        nome = fake.name()
        email = f"prof{i+1}@escola.com"
        senha = "123"
        cpf = fake.cpf()
        inserir_dados_professor(nome, email, senha, cpf)

# Inserir múltiplos alunos
def inserir_varios_alunos(qtd=100):
    for i in range(qtd):
        nome = fake.name()
        email = f"aluno{i+1}@escola.com"
        senha = "123"
        cpf = fake.cpf()
        inserir_dados_aluno(nome, email, senha, cpf)

# Inserir disciplinas
def inserir_disciplinas(qtd=20):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        for i in range(1, qtd + 1):
            nome_disciplina = f"Disciplina {i}"
            matricula_professor = ((i - 1) % 20) + 1  # Distribui entre 20 professores
            cursor.execute(
                "INSERT INTO disciplina (nome, matricula_professor) VALUES (%s, %s)",
                (nome_disciplina, matricula_professor)
            )
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"{qtd} disciplinas inseridas com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir disciplinas: {e}")

# Inserir relações aluno_disciplina e notas
def inserir_aluno_disciplina_e_nota():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        # Pega os alunos e disciplinas existentes
        cursor.execute("SELECT matricula FROM aluno")
        alunos = [a[0] for a in cursor.fetchall()]

        cursor.execute("SELECT id_disciplina FROM disciplina")
        disciplinas = [d[0] for d in cursor.fetchall()]

        for aluno in alunos:
            disciplinas_escolhidas = random.sample(disciplinas, 5)
            for disciplina in disciplinas_escolhidas:
                # Inserir na tabela aluno_disciplina
                cursor.execute(
                    "INSERT INTO aluno_disciplina (matricula_aluno, id_disciplina) VALUES (%s, %s)",
                    (aluno, disciplina)
                )
                # Gerar notas aleatórias entre 0 e 10
                nota1 = round(random.uniform(5, 10), 2)
                nota2 = round(random.uniform(5, 10), 2)
                nota3 = round(random.uniform(5, 10), 2)

                # Inserir na tabela nota
                cursor.execute(
                    '''INSERT INTO nota (matricula_aluno, id_disciplina, nota1, nota2, nota3)
                    VALUES (%s, %s, %s, %s, %s)''',
                    (aluno, disciplina, nota1, nota2, nota3)
                )

        conexao.commit()
        cursor.close()
        conexao.close()
        print("Relações aluno_disciplina e notas inseridas com sucesso!")

    except Exception as e:
        print(f"Erro ao inserir aluno_disciplina e notas: {e}")

# Executar as inserções
inserir_varios_professores()
inserir_varios_alunos()
inserir_disciplinas()
inserir_aluno_disciplina_e_nota()

print("População do banco concluída com sucesso!")
