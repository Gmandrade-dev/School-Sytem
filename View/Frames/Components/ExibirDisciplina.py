from tkinter import messagebox
from customtkinter import *
from Controller.ExcluirController import ExcluirDisciplinaController
from Controller.EditarController import EditarDisciplinaController


def ExibirDisciplinaComponent(scroll, dados, callback_recarregar):

    labels = ("ID", "Nome", "Matrícula Professor", "Excluir", "Editar")
    for idx, text in enumerate(labels):
        header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
        header_label.grid(row=1, column=idx, padx=5, pady=5)

    for idx, (id_disciplina, nome, matricula_professor) in enumerate(dados, start=2):

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
        

        # ✅ Botão excluir
        btn_excluir = CTkButton(
            scroll,
            text="Excluir",
            width=100,
            height=45,
            fg_color="#e02c2c",
            hover_color="#660d0d",
            text_color="#ffffff",
            command=lambda id_disciplina=id_disciplina: DeletarNota(id_disciplina, callback_recarregar)
        )
        btn_excluir.grid(row=idx, column=3, padx=5, pady=5)

        btn_editar = CTkButton(
            scroll,
            text="Editar",
            width=100,
            height=45,
            command=lambda id_disciplina=id_disciplina,
                        nome_entry=entry_nome,
                        matricula_entry=entry_matricula_prof: EditarNota(
                id_disciplina,
                nome_entry.get(),
                matricula_entry.get(),
            )
        )
        btn_editar.grid(row=idx, column=4, padx=5, pady=5)

        

def DeletarNota(id_disciplina, callback_recarregar):
    confirmar = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta nota?")
    if confirmar:
        result = ExcluirDisciplinaController(id_disciplina)
        if not result:
            messagebox.showerror("Erro", "Erro ao excluir nota.")
            return
        messagebox.showinfo("Sucesso", "Nota excluída com sucesso.")
        callback_recarregar()


# ✅ Função para editar nota
def EditarNota(id_disciplina, nome, matricula_professor):
    print(f"Editando disciplina: {id_disciplina}, Nome: {nome}, Matrícula do Professor: {matricula_professor}")
    sucesso, mensagem = EditarDisciplinaController(id_disciplina, nome, matricula_professor)
    if sucesso:
        messagebox.showinfo("Sucesso", mensagem)
        
    else:
        messagebox.showerror("Erro", mensagem)