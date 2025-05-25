from Model.EditarUserModel import EditarUsuarioModel, EditarSenhaModel
from passlib.hash import sha256_crypt

def VerificarSenhaController(senha_atual_hash,senha_antiga_digitada, senha1, senha2):
    if sha256_crypt.verify(senha_antiga_digitada, senha_atual_hash):
        if senha1 == senha2:
            return True
        else:
            print("As novas senhas não coincidem.")
            return False
    else:
        print("Senha antiga incorreta.")
        return False
    
def EditarSenhaController(matricula, senha, tabela):
    try:
        if matricula and senha:
            senha_hash = sha256_crypt.hash(senha)
            sucesso = EditarSenhaModel(matricula, senha_hash, tabela)
            if sucesso:
                print("Senha editada com sucesso!")
                return True
            else:
                return False
        else:
            print("Matricula ou senha não fornecidos.")
            return False
    except Exception as e:
        print(f"Erro ao editar senha: {e}")
        return False  

def EditarUserController(matricula, nome, email, cpf, tabela,):
    try:        
        if matricula and nome and email and cpf:
            sucesso = EditarUsuarioModel(matricula, nome, email,cpf, tabela)
            if sucesso:
                print("Dados editados com sucesso!")
                return True
            else:
                print("Erro ao editar dados.")
                return False
        else:
            print("Matricula, nome, email ou cpf não fornecidos.")
            return False
    except Exception as e:
        print(f"Erro ao editar usuário: {e}")
        return False







