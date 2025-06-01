from Model.ExibirModel import ExibirAllModel

    
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