import psycopg2


# 🔗 Conexão com o banco
def conectar():
    return psycopg2.connect(
        host="ballast.proxy.rlwy.net",
        database="railway",
        user="postgres",
        password="TPuBdQJuTZkbhXrXNmgTXHNFIdMDUHUN",
        port="57581"
    )

def buscar_todos():
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT matricula, nome, email FROM aluno;")
        dados = cur.fetchall()

        cur.close()
        conn.close()

        return dados
    except Exception as e:
        print(f"Erro ao buscar todos: {e}")
        return None
    
def buscar_por_matricula(matricula):
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("SELECT matricula, nome, email FROM aluno WHERE matricula = %s;", (matricula,))
        dados = cur.fetchall()

        cur.close()
        conn.close()

        return dados
    except Exception as e:
        print(f"Erro ao buscar matrícula: {e}")
        return None

def editar_usuario(matricula, novo_nome, novo_email):
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(
            "UPDATE aluno SET nome = %s, email = %s WHERE matricula = %s;",
            (novo_nome, novo_email, matricula)
        )
        conn.commit()

        cur.close()
        conn.close()

        return True
    except Exception as e:
        print(f"Erro ao editar: {e}")
        return False

def deletar_usuario(matricula):
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("DELETE FROM aluno WHERE matricula = %s;", (matricula,))
        conn.commit()

        cur.close()
        conn.close()

        return True
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        return False

def cadastrar_usuario(matricula, nome, email):
    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO aluno (matricula, nome, email) VALUES (%s, %s, %s);",
            (matricula, nome, email)
        )
        conn.commit()

        cur.close()
        conn.close()

        return True
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
        return False
