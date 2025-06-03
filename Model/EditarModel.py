from Model.cnx import conectar

def EditarDisciplinaModel(id_disciplina, nome, matricula_professor):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = """
            UPDATE disciplina 
            SET nome = %s, matricula_professor = %s 
            WHERE id_disciplina = %s
        """
        cursor.execute(query, (nome, matricula_professor, id_disciplina))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao editar disciplina: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def EditarNotaModel(id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3):
    conn = None
    cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = """
            UPDATE nota 
            SET nota1 = %s, nota2 = %s, nota3 = %s 
            WHERE id_nota = %s AND matricula_aluno = %s AND id_disciplina = %s
        """
        cursor.execute(query, (nota1, nota2, nota3, id_nota, matricula_aluno, id_disciplina))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao editar nota: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


