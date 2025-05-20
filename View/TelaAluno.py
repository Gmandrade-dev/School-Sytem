from customtkinter import *

# Definir o tema da interface
set_appearance_mode("dark")  # Tema escuro
set_default_color_theme("blue")  # Tema azul escuro

def TelaAluno(dados, login_window):
    # Criar a janela principal da tela do aluno
    janela = CTkToplevel()
    janela.geometry("500x500")
    janela.title("School System")
    janela.resizable(False, False)

    # Descompactar dados do aluno
    matricula, cpf, email, senha, nome = dados

    # Criar o menu de abas
    menu = CTkTabview(janela)
    menu.pack(fill="both", expand=True, padx=10, pady=10)

    menu.add("Perfil")
    menu.add("Notas")

    # ----- Aba Perfil -----
    perfil_tab = menu.tab("Perfil")

    CTkLabel(perfil_tab, text="Informações do Aluno", font=("Arial", 18, "bold")).pack(pady=15)

    CTkLabel(perfil_tab, text=f"Nome: {nome}", font=("Arial", 14)).pack(pady=5)
    CTkLabel(perfil_tab, text=f"Matrícula: {matricula}", font=("Arial", 14)).pack(pady=5)
    CTkLabel(perfil_tab, text=f"CPF: {cpf}", font=("Arial", 14)).pack(pady=5)
    CTkLabel(perfil_tab, text=f"E-mail: {email}", font=("Arial", 14)).pack(pady=5)

    # ----- Aba Notas -----
    notas_tab = menu.tab("Notas")
    CTkLabel(notas_tab, text="Notas do Aluno", font=("Arial", 18, "bold")).pack(pady=15)
    CTkLabel(notas_tab, text="Notas serão exibidas aqui...", font=("Arial", 14)).pack(pady=10)

    # ----- Evento ao fechar -----
    def on_close():
        janela.destroy()
        login_window.deiconify()

    janela.protocol("WM_DELETE_WINDOW", on_close)
