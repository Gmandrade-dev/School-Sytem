from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox

# Configurações iniciais
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul escuro

# Criar a janela principal
janela = CTk()
janela.geometry("400x500")
janela.title("Cadastro de Usuário")

# Título
titulo = ctk.CTkLabel(janela, text="Cadastro", font=("Arial", 24, "bold"))
titulo.pack(pady=20)

# Campo Nome
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Nome completo")
entrada_nome.pack(pady=10)

# Campo CPF
entrada_cpf = ctk.CTkEntry(janela, placeholder_text="CPF (somente números)")
entrada_cpf.pack(pady=10)

# Campo Email
entrada_email = ctk.CTkEntry(janela, placeholder_text="Email")
entrada_email.pack(pady=10)

# Campo Senha
entrada_senha = ctk.CTkEntry(janela, placeholder_text="Senha", show="*")
entrada_senha.pack(pady=10)

# Campo Data de Nascimento
entrada_data = ctk.CTkEntry(janela, placeholder_text="Data de Nascimento (DD/MM/AAAA)")
entrada_data.pack(pady=10)

# Função do botão
def cadastrar():
    nome = entrada_nome.get()
    cpf = entrada_cpf.get()
    email = entrada_email.get()
    senha = entrada_senha.get()
    data_nasc = entrada_data.get()

    mensagem = f"Nome: {nome}\nCPF: {cpf}\nEmail: {email}\nSenha: {senha}\nNascimento: {data_nasc}"
    messagebox.showinfo("Cadastro Realizado", mensagem)

# Botão de Cadastro
botao_cadastrar = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=20)

# Iniciar a interface
janela.mainloop()
