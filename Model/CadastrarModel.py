from Model.cnx import conectar


def CadastrarUserModel(nome,email,senha,cpf, tipo_usuario):
    try:
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
    
