from Model.EditarModel import EditarDisciplinaModel,EditarNotaModel

def EditarDisciplinaController(id_disciplina, nome, matricula_professor):
    try:

        if not id_disciplina or not nome or not matricula_professor:
            return False, "Todos os campos são obrigatórios."
        nome = str(nome).strip()
        matricula_professor = int(str(matricula_professor).strip())

        result = EditarDisciplinaModel(id_disciplina, nome.strip(), matricula_professor)
        if result:
            return True, "Disciplina editada com sucesso."
        else:
            return False, "Erro ao editar disciplina. Verifique os dados e tente novamente."

    except Exception as e:
        return False, f"Erro ao editar disciplina: {str(e)}"

    
    
def EditarNotaController(id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3):
    try:
        if id_nota is None or matricula_aluno is None or id_disciplina is None or nota1 is None:
            return False, "Todos os campos obrigatórios devem ser preenchidos."
        
        try:
            id_nota = int(str(id_nota).strip())
            matricula_aluno = int(str(matricula_aluno).strip())
            id_disciplina = int(str(id_disciplina).strip())
        except ValueError:
            return False, "ID da nota, matrícula do aluno e ID da disciplina devem ser números inteiros."

        try:
            nota1 = float(str(nota1).strip())
        except ValueError:
            return False, "Nota 1 deve ser um número decimal."

        try:
            nota2 = float(str(nota2).strip()) if nota2 is not None and str(nota2).strip() != "" else 0.0
        except ValueError:
            return False, "Nota 2 deve ser um número decimal."

        try:
            nota3 = float(str(nota3).strip()) if nota3 is not None and str(nota3).strip() != "" else 0.0
        except ValueError:
            return False, "Nota 3 deve ser um número decimal."

        result = EditarNotaModel(id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3)

        if result:
            return True, "Nota editada com sucesso."
        else:
            return False, "Erro ao editar nota. Verifique os dados e tente novamente."
        
    except Exception as e:
        print(f"Erro ao editar nota: {e}")
        return False, f"Erro ao editar nota: {str(e)}"

