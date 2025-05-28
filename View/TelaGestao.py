from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from Controller.CadastrarController import CadastrarUserController  # importe seu controller corretamente

def TelaGestao(gestao_tab, dados, user_nivel, callback_logou):

    # Título
    titulo = ctk.CTkLabel(gestao_tab, text="Cadastro", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    # Campo Nome
    entrada_nome = ctk.CTkEntry(gestao_tab, placeholder_text="Nome completo", height=50, width=200)
    entrada_nome.pack(side="left",pady=10)

    # Campo CPF
    entrada_cpf = ctk.CTkEntry(gestao_tab, placeholder_text="CPF (somente números)", height=50, width=200)
    entrada_cpf.pack(side="left",pady=10)

    # Campo Email
    entrada_email = ctk.CTkEntry(gestao_tab, placeholder_text="Email", height=50, width=200)
    entrada_email.pack(side="left",pady=10)

    # Campo Senha
    entrada_senha = ctk.CTkEntry(gestao_tab, placeholder_text="Senha", show="*", height=50, width=200)
    entrada_senha.pack(side="left",pady=10)
   

    #
    botao_cadastrar = ctk.CTkButton(gestao_tab, text="Cadastrar", height=50)
    botao_cadastrar.pack(pady=20)
