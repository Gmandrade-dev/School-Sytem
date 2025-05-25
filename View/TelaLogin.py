from customtkinter import *
from Controller.LoginController import LoginController
from tkinter import messagebox

def TelaLogin(main, callback_trocar_tela):
    frame_login = CTkFrame(main)
    frame_login.pack(fill="both", expand=True)

    def handle_login():
        nivel = nivelAcesso.get()
        email = campo_email.get()
        senha = campo_senha.get()

        dados = LoginController(email, senha, nivel)

        if dados:
            callback_trocar_tela(dados, nivel)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    section = CTkFrame(frame_login, width=400, height=400, fg_color="transparent")
    section.place(relx=0.5, rely=0.5, anchor=CENTER)

    nivelAcesso = CTkComboBox(section, values=["aluno", "professor"], width=200, height=40)
    nivelAcesso.pack(pady=20)

    campo_email = CTkEntry(section, placeholder_text="Email", width=200, height=40)
    campo_email.pack(pady=20)

    campo_senha = CTkEntry(section, placeholder_text="Senha", width=200, height=40, show="*")
    campo_senha.pack(pady=20)

    mostrar = CTkCheckBox(section, text="Mostrar Senha")
    mostrar.pack(pady=10)
    mostrar.configure(command=lambda: campo_senha.configure(show="" if mostrar.get() else "*"))

    botao = CTkButton(section, text="Login", width=100, height=40, command=handle_login)
    botao.pack(pady=10)
