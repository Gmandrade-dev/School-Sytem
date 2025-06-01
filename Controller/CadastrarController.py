from Model.CadastrarModel import CadastrarAlunoModel, CadastrarProfessorModel, VerificarUserModel, CadastrarNotasModel,CadastrarDisciplinaModel,VerificarUserExistsModel,VerificarDisciplinaExistsModel
from passlib.hash import sha256_crypt

def VerificarUserController(email):
    try:
        if not email:
            print("Email não pode ser vazio!")
            return False, "Email não pode ser vazio!"

        result = VerificarUserModel(email)

        if result:
            return True, "Usuário já cadastrado."
        else:
            return False, "Usuário não cadastrado."

    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False, f"Erro ao verificar usuário: {e}"


def CadastrarUserController(nome, email, senha, cpf, tipo_usuario):
    try:
        if nome == "" or email == "" or senha == "" or cpf == "" or tipo_usuario == "" or tipo_usuario == "Selecione o tipo de usuário":
            print("Preencha todos os campos!")
            return False, "Preencha todos os campos!"

        if len(cpf) != 11:
            print("CPF deve ter 11 dígitos!")
            return False, "CPF deve ter 11 dígitos!"

        existe, msg = VerificarUserController(email)
        if existe:
            print(msg)
            return False, msg

        senha_hash = sha256_crypt.hash(senha)

        if tipo_usuario == "Aluno":
            sucesso = CadastrarAlunoModel(nome, email, senha_hash, cpf)
        elif tipo_usuario == "Professor":
            sucesso = CadastrarProfessorModel(nome, email, senha_hash, cpf)
        else:
            print("Tipo de usuário inválido!")
            return False, "Tipo de usuário inválido!"

        if sucesso:
            return True, "Usuário cadastrado com sucesso!"
        else:
            return False, "Erro ao cadastrar usuário."

    except Exception as e:
        print(f"Erro no cadastro: {e}")
        return False, f"Erro no cadastro: {e}"

# # Controller para cadastrar disciplina e notas

    
def CadastrarDisciplinaController(nome, matricula_prof):
    try:
        if not nome or not matricula_prof:
            return False, "Preencha todos os campos."

        if not VerificarUserExists("professor", matricula_prof):
            return False, "Professor não encontrado."

        sucesso = CadastrarDisciplinaModel(nome, matricula_prof)

        if sucesso:
            return True, "Disciplina cadastrada com sucesso!"
        else:
            return False, "Erro ao cadastrar disciplina."

    except Exception as e:
        return False, f"Erro interno ao cadastrar disciplina: {e}"


def CadastrarNotasController(matricula, disciplina, av1, av2, av3):
    try:
        if not matricula or not disciplina or av1 is None:
            return False, "Preencha a matrícula, disciplina e a nota AV1."

        if not VerificarUserExists("aluno", matricula):
            return False, "Aluno não encontrado."

        if not VerificarDisciplinaExists(disciplina):
            return False, "Disciplina não encontrada."

        sucesso = CadastrarNotasModel(matricula, disciplina, av1, av2, av3)

        if sucesso:
            return True, "Notas lançadas com sucesso!"
        else:
            return False, "Erro ao cadastrar as notas."

    except Exception as e:
        return False, f"Erro interno ao lançar notas: {e}"


def VerificarUserExists(tabela, matricula):
    try:
        if not matricula or not tabela:
            return False

        sucesso = VerificarUserExistsModel(tabela, matricula)
        return bool(sucesso)

    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False


def VerificarDisciplinaExists(id_disciplina):
    try:
        if not id_disciplina:
            return False

        sucesso = VerificarDisciplinaExistsModel(id_disciplina)
        return bool(sucesso)

    except Exception as e:
        print(f"Erro ao verificar disciplina: {e}")
        return False