import customtkinter as ctk
from testes import buscar_todos, editar_usuario, deletar_usuario

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Gerenciador de Usuários")
app.geometry("900x600")

frame_lista = ctk.CTkScrollableFrame(app, width=880, height=450)
frame_lista.pack(padx=10, pady=10)

def limpar_frame_lista():
    for widget in frame_lista.winfo_children():
        widget.destroy()

def mostrar_todos():
    limpar_frame_lista()
    dados = buscar_todos()

    if not dados:
        label = ctk.CTkLabel(frame_lista, text="Nenhum dado encontrado.")
        label.pack()
        return

    for idx, (matricula, nome, email) in enumerate(dados):
        # Entrys
        entry_matricula = ctk.CTkEntry(frame_lista, width=120)
        entry_matricula.insert(0, matricula)
        entry_matricula.configure(state="readonly")  # Matricula não pode ser alterada
        entry_matricula.grid(row=idx, column=0, padx=5, pady=5)

        entry_nome = ctk.CTkEntry(frame_lista, width=200)
        entry_nome.insert(0, nome)
        entry_nome.grid(row=idx, column=1, padx=5, pady=5)

        entry_email = ctk.CTkEntry(frame_lista, width=250)
        entry_email.insert(0, email)
        entry_email.grid(row=idx, column=2, padx=5, pady=5)

        # Botão editar
        def editar_closure(matricula=matricula, en_nome=entry_nome, en_email=entry_email):
            def editar():
                novo_nome = en_nome.get()
                novo_email = en_email.get()
                sucesso = editar_usuario(matricula, novo_nome, novo_email)
                if sucesso:
                    print(f"Usuário {matricula} editado com sucesso.")
                else:
                    print(f"Erro ao editar usuário {matricula}.")
            return editar

        btn_editar = ctk.CTkButton(frame_lista, text="Editar", command=editar_closure())
        btn_editar.grid(row=idx, column=3, padx=5, pady=5)

        # Botão deletar
        def deletar_closure(matricula=matricula):
            def deletar():
                sucesso = deletar_usuario(matricula)
                if sucesso:
                    print(f"Usuário {matricula} deletado.")
                    mostrar_todos()  # Atualiza a lista
                else:
                    print(f"Erro ao deletar usuário {matricula}.")
            return deletar

        btn_deletar = ctk.CTkButton(frame_lista, text="Deletar", command=deletar_closure())
        btn_deletar.grid(row=idx, column=4, padx=5, pady=5)


# Botão para carregar lista
btn_mostrar = ctk.CTkButton(app, text="Mostrar Todos", command=mostrar_todos)
btn_mostrar.pack(pady=5)

app.mainloop()
