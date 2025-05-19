from Model.LoginModel import LoginModel

def LoginController(nome, senha, nivel):
    try:
        dados = LoginModel(nome, senha, nivel)
        if dados:
            if nivel.lower() in ["aluno", "professor"]:
                return dados  # login OK
        return None  # login falhou
    except Exception as e:
        print(f"Erro no login: {e}")
        return None
