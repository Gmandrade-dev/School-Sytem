from cnx import conectar
from passlib.hash import sha256_crypt

def CadastrarAlunoModel(nome,email,senha,nascimento,cpf):
    try:
        senhahash = sha256_crypt.hash(senha)
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO aluno (nome,email,senha,data_nascimento,cpf) VALUES (%s,%s,%s,%s,%s)", (nome,email,senhahash,nascimento,cpf))
        conn.commit()
        cursor.close()
        conn.close()
        print("Cadastro realizado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")
        return False
    
CadastrarAlunoModel("Guilherme","teste2@gmail.com","123","2000-01-01","15187846388")    