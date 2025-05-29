from customtkinter import *
from Model.cnx import conectar
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