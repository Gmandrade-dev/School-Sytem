from customtkinter import *
from tkinter import messagebox
from Controller.ExibirController import ExibirAllController
from View.Frames.Components.ExibirDisciplina import ExibirDisciplinaComponent
from View.Frames.Components.ExibirNotas import ExibirNotaComponent


def ExibirNotasDisciplinas(gestao_tab, callback_logou):
    def limpar_frame_lista():
        for widget in scroll.winfo_children():
            widget.destroy()

    def mostrar_dados():
        limpar_frame_lista()
        tabela = selecionar.get()

        if tabela == "Disciplinas":
            tabela_db = "disciplina"
        elif tabela == "Notas":
            tabela_db = "nota"
        else:
            messagebox.showerror("Erro", "Selecione uma opção válida.")
            return

        dados = ExibirAllController(tabela_db)

        if not dados:
            label = CTkLabel(scroll, text="Não foi possível encontrar dados.", font=("Arial", 16))
            label.pack(padx=10, pady=10)
            return

        if tabela_db == "disciplina":
            ExibirDisciplinaComponent(scroll, dados, mostrar_dados)

        elif tabela_db == "nota":
            ExibirNotaComponent(scroll, dados, mostrar_dados)

    linha_selecao = CTkFrame(gestao_tab, height=50)
    linha_selecao.pack(pady=5)

    selecionar = CTkComboBox(linha_selecao, values=["Disciplinas", "Notas"], width=200, height=50, state="readonly")
    selecionar.pack(side="left", padx=5, pady=5)
    selecionar.set("Disciplinas")

    btn_exibir = CTkButton(linha_selecao, text="Exibir", height=50, command=mostrar_dados)
    btn_exibir.pack(side="left", padx=5, pady=5)

    scroll = CTkScrollableFrame(gestao_tab)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)
