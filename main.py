from cnx import conectar, criar_tabela_aluno, criar_tabela_disciplinas
from View.TelaLogin import TelaLogin 

if __name__ == "__main__":
    app = TelaLogin()

conectar()
#criar_tabela_aluno()
#criar_tabela_disciplinas()
  