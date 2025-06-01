from tkinter import messagebox
from customtkinter import *
from Controller.ExcluirController import ExcluirNotaController


def ExibirNotaComponent(scroll, dados, callback_recarregar):
    campo_pesquisa = CTkEntry(scroll, placeholder_text="ID", width=110, height=20)
    campo_pesquisa.grid(row=0, column=7, padx=5, pady=5)

    btn_pesquisar = CTkButton(scroll, text="Pesquisar", height=25, width=100)
    btn_pesquisar.grid(row=0, column=8, padx=5, pady=5)

    labels = ("ID Nota", "Matrícula Aluno", "ID Disciplina", "Nota 1", "Nota 2", "Nota 3", "Média", "Excluir", "Editar")
    for idx, text in enumerate(labels):
        header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
        header_label.grid(row=1, column=idx, padx=5, pady=5)

    for idx, (id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3, media) in enumerate(dados, start=2):
        def DeletarNota(id_nota=id_nota):
            confirmar = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta nota?")
            if confirmar:
                result = ExcluirNotaController(id_nota)
                if not result:
                    messagebox.showerror("Erro", "Erro ao excluir nota.")
                    return
                messagebox.showinfo("Sucesso", "Nota excluída com sucesso.")
                callback_recarregar()

        entry_id_nota = CTkEntry(scroll, width=120, height=45)
        entry_id_nota.insert(0, id_nota)
        entry_id_nota.configure(state="readonly")
        entry_id_nota.grid(row=idx, column=0, padx=5, pady=5)

        entry_matricula_aluno = CTkEntry(scroll, width=120, height=45)
        entry_matricula_aluno.insert(0, matricula_aluno)
        entry_matricula_aluno.grid(row=idx, column=1, padx=5, pady=5)

        entry_id_disciplina = CTkEntry(scroll, width=120, height=45)
        entry_id_disciplina.insert(0, id_disciplina)
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
        entry_media.grid(row=idx, column=6, padx=5, pady=5)

        btn_editar = CTkButton(scroll, text="Editar", width=100, height=45)
        btn_editar.grid(row=idx, column=7, padx=5, pady=5)

        btn_excluir = CTkButton(
            scroll, text="Excluir", width=100, height=45,
            fg_color="#e02c2c", hover_color="#660d0d", text_color="#ffffff",
            command=DeletarNota
        )
        btn_excluir.grid(row=idx, column=8, padx=5, pady=5)
