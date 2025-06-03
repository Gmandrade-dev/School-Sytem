from Model.ListarModel import ExibirProfAluno

    
def ExibirUm(tabela,busca):
    try:
        if not tabela:
            return False
        resultado = ExibirProfAluno(tabela,busca)
        if resultado:
            return resultado
        else:
            return False
    except Exception as e:
        print(f"Erro ao exibir: {e}")
        return False