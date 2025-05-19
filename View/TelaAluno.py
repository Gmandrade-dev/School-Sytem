from customtkinter import *

def TelaAluno(dados, login_window):
    janela = CTkToplevel()
    janela.geometry("500x500")
    janela.title("School System")
    janela.resizable(False, False)

    # Pegando os dados do aluno
    matricula = dados[0]
    cpf = dados[1]
    email = dados[2]
    senha = dados[3]
    nome = dados[4]

    # Criando as abas
    menu = CTkTabview(janela, width=500, height=500)
    menu.pack(fill="both", expand=True)
    menu.add("Notas")
    menu.add("Perfil")

    # Exemplo: conteúdo da aba "Perfil"
    perfil_tab = menu.tab("Perfil")
    CTkLabel(perfil_tab, text=f"Nome: {nome}").pack(pady=10)
    CTkLabel(perfil_tab, text=f"Matrícula: {matricula}").pack(pady=10)
    CTkLabel(perfil_tab, text=f"CPF: {cpf}").pack(pady=10)
    CTkLabel(perfil_tab, text=f"E-mail: {email}").pack(pady=10)

    # Aba "Notas" — você pode adaptar conforme os dados
    notas_tab = menu.tab("Notas")
    CTkLabel(notas_tab, text="Notas serão exibidas aqui...").pack(pady=20)

    # Tratamento de fechamento
    def on_close():
        janela.destroy()
        login_window.deiconify()

    janela.protocol("WM_DELETE_WINDOW", on_close)
