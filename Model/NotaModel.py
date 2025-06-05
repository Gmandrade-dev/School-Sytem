from customtkinter import *
from Model.cnx import conectar
from tkinter import messagebox


def listar_notas(matricula_aluno):
    """
    Função para listar todas as notas de um aluno, incluindo o nome da disciplina.
    """
    cnx = conectar()
    cursor = cnx.cursor()
    query = """
        SELECT a.nome AS nome_aluno, d.nome AS nome_disciplina, n.nota1, n.nota2, n.nota3, n.media FROM nota n
        JOIN disciplina d ON n.id_disciplina = d.id_disciplina
        JOIN aluno a ON n.matricula_aluno = a.matricula
        WHERE n.matricula_aluno = %s
    """
    cursor.execute(query, (matricula_aluno,))
    resultado = cursor.fetchall()

    cursor.close()
    cnx.close()
    
    return resultado if resultado else None
