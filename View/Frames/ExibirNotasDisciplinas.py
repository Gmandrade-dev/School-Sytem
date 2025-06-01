from customtkinter import *
from tkinter import messagebox
from Controller.ExibirController import ExibirAllController
from Controller.ExcluirController import ExcluirNotaController,ExcluirDisciplinaController

def ExibirNotasDisciplinas(gestao_tab, callback_logou):       
    
    def limpar_frame_lista():
        for widget in scroll.winfo_children():
            widget.destroy()
    
    def mostrar_dados():
        limpar_frame_lista()
        tabela= selicionar.get()
    

        if tabela == "Disciplinas":
            tabela= "disciplina"
        elif tabela == "Notas":
            tabela= "nota"
        else:
            messagebox.showerror("Erro", "Selecione uma opção válida.")
            return

        dados= ExibirAllController(tabela)

        if not dados:
            label = CTkLabel(scroll, text="Não foi possível encontrar dados.", font=("Arial", 16))
            label.pack(padx=10, pady=10)
            return
        if tabela == "disciplina":
            campo_pesquisa = CTkEntry(scroll, placeholder_text="ID", width=200, height=20)
            campo_pesquisa.grid(row=0, column=7, padx=5, pady=5)

            btnpesquisar = CTkButton(scroll, text="Pesquisar", height=25,width=100)
            btnpesquisar.grid(row=0, column=8, padx=5, pady=5)

            label =("ID", "Nome", "Matrícula Professor", "Excluir", "Editar")
            for idx, text in enumerate(label):

                header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
                header_label.grid(row=0, column=idx, padx=5, pady=5)


            for idx, (id_disciplina, nome, matricula_professor) in enumerate(dados,start=1):
                def DeletarDisciplina():
                    id_disciplina = entry_codigo.get()
                    mensagem = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta nota?")
                    if mensagem:
          
                        result=ExcluirDisciplinaController(id_disciplina)
                        if not result:
                            messagebox.showerror("Erro", "Erro ao excluir Disciplina.")
                            
                        messagebox.showinfo("Sucesso", "Disciplina excluída com sucesso.")
                        mostrar_dados()

                entry_codigo = CTkEntry(scroll, width=120,height=45)
                entry_codigo.insert(0, id_disciplina)
                entry_codigo.configure(state="readonly")
                entry_codigo.grid(row=idx, column=0, padx=5, pady=5)

                entry_nome = CTkEntry(scroll, width=200,height=45)
                entry_nome.insert(0, nome)
                entry_nome.grid(row=idx, column=1, padx=5, pady=5)

                entry_matricula_professor = CTkEntry(scroll, width=120,height=45)
                entry_matricula_professor.insert(0, matricula_professor)
                entry_matricula_professor.grid(row=idx, column=2, padx=5, pady=5)

                btn_editar = CTkButton(scroll, text="Editar", width=100,height=45)
                btn_editar.grid(row=idx, column=4, padx=5, pady=5)

                btn_excluir = CTkButton(scroll, text="Excluir", width=100,height=45,fg_color="#e02c2c",hover_color="#660d0d", text_color="#ffffff",command=DeletarDisciplina)
                btn_excluir.grid(row=idx, column=3, padx=5, pady=5)

        elif tabela == "nota":
            campo_pesquisa = CTkEntry(scroll, placeholder_text="ID", width=110, height=20)
            campo_pesquisa.grid(row=0, column=7, padx=5, pady=5)

            btnpesquisar = CTkButton(scroll, text="Pesquisar", height=25,width=100)
            btnpesquisar.grid(row=0, column=8, padx=5, pady=5)

            label =("ID Nota", "Matrícula Aluno", "ID Disciplina", "Nota 1", "Nota 2", "Nota 3", "Média", "Excluir", "Editar")
            for idx, text in enumerate(label):

                header_label = CTkLabel(scroll, text=text, font=("Arial", 14))
                header_label.grid(row=1, column=idx, padx=5, pady=5)

            for idx, (id_nota, matricula_aluno, id_disciplina, nota1, nota2, nota3, media) in enumerate(dados,start=2):

                def DeletarNota():
                    id_nota = entry_id_nota.get()
                    mensagem = messagebox.askyesno("Confirmação", "Você tem certeza que deseja excluir esta nota?")
                    if mensagem:
          
                        result=ExcluirNotaController(id_nota)
                        if not result:
                            messagebox.showerror("Erro", "Erro ao excluir nota.")
                            
                        messagebox.showinfo("Sucesso", "Nota excluída com sucesso.")
                        mostrar_dados()

                entry_id_nota = CTkEntry(scroll, width=120,height=45)
                entry_id_nota.insert(0, id_nota)
                entry_id_nota.configure(state="readonly")
                entry_id_nota.grid(row=idx, column=0, padx=5, pady=5)

                entry_matricula_aluno = CTkEntry(scroll, width=120,height=45)
                entry_matricula_aluno.insert(0, matricula_aluno)
                entry_matricula_aluno.grid(row=idx, column=1, padx=5, pady=5)

                entry_id_disciplina = CTkEntry(scroll, width=120,height=45)
                entry_id_disciplina.insert(0, id_disciplina)
                entry_id_disciplina.grid(row=idx, column=2, padx=5, pady=5)

                entry_nota1 = CTkEntry(scroll, width=120,height=45)
                entry_nota1.insert(0, nota1)
                entry_nota1.grid(row=idx, column=3, padx=5, pady=5)

                entry_nota2 = CTkEntry(scroll, width=120,height=45)
                entry_nota2.insert(0, nota2)
                entry_nota2.grid(row=idx, column=4, padx=5, pady=5)

                entry_nota3 = CTkEntry(scroll, width=120,height=45)
                entry_nota3.insert(0, nota3)
                entry_nota3.grid(row=idx, column=5, padx=5, pady=5)

                entry_media = CTkEntry(scroll, width=120,height=45)
                entry_media.insert(0, media)
                entry_media.grid(row=idx, column=6, padx=5, pady=5)

                btn_editar = CTkButton(scroll,text="Editar", width=100,height=45)
                btn_editar.grid(row=idx,column=7,padx=5,pady=5)

                btn_excluir = CTkButton(scroll,text="Excluir", width=100,height=45, fg_color="#e02c2c",hover_color="#660d0d", text_color="#ffffff",command=DeletarNota)
                btn_excluir.grid(row=idx,column=8,padx=5,pady=5)
        else:
            messagebox.showerror("Erro", "Selecione uma opção válida.")
            return
                

    linha6=CTkFrame(gestao_tab,height=50)
    linha6.pack(pady=5)
    selicionar = CTkComboBox(linha6, values=["Disciplinas", "Notas"], width=200, height=50)
    selicionar.pack(side="left", padx=5, pady=5)
    selicionar.configure(state="readonly")
    btnexibir = CTkButton(linha6, text="Exibir", height=50, command=mostrar_dados)
    btnexibir.pack(side="left", padx=5, pady=5)


    
    scroll = CTkScrollableFrame(gestao_tab)
    scroll.pack(fill="both", expand=True, padx=10, pady=10)

