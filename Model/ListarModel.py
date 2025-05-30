from customtkinter import *
from Model.cnx import conectar
from tkinter import messagebox
#import psycopg2

def listar_aluno():
    """Retorna todos os alunos cadastrados"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aluno")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def listar_aluno_um(busca):
    """Retorna todos os alunos cadastrados"""

    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute(f"SELECT * FROM aluno WHERE matricula = %s", [busca]) # Retorna um aluno específico baseado na matrícula, retornando uma tupla com os dados do aluno.

    dados = cursor.fetchone()
    if dados:
        return list(dados)  # converte a tupla em lista
    else:
        messagebox.showinfo("Consulta de Alunos", "Nenhum aluno encontrado.") # Se não encontrar o aluno, exibe uma mensagem
    
    # cursor.close()
    # conn.close()
    
    # return dados

def listar_professor():
    """Retorna todos os professores cadastrados"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM professor")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def listar_nota():
    """Retorna todos as notas cadastradas"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nota")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def listar_disciplina():
    """Retorna todos as disciplinas cadastradas"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM disciplina")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados

def listar_aluno_disciplina():
    """Retorna todos as notas em disciplinas cadastradas"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aluno_disciplina")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return dados