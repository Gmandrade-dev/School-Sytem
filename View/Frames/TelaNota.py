from customtkinter import *
from Model.NotaModel import listar_notas
import customtkinter as ctk
from tkinter import messagebox


def limpar_frame_lista(container):
        for widget in container.winfo_children():
            widget.destroy()

def TelaNota(notas_tab, dados): # Função para criar a tela de consulta de notas do aluno
    
    def mostrar_notas(): # Função para mostrar as notas do aluno logado

        limpar_frame_lista(janela_busca) # Limpa o frame antes de mostrar os dados do aluno

        matricula_id = dados[0] # Pega a matrícula do aluno que está logado

        if not isinstance(matricula_id, int): # Verifica se o valor do entry é um número inteiro
            messagebox.showinfo("Consulta", "Digite uma matrícula válida.")
            return

        resultado = listar_notas(matricula_id) # Chama a função listar_notas passando a matrícula do aluno

        if not resultado:
            messagebox.showinfo("Consulta", "Nenhuma nota encontrada.")
            return

        headers = ["NOME DO ALUNO", "DISCIPLINA", "NOTA 1", "NOTA 2", "NOTA 3", "MÉDIA"] # TITULOS DAS COLUNAS
        for col, texto in enumerate(headers):
            label = ctk.CTkLabel(janela_busca, text=texto, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=(5, 10))

        for idx, (nome_aluno, nome_disciplina, nota1, nota2, nota3, media) in enumerate(resultado, start=1): # Itera sobre os resultados retornados pela função listar_notas
        # Entrys

            entry_matricula = ctk.CTkEntry(janela_busca, width=120, height=42)
            entry_matricula.insert(0, nome_aluno)  # RETORNA O NOME DO ALUNO
            entry_matricula.configure(state="readonly")  # Nome do aluno não pode ser alterado
            entry_matricula.grid(row=idx, column=0, padx=5, pady=5)

            entry_id_disciplina = ctk.CTkEntry(janela_busca, width=200, height=42)
            entry_id_disciplina.insert(0, nome_disciplina) # RETORNA O NOME DA DISCIPLINA
            entry_id_disciplina.configure(state="readonly") # Não pode ser alterado
            entry_id_disciplina.grid(row=idx, column=1, padx=5, pady=5)

            entry_nota1 = ctk.CTkEntry(janela_busca, width=60, height=42)
            entry_nota1.insert(0, nota1) # RETORNA A NOTA 1
            entry_nota1.grid(row=idx, column=2, padx=5, pady=5)

            entry_nota2 = ctk.CTkEntry(janela_busca, width=60, height=42)
            entry_nota2.insert(0, nota2) # RETORNA A NOTA 2
            entry_nota2.grid(row=idx, column=3, padx=5, pady=5)

            entry_nota3 = ctk.CTkEntry(janela_busca, width=60, height=42)
            entry_nota3.insert(0, nota3) # RETORNA A NOTA 3
            entry_nota3.grid(row=idx, column=4, padx=5, pady=5)

            entry_media = ctk.CTkEntry(janela_busca, width=60, height=42)
            entry_media.insert(0, media) # RETORNA A MÉDIA
            entry_media.grid(row=idx, column=5, padx=5, pady=5)

    #INTERFACE DA TELA DE CONSULTA

    container = ctk.CTkFrame(notas_tab) # CRIA UM FRAME PARA A TELA DE CONSULTA
    container.pack(expand=True, fill="both" )

    titulo = CTkLabel(container, text="Consulta de Notas", font=("Calibri", 24))
    titulo.pack(padx=5, pady=25)

    botao_buscar = ctk.CTkButton(container, text="Ver Notas",height=40, command=mostrar_notas) # BOTÃO PARA BUSCAR AS NOTAS DO ALUNO
    botao_buscar.pack(pady=10)

    janela_busca = ctk.CTkScrollableFrame(container) # CRIA UM FRAME SCROLLABLE PARA MOSTRAR AS NOTAS DO ALUNO
    janela_busca.pack(expand=True, fill="both", padx=20, pady=20)