from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox

def TelaCadastrar(cadastro_tab, dados,user_nivel,callback_logou):

    # Título
    titulo = ctk.CTkLabel(cadastro_tab, text="Cadastro", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    # Campo Nome
    entrada_nome = ctk.CTkEntry(cadastro_tab, placeholder_text="Nome completo")
    entrada_nome.pack(pady=10)

    # Campo CPF
    entrada_cpf = ctk.CTkEntry(cadastro_tab, placeholder_text="CPF (somente números)")
    entrada_cpf.pack(pady=10)

    # Campo Email
    entrada_email = ctk.CTkEntry(cadastro_tab, placeholder_text="Email")
    entrada_email.pack(pady=10)

    # Campo Senha
    entrada_senha = ctk.CTkEntry(cadastro_tab, placeholder_text="Senha", show="*")
    entrada_senha.pack(pady=10)

    tipo= CTkComboBox(cadastro_tab, values=["Aluno", "Professor"], placeholder_text="Selecione o tipo de usuário")
    tipo.set("Selecione o tipo de usuário")
    tipo.pack(pady=10)

    # Função do botão
    def cadastrar():
        nome = entrada_nome.get()
        cpf = entrada_cpf.get()
        email = entrada_email.get()
        senha = entrada_senha.get()
        tipo_usuario = tipo.get()
        


    # Botão de Cadastro
    botao_cadastrar = ctk.CTkButton(cadastro_tab, text="Cadastrar", command=cadastrar)
    botao_cadastrar.pack(pady=20)

