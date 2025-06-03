from tkinter import messagebox
from customtkinter import *
from Controller.ExcluirController import ExcluirNotaController
from Controller.EditarController import EditarNotaController
from Controller.ExibirController import PesquisarNotaController  # Crie esse controller se ainda não tiver


def ExibirNotaComponent(scroll, dados, callback_recarregar):
    # 🔸 Remove widgets antigos (se houver)
    for widget in scroll.winfo_children():
        widget.destroy()

    # 🏷️ Cabeçalhos
    labels = ("ID Nota", "Matrícula Aluno", "ID Disciplina", "Nota 1", "Nota 2", "Nota 3", "Média", "Excluir", "Editar")
    for idx, text in enumerate(labels):
        header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
        header_label.grid(row=1, column=idx, padx=5, pady=5)

    # 🔄 Gerar linhas de dados
    for idx, (id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3, media) in enumerate(dados, start=2):
        entry_id_nota = CTkEntry(scroll, width=120, height=45)
        entry_id_nota.insert(0, id_nota)
        entry_id_nota.configure(state="readonly")
        entry_id_nota.grid(row=idx, column=0, padx=5, pady=5)

        entry_matricula_aluno = CTkEntry(scroll, width=120, height=45)
        entry_matricula_aluno.insert(0, matricula_aluno)
        entry_matricula_aluno.configure(state="readonly")
        entry_matricula_aluno.grid(row=idx, column=1, padx=5, pady=5)

        entry_id_disciplina = CTkEntry(scroll, width=120, height=45)
        entry_id_disciplina.insert(0, id_disciplina)
        entry_id_disciplina.configure(state="readonly")
        entry_id_disciplina.grid(row=idx, column=2, padx=5, pady=5)

        entry_nota1 = CTkEntry(scroll, width=120, height=45)
        entry_nota1.insert(0, nota1)
        entry_nota1.grid(row=idx, column=3, padx=5, pady=5)

        entry_nota2 = CTkEntry(scroll, width=120, height=45)
        entry_nota2.insert(0, nota2)
        entry_nota2.grid(row=idx, column=4, padx=5, pady=5)

        entry_nota3 = CTkEntry(scroll, width=120, height=45)
        entry_nota3.insert(0, nota3)
        entry_nota3.grid(row=idx, column=5, padx=5, pady=5)

        entry_media = CTkEntry(scroll, width=120, height=45)
        entry_media.insert(0, media)
        entry_media.configure(state="readonly")
        entry_media.grid(row=idx, column=6, padx=5, pady=5)

        btn_excluir = CTkButton(
            scroll,
            text="Excluir",
            width=100,
            height=45,
            fg_color="#e02c2c",
            hover_color="#660d0d",
            text_color="#ffffff",
            command=lambda id_nota=id_nota: DeletarNota(id_nota, callback_recarregar)
        )
        btn_excluir.grid(row=idx, column=7, padx=5, pady=5)

        btn_editar = CTkButton(
            scroll,
            text="Editar",
            width=100,
            height=45,
            command=lambda id_nota=id_nota,
                           matricula=matricula_aluno,
                           disciplina=id_disciplina,
                           n1=entry_nota1,
                           n2=entry_nota2,
                           n3=entry_nota3: EditarNota(
                id_nota,
                matricula,
                disciplina,
                n1.get(),
                n2.get(),
                n3.get(),
                callback_recarregar
            )
        )
        btn_editar.grid(row=idx, column=8, padx=5, pady=5)


# 🔍 Adicionar pesquisa corretamente
def CriarBusca(scroll, callback_recarregar):
    campo_pesquisa = CTkEntry(scroll, placeholder_text="Digite o Id do Aluno", width=110, height=20)
    campo_pesquisa.grid(row=0, column=6, padx=5, pady=5)

    def buscar():
        id_aluno = campo_pesquisa.get()
        if id_aluno == "":
            messagebox.showwarning("Aviso", "Digite o ID do aluno para pesquisar.")
            return
        dados = PesquisarNotaController(id_aluno)  # Retorna lista no mesmo formato dos dados normais
        if not dados:
            messagebox.showinfo("Resultado", "Nenhuma nota encontrada para este aluno.")
        ExibirNotaComponent(scroll, dados, callback_recarregar)

    btn_pesquisar = CTkButton(scroll, text="Pesquisar", height=25, width=100, command=buscar)
    btn_pesquisar.grid(row=0, column=7, padx=5, pady=5)

    btn_listar_todos = CTkButton(scroll, text="Listar Todos", height=25, width=100, command=callback_recarregar)
    btn_listar_todos.grid(row=0, column=8, padx=5, pady=5)


# ✅ Funções utilitárias
def DeletarNota(id_nota, callback_recarregar):
    confirmar = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta nota?")
    if confirmar:
        result = ExcluirNotaController(id_nota)
        if not result:
            messagebox.showerror("Erro", "Erro ao excluir nota.")
            return
        messagebox.showinfo("Sucesso", "Nota excluída com sucesso.")
        callback_recarregar()


def EditarNota(id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3, callback_recarregar):
    sucesso, mensagem = EditarNotaController(id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3)
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        callback_recarregar()
    else:
        messagebox.showerror("Erro", mensagem)
