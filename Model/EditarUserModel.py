from Model.cnx import conectar
def EditarUsuarioModel(matricula, nome, email,cpf, tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"UPDATE {tabela} SET nome = %s, email = %s, cpf = %s WHERE matricula = %s", (nome,email,cpf,matricula))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    except Exception as e:
        print(f"Erro ao editar dados: {e}")
        return False
def EditarSenhaModel(matricula, senha, tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"UPDATE {tabela} SET senha = %s WHERE matricula = %s", (senha,matricula))
        conn.commit()
        cursor.close()
        conn.close()
        # print("Senha editada com sucesso!")
        return True
        
    except Exception as e:
        print(f"Erro ao editar senha: {e}")
        return False