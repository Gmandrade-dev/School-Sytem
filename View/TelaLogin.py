from customtkinter import *
from Controller.LoginController import LoginController
from tkinter import messagebox
from View.TelaAluno import TelaAluno  # garante que aceita um parâmetro (dados)

def TelaLogin():
    tela = CTk()
    tela.geometry("500x500")
    tela.title("School System")
    tela.resizable(False, False)

    def handle_login():
        nivel = nivelAcesso.get()
        email = campo_email.get()
        senha = campo_senha.get()

        dados = LoginController(email, senha, nivel)

        if dados:
            if nivel == "Aluno":
                print("Login realizado com sucesso!")
                tela.quit()  
                tela.destroy()  
                TelaAluno(frameAluno,dados) 
                
                 # ← Agora envia os dados do aluno
            else:
                print("Login com tipo não tratado ainda.")
                messagebox.showinfo("Atenção", "Login de professor será implementado em breve.")
        else:
            print("Senha ou usuário incorretos.")
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
    frameAluno = CTkFrame(tela)
    section = CTkFrame(tela, width=400, height=400, fg_color="transparent")
    section.place(relx=0.5, rely=0.5, anchor=CENTER)

    nivelAcesso = CTkComboBox(section, values=["Aluno", "Professor"], width=200, height=40)
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

    tela.mainloop()
