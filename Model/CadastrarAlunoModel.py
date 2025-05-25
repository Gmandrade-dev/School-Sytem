from Model.cnx import conectar
from passlib.hash import sha256_crypt

def CadastrarAlunoModel(nome,email,senha,cpf):
    try:
        if (nome == "" or email == "" or senha == "" or cpf == ""):
            print("Preencha todos os campos!")
            return False
        if (len(cpf) != 11):
            print("CPF deve ter 11 dígitos!")
            return False
        senhahash = sha256_crypt.hash(senha)
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO aluno (nome,email,senha,cpf) VALUES (%s,%s,%s,%s)", (nome,email,senhahash,cpf))
        conn.commit()
        cursor.close()
        conn.close()
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")
        return False
    
CadastrarAlunoModel("Guilherme","teste@gmail.com","123","18158481845")    