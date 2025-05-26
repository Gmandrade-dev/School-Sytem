from Model.CadastrarModel import CadastrarAlunoModel, CadastrarProfessorModel
from passlib.hash import sha256_crypt

def CadastrarUserController(nome,email,senha,cpf, tipo_usuario):
    try:
        if (nome == "" or email == "" or senha == "" or cpf == "" or tipo_usuario == "" or tipo_usuario == "Selecione o tipo de usuário"):
            print("Preencha todos os campos!")
            return False,"Preencha todos os campos!"
        if (len(cpf) != 11):
            print("CPF deve ter 11 dígitos!")
            return False,"CPF deve ter 11 dígitos!"
        senha_hash = sha256_crypt.hash(senha)
        if (tipo_usuario == "Aluno"):
            return CadastrarAlunoModel(nome, email, senha, cpf)
        elif (tipo_usuario == "Professor"):

        
    except Exception as e:
        print(f"Erro no cadastro: {e}")
        return None
    