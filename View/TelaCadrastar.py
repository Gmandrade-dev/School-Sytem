from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from Controller.CadastrarController import CadastrarUserController  # importe seu controller corretamente

def TelaCadastrar(cadastro_tab, dados, user_nivel, callback_logou):

    # Título
    titulo = ctk.CTkLabel(cadastro_tab, text="Cadastro", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    # Campo Nome
    entrada_nome = ctk.CTkEntry(cadastro_tab, placeholder_text="Nome completo", height=50, width=200)
    entrada_nome.pack(pady=10)

    # Campo CPF
    entrada_cpf = ctk.CTkEntry(cadastro_tab, placeholder_text="CPF (somente números)", height=50, width=200)
    entrada_cpf.pack(pady=10)

    # Campo Email
    entrada_email = ctk.CTkEntry(cadastro_tab, placeholder_text="Email", height=50, width=200)
    entrada_email.pack(pady=10)

    # Campo Senha
    entrada_senha = ctk.CTkEntry(cadastro_tab, placeholder_text="Senha", show="*", height=50, width=200)
    entrada_senha.pack(pady=10)

    # Combobox sem placeholder_text, com valor inicial definido pelo set
    tipo = ctk.CTkComboBox(cadastro_tab, values=["Aluno", "Professor"], height=50, width=200)
    tipo.set("Selecione o tipo")
    tipo.pack(pady=10)

    def cadastrar():
        nome = entrada_nome.get().strip()
        cpf = entrada_cpf.get().strip()
        email = entrada_email.get().strip()
        senha = entrada_senha.get().strip()
        tipo_usuario = tipo.get()

        # Verificação inicial do tipo
        if tipo_usuario == "Selecione o tipo":
            messagebox.showwarning("Aviso", "Por favor, selecione o tipo de usuário.")
            return

        # Chama o controller para validar e cadastrar
        sucesso, mensagem = CadastrarUserController(nome, email, senha, cpf, tipo_usuario)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            # Limpa os campos após sucesso
            entrada_nome.delete(0, 'end')
            entrada_cpf.delete(0, 'end')
            entrada_email.delete(0, 'end')
            entrada_senha.delete(0, 'end')
            tipo.set("Selecione o tipo")

            # Opcional: pode chamar callback_logou() para retornar à tela de login ou outro fluxo
            # callback_logou()

        else:
            messagebox.showerror("Erro", mensagem)

    # Botão de Cadastro
    botao_cadastrar = ctk.CTkButton(cadastro_tab, text="Cadastrar", command=cadastrar, height=50)
    botao_cadastrar.pack(pady=20)
