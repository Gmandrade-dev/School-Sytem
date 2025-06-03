from Model.cnx import conectar

def ExibirAllModel(tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela} limit 30")
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        if resultado:
            #print(f"Dados exibidos da tabela {tabela}: {resultado}")
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir dados selecionados: {e}")
        return False


def PesquisarNotaModel(matricula_aluno):
    try:
        conn = conectar()
        cursor = conn.cursor()

        query = """
            SELECT id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3, media
            FROM notas
            WHERE matricula_aluno = %s
        """

        cursor.execute(query, (matricula_aluno,))
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        if resultado:
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao pesquisar nota: {e}")
        return False
