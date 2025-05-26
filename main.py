from customtkinter import *
from View.TelaLogin import TelaLogin
from View.TelaAluno import TelaAluno
from View.TelaProfessor import TelaProfessor
from tkinter import messagebox

# Criar janela principal
main = CTk()
main.geometry("1000x670")
main.title("School System")
main.resizable(False, False)
set_appearance_mode("dark")
set_default_color_theme("blue")

frame_container = CTkFrame(main)
frame_container.pack(fill="both", expand=True)

def limpar_tela():
    for widget in frame_container.winfo_children():
        widget.destroy()

def mostrar_tela_login():
    limpar_tela()
    TelaLogin(frame_container, mostrar_tela_usuario)

def mostrar_tela_usuario(dados, nivel): 
    limpar_tela()
    if nivel == "aluno":
        TelaAluno(frame_container, dados, nivel, mostrar_tela_login)
    elif nivel == "professor":
        TelaProfessor(frame_container, dados, nivel, mostrar_tela_login)
    else:
        messagebox.showerror("Erro", "Nível de acesso inválido")

mostrar_tela_login()

main.mainloop()
