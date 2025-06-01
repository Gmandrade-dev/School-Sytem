from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from Controller.CadastrarController import CadastrarDisciplinaController


def CadastroDisciplinaFrame(gestao_tab, callback_logou):
    def cadastrar_disciplina():
        nome = nomeDisciplina.get().strip()
        matricula = matricula_prof.get().strip()

        status, mensagem = CadastrarDisciplinaController(nome, matricula)

        if status:
            messagebox.showinfo("Sucesso", mensagem)
            nomeDisciplina.delete(0, 'end')
            matricula_prof.delete(0, 'end')
        else:
            messagebox.showerror("Erro", mensagem)

    # Linha do título
    linha1 = ctk.CTkFrame(gestao_tab)
    linha1.pack(pady=5)

    titulo = ctk.CTkLabel(linha1, text="Cadastro de Disciplinas", font=("Arial", 18, "bold")) 
    titulo.pack(side="left", padx=5, pady=5)

    # Linha dos campos e botão
    linha2 = ctk.CTkFrame(gestao_tab)
    linha2.pack(pady=5)

    nomeDisciplina = ctk.CTkEntry(linha2, placeholder_text="Nome da Disciplina", height=40, width=180)
    nomeDisciplina.pack(side="left", pady=5, padx=5)

    matricula_prof = ctk.CTkEntry(linha2, placeholder_text="Matrícula do Professor", height=40, width=180)
    matricula_prof.pack(side="left", pady=5, padx=5)

    botao_cadastrar = ctk.CTkButton(linha2, text="Cadastrar", height=40, command=cadastrar_disciplina)
    botao_cadastrar.pack(side="left", pady=5, padx=5)
