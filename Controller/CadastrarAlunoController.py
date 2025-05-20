from Model.CadastrarAlunoModel import CadastrarAlunoModel

def CadastrarAlunoController(cpf,email,senha,nome,data_nascimento):
    try:
        dados = CadastrarAlunoModel(cpf,email,senha,nome,data_nascimento)
        if dados:
            return dados  # cadastro OK
        return None  # cadastro falhou
    except Exception as e:
        print(f"Erro no cadastro: {e}")
        return None
    