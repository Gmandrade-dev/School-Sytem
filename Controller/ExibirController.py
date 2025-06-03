from Model.ExibirModel import ExibirAllModel,PesquisarNotaModel

    
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
    

def PesquisarNotaController(matricula_aluno):
    try:
        dados = PesquisarNotaModel(matricula_aluno)
        return dados
    except Exception as e:
        print(f"Erro no Controller ao pesquisar nota: {e}")
        return False
