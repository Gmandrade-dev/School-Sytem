from Model.cnx import conectar
from passlib.hash import sha256_crypt

def LoginModel(email,senha,tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"SELECT matricula,cpf,email,senha,nome FROM {tabela} WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        if usuario:
            print(usuario)
            senha_hash = usuario[3]
            if sha256_crypt.verify(senha,senha_hash):
                                
                return usuario
            else:
                
                return False
            
    except Exception as e:
        print(f"Erro ao verificar login: {e}")
        return False
    


