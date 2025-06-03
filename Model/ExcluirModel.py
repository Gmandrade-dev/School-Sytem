from Model.cnx import conectar

def ExcluirNotaModel(id_nota):
    try:
        con=conectar()
        cursor=con.cursor()
        cursor.execute(f"DELETE FROM nota WHERE id_nota =%s", (id_nota,))
        con.commit()
        cursor.close()
        con.close()
        # print(f"Nota com ID {id_nota} excluída com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao excluir nota: {e}")
        return False
    
def ExcluirDisciplinaModel(id_disciplina):
    try:
        con=conectar()
        cursor=con.cursor()
        cursor.execute(f"DELETE FROM disciplina WHERE id_disciplina =%s", (id_disciplina,))
        con.commit()
        cursor.close()
        con.close()
        # print(f"Disciplina com ID {id_disciplina} excluída com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao excluir disciplina: {e}")
        return False