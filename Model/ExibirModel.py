from Model.cnx import conectar

def ExibirAllModel(tabela):
    try:
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute(f"SELECT * FROM {tabela} limit 20")
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

def ExibirOneModel(tabela, id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        if tabela == "disciplina":
            cursor.execute(f"SELECT * FROM {tabela} WHERE matricula_professor = %s", (id,))
        elif tabela == "nota":
            cursor.execute(f"SELECT * FROM {tabela} WHERE matricula_aluno = %s", (id,))
        else:
            return False
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        if resultado:
            # print(f"Dados exibidos da tabela {tabela} para o aluno {id}: {resultado}")
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir dados específicos: {e}")
        return False

