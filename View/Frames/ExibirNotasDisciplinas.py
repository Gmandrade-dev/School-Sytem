from customtkinter import *
from tkinter import messagebox
from Controller.ExibirController import ExibirAllController, ExibirOneController
from View.Frames.Components.ExibirDisciplina import ExibirDisciplinaComponent
from View.Frames.Components.ExibirNotas import ExibirNotaComponent
from View.Frames.Components.ExibirOneNota import ExibirOneNota


def ExibirNotasDisciplinas(gestao_tab, callback_logou):
    def limpar_frame_lista():
        for widget in scroll.winfo_children():
            widget.destroy()

    def verificar_tabela():
        tabela = selecionar.get()
        if tabela == "Disciplinas":
            return "disciplina"
        elif tabela == "Notas":
            return "nota"
        else:
            messagebox.showerror("Erro", "Selecione uma tabela válida.")
            return None

    def mostrar_one_dado(id_aluno):
        limpar_frame_lista()
        tabela = verificar_tabela()
        if not tabela:
            return

        if not id_aluno.isdigit():
            messagebox.showerror("Erro", "Digite um ID válido (número inteiro).")
            return

        id_aluno = int(id_aluno)
        pesquisa = ExibirOneController(tabela, id_aluno)

        if pesquisa:
            # Garante que dados seja sempre uma lista (mesmo que contenha só um resultado)
            if not isinstance(pesquisa, list):
                pesquisa = [pesquisa]

            if tabela == "disciplina":
                ExibirDisciplinaComponent(scroll, pesquisa, mostrar_dados)
            elif tabela == "nota":
                ExibirNotaComponent(scroll, pesquisa, mostrar_dados)
        else:
            label = CTkLabel(scroll, text="Não foi possível encontrar dados.", font=("Arial", 16))
            label.pack(padx=10, pady=10)


    def mostrar_dados():
        limpar_frame_lista()
        tabela_db = verificar_tabela()
        if not tabela_db:
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

    # ▪️ Interface
    linha_selecao = CTkFrame(gestao_tab, height=50)
    linha_selecao.pack(pady=5)

    selecionar = CTkComboBox(linha_selecao, values=["Disciplinas", "Notas"], width=200, height=50, state="readonly")
    selecionar.pack(side="left", padx=5, pady=5)
    selecionar.set("Disciplinas")

    btn_exibir = CTkButton(linha_selecao, text="Exibir Todos", height=50, command=mostrar_dados)
    btn_exibir.pack(side="left", padx=5, pady=5)

    campo_pesquisa = CTkEntry(linha_selecao, placeholder_text="Matricula", width=110, height=50)
    campo_pesquisa.pack(side="left", padx=5, pady=5)

    btn_pesquisar = CTkButton(
        linha_selecao, text="Pesquisar", height=50, width=100,
        command=lambda: mostrar_one_dado(campo_pesquisa.get())
    )
    btn_pesquisar.pack(side="left", padx=5, pady=5)

    scroll = CTkScrollableFrame(gestao_tab)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)
