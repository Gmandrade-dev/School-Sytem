from Model.cnx import conectar


def CadastrarAlunoModel(nome, email, senha, cpf):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO aluno (nome, email, senha, cpf) VALUES (%s, %s, %s, %s)",
            (nome, email, senha, cpf)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Cadastro de aluno realizado com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")
        return False


def CadastrarProfessorModel(nome, email, senha, cpf):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO professor (nome, email, senha, cpf) VALUES (%s, %s, %s, %s)",
            (nome, email, senha, cpf)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Cadastro de professor realizado com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar professor: {e}")
        return False


def VerificarUserModel(email):
    try:
        conn = conectar()
        cursor = conn.cursor()

        # Verificar na tabela aluno
        cursor.execute("SELECT * FROM aluno WHERE email = %s", (email,))
        aluno = cursor.fetchone()

        # Verificar na tabela professor
        cursor.execute("SELECT * FROM professor WHERE email = %s", (email,))
        professor = cursor.fetchone()

        cursor.close()
        conn.close()

        if aluno or professor:
            print("Usuário já cadastrado!")
            return True  # Usuário existe
        else:
            print("Usuário não cadastrado!")
            return False  # Usuário não existe

    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False  # Se der erro, retorna False também
    

def CadastrarNotasModel(matricula, disciplina, av1, av2,av3):

    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO nota (matricula_aluno, id_disciplina, nota1, nota2, nota3) VALUES (%s, %s, %s, %s, %s)",
            (matricula, disciplina, av1, av2, av3)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Notas cadastradas com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar notas: {e}")
        return False
def CadastrarDisciplinaModel(nome, matricula_prof):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO disciplina (nome, matricula_professor) VALUES (%s, %s)",
            (nome, matricula_prof)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print("Disciplina cadastrada com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao cadastrar disciplina: {e}")
        return False
def VerificarUserExistsModel(tabela, matricula):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela} WHERE matricula = %s", (matricula,))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        if resultado:
            print(f"Usuário encontrado na tabela {tabela}!")
            return True
        else:
            print(f"Usuário não encontrado na tabela {tabela}.")
            return False
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")

        return False
def VerificarDisciplinaExistsModel(id_disciplina):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT id_disciplina FROM disciplina WHERE id_disciplina = %s", (id_disciplina))
        resultado = cursor.fetchone()
        cursor.close()
        conn.close()
        if resultado:
            print("Disciplina já cadastrada!")
            return True
        else:
            print("Disciplina não cadastrada.")
            return False
    except Exception as e:
        print(f"Erro ao verificar disciplina: {e}")
        return False