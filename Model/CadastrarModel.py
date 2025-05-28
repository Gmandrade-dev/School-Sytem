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
