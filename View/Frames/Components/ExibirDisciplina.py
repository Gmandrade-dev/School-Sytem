from tkinter import messagebox
from customtkinter import *
from Controller.ExcluirController import ExcluirDisciplinaController
from Controller.EditarController import EditarDisciplinaController


def ExibirDisciplinaComponent(scroll, dados, callback_recarregar):
    campo_pesquisa = CTkEntry(scroll, placeholder_text="ID", width=200, height=20)
    campo_pesquisa.grid(row=0, column=7, padx=5, pady=5)

    btn_pesquisar = CTkButton(scroll, text="Pesquisar", height=25, width=100)
    btn_pesquisar.grid(row=0, column=8, padx=5, pady=5)

    labels = ("ID", "Nome", "Matrícula Professor", "Excluir", "Editar")
    for idx, text in enumerate(labels):
        header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
        header_label.grid(row=1, column=idx, padx=5, pady=5)

    for idx, (id_disciplina, nome, matricula_professor) in enumerate(dados, start=2):
        def DeletarDisciplina(id_disciplina=id_disciplina):
            confirmar = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta disciplina?")
            if confirmar:
                result = ExcluirDisciplinaController(id_disciplina)
                if not result:
                    messagebox.showerror("Erro", "Erro ao excluir disciplina.")
                    return
                messagebox.showinfo("Sucesso", "Disciplina excluída com sucesso.")
                callback_recarregar()

        entry_id = CTkEntry(scroll, width=120, height=45)
        entry_id.insert(0, id_disciplina)
        entry_id.configure(state="readonly")
        entry_id.grid(row=idx, column=0, padx=5, pady=5)

        entry_nome = CTkEntry(scroll, width=200, height=45)
        entry_nome.insert(0, nome)
        entry_nome.grid(row=idx, column=1, padx=5, pady=5)

        entry_matricula_prof = CTkEntry(scroll, width=120, height=45)
        entry_matricula_prof.insert(0, matricula_professor)
        entry_matricula_prof.grid(row=idx, column=2, padx=5, pady=5)
        

        btn_editar = CTkButton(scroll, text="Editar", width=100, height=45)
        btn_editar.grid(row=idx, column=4, padx=5, pady=5)

        btn_excluir = CTkButton(
            scroll, text="Excluir", width=100, height=45,
            fg_color="#e02c2c", hover_color="#660d0d", text_color="#ffffff",
            command=DeletarDisciplina
        )
        btn_excluir.grid(row=idx, column=3, padx=5, pady=5)
