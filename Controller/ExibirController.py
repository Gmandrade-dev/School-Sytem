from Model.ExibirModel import ExibirAllModel, ExibirOneModel

    
def ExibirAllController(tabela):
    try:
        if not tabela:
            return False
        resultado = ExibirAllModel(tabela)
        if resultado:
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir notas: {e}")
        return False
    

    

def ExibirOneController(tabela, id_aluno):
    try:
        if not tabela or id_aluno is None or isinstance(id_aluno, (str,float)):
            return False

        resultado = ExibirOneModel(tabela, id_aluno)
        if resultado:
            # print(f"Dados exibidos da tabela {tabela} para o aluno {id_aluno}: {resultado}")
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir nota específica: {e}")
        return False