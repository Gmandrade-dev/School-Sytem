from Model.ExcluirModel import ExcluirNotaModel,ExcluirDisciplinaModel

def ExcluirNotaController(id_nota):
    try:
        if not id_nota:
            return False
        resultado = ExcluirNotaModel(id_nota)
        if resultado:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao excluir nota: {e}")
        return False
def ExcluirDisciplinaController(id_disciplina):
    try:
        if not id_disciplina:
            return False
        resultado = ExcluirDisciplinaModel(id_disciplina)
        if resultado:
            return True
        else:
            return False
    except Exception as e:
        print(f"Erro ao excluir disciplina: {e}")
        return False