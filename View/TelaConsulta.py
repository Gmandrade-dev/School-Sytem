#from Controller.ListarController import listar_aluno, listar_professor, listar_nota, listar_disciplina, listar_aluno_disciplina
from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox


from Model.ListarModel import listar_aluno
from testes import editar_usuario, deletar_usuario

def limpar_frame_lista(container):
        for widget in container.winfo_children():
            widget.destroy()

def TelaConsulta(consulta_tab, dados, user_nivel, callback_logout):

    # limpar_frame_lista()

    def mostrar_alunos():
        limpar_frame_lista(janela_busca)
        alunos = listar_aluno()
        
        if not alunos:
            messagebox.showinfo("Consulta de Alunos", "Nenhum aluno encontrado.")
            return
        
        headers = ["MATRÍCULA", "CPF", "NOME", "EMAIL", "SENHA", "STATUS"]
        for col, texto in enumerate(headers):
            label = ctk.CTkLabel(janela_busca, text=texto, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=(5, 10))
        
        for idx, (matricula, cpf, nome, email, senha, status) in enumerate(alunos, start=1):
        # Entrys

            entry_matricula = ctk.CTkEntry(janela_busca, width=40, height=42)
            entry_matricula.insert(0, matricula)
            entry_matricula.configure(state="readonly")  # Matricula não pode ser alterada
            entry_matricula.grid(row=idx, column=0, padx=5, pady=5)

            entry_cpf = ctk.CTkEntry(janela_busca, width=100, height=42)
            entry_cpf.insert(0, cpf)
            entry_cpf.grid(row=idx, column=1, padx=5, pady=5)

            entry_nome = ctk.CTkEntry(janela_busca, width=120, height=42)
            entry_nome.insert(0, nome)
            entry_nome.grid(row=idx, column=2, padx=5, pady=5)

            entry_email = ctk.CTkEntry(janela_busca, width=200, height=42)
            entry_email.insert(0, email)
            entry_email.grid(row=idx, column=3, padx=5, pady=5)

            entry_senha = ctk.CTkEntry(janela_busca, width=80, show="*", height=42)
            entry_senha.insert(0, senha)
            entry_senha.grid(row=idx, column=4, padx=5, pady=5)

            entry_status = ctk.CTkEntry(janela_busca, width=50, height=42)
            entry_status.insert(0, status)
            entry_status.grid(row=idx, column=5, padx=5, pady=5)

            #print(alunos)
        
    container = ctk.CTkFrame(consulta_tab)
    container.pack(expand=True, fill="both" )

    titulo = ctk.CTkLabel(container, text="Consulta de Alunos", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    botao_buscar = ctk.CTkButton(container, text="Mostrar Todos os Alunos", command=mostrar_alunos)
    botao_buscar.pack(pady=10)

    janela_busca = ctk.CTkScrollableFrame(container)
    janela_busca.pack(expand=True, fill="both", padx=20, pady=20)


    

    
         
        

    
    




    



# Janela principal
#root = tk.Tk()
#root.title("Sistema de Alunos")

#botao_abrir = tk.Button(root, text="Abrir Janela de Busca", command=abrir_janela_busca)
#botao_abrir.pack(pady=20)

# Criar Treeview com colunas
#colunas = ("Matrícula", "CPF", "Nome", "Email", "Senha", "Status")
#tree = ttk.Treeview(root, columns=colunas, show='headings')

#for coluna in colunas:
#    tree.heading(coluna, text=coluna)
#    tree.column(coluna, width=100, anchor='center')
#
#tree.pack(fill=tk.BOTH, expand=True)

# Interface pronta

#def carregar_dados_professor():
#    professores = listar_professor()
#    for professor in professores:
        # Mascarar a senha
#        professor_formatado = professor[:4] + ('********', professor[5])
#        tree.insert('', 'end', values=professor_formatado)





