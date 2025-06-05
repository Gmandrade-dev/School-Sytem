from tkinter import messagebox
from customtkinter import *
from Controller.ExcluirController import ExcluirDisciplinaController
from Controller.EditarController import EditarDisciplinaController


def ExibirOneDisciplina(scroll, pesquisa, callback_recarregar):
    if not pesquisa or len(pesquisa) != 3:
        messagebox.showerror("Erro", "Dados da disciplina estão inválidos.")
        return

    id_disciplina, nome, matricula_professor = pesquisa

    # Labels dos cabeçalhos
    labels = ("ID", "Nome", "Matrícula Professor", "Excluir", "Editar")
    for idx, text in enumerate(labels):
        header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
        header_label.grid(row=0, column=idx, padx=5, pady=5)

    # Campo ID (somente leitura)
    entry_id = CTkEntry(scroll, width=120, height=45)
    entry_id.insert(0, id_disciplina)
    entry_id.configure(state="readonly")
    entry_id.grid(row=1, column=0, padx=5, pady=5)

    # Campo Nome
    entry_nome = CTkEntry(scroll, width=200, height=45)
    entry_nome.insert(0, nome)
    entry_nome.grid(row=1, column=1, padx=5, pady=5)

    # Campo Matrícula do Professor
    entry_matricula_prof = CTkEntry(scroll, width=120, height=45)
    entry_matricula_prof.insert(0, matricula_professor)
    entry_matricula_prof.grid(row=1, column=2, padx=5, pady=5)

    # Botão Excluir
    btn_excluir = CTkButton(
        scroll,
        text="Excluir",
        width=100,
        height=45,
        fg_color="#e02c2c",
        hover_color="#660d0d",
        text_color="#ffffff",
        command=lambda: DeletarDisciplina(id_disciplina, callback_recarregar)
    )
    btn_excluir.grid(row=1, column=3, padx=5, pady=5)

    # Botão Editar
    btn_editar = CTkButton(
        scroll,
        text="Editar",
        width=100,
        height=45,
        command=lambda: EditarDisciplina(
            id_disciplina,
            entry_nome.get(),
            entry_matricula_prof.get(),
            callback_recarregar
        )
    )
    btn_editar.grid(row=1, column=4, padx=5, pady=5)


def DeletarDisciplina(id_disciplina, callback_recarregar):
    confirmar = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta disciplina?")
    if confirmar:
        result = ExcluirDisciplinaController(id_disciplina)
        if not result:
            messagebox.showerror("Erro", "Erro ao excluir a disciplina.")
            return
        messagebox.showinfo("Sucesso", "Disciplina excluída com sucesso.")
        callback_recarregar()


def EditarDisciplina(id_disciplina, nome, matricula_professor, callback_recarregar):
    print(f"Editando disciplina: {id_disciplina}, Nome: {nome}, Matrícula Professor: {matricula_professor}")

    # try:
    #     # Verificar se matrícula é número
    #     matricula_int = int(matricula_professor)
    # except ValueError:
    #     messagebox.showerror("Erro", "Matrícula do professor deve ser um número.")
    #     return

    # sucesso, mensagem = EditarDisciplinaController(id_disciplina, nome, matricula_int)
    # if sucesso:
    #     messagebox.showinfo("Sucesso", mensagem)
    #     callback_recarregar()
    # else:
    #     messagebox.showerror("Erro", mensagem)
