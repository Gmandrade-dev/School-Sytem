from Model.CadastrarModel import CadastrarAlunoModel, CadastrarProfessorModel, VerificarUserModel
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
