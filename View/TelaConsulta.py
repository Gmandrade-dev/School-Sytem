#from Controller.ListarController import listar_aluno, listar_professor, listar_nota, listar_disciplina, listar_aluno_disciplina
from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from Model.ListarModel import listar_aluno, listar_aluno_um, listar_professor, listar_professor_um
from Controller.ExibirController import ExibirAllController
from Controller.ListarController import ExibirProfAluno

def limpar_frame_lista(container):
        for widget in container.winfo_children():
            widget.destroy()

def TelaConsulta(consulta_tab, dados, user_nivel, callback_logout): # FUNÇÃO PARA CRIAR A TELA DE CONSULTA DE ALUNOS

    # limpar_frame_lista()

    def mostrar_alunos(): # FUNÇÃO PARA MOSTRAR TODOS OS ALUNOS CADASTRADOS

        limpar_frame_lista(janela_busca) # Limpa o frame antes de mostrar os dados dos alunos
        tabela = selecionar.get() # SELECIONA O TIPO DE CONSULTA (ALUNO OU PROFESSOR)

        if tabela == "Aluno": # SE O TIPO DE CONSULTA FOR ALUNO, LISTA OS ALUNOS CADASTRADOS
            tabela = "aluno" # AQUI É ONDE O TIPO DE CONSULTA É DEFINIDO COMO ALUNO
        elif tabela == "Professor": # SE O TIPO DE CONSULTA FOR PROFESSOR, LISTA OS PROFESSORES CADASTRADOS
            tabela = "professor" # AQUI É ONDE O TIPO DE CONSULTA É DEFINIDO COMO PROFESSOR
        else:
            messagebox.showinfo("Consulta", "Selecione um tipo de consulta válido.")
            return

        if tabela == "aluno": # SE O TIPO DE CONSULTA FOR ALUNO, LISTA OS ALUNOS CADASTRADOS
            resultado = ExibirAllController(tabela)
        elif tabela == "professor": # SE O TIPO DE CONSULTA FOR PROFESSOR, LISTA OS PROFESSORES CADASTRADOS
            resultado = ExibirAllController(tabela)
        else:
            messagebox.showinfo("Consulta", "Selecione um tipo de consulta válido.")
            return
        
        if not resultado: # Se não houver alunos cadastrados, exibe uma mensagem
            messagebox.showinfo("Consulta", "Nenhum aluno encontrado.")
            return
        
        headers = ["MATRÍCULA", "CPF", "NOME", "EMAIL", "SENHA", "STATUS"] # TITULOS DAS COLUNAS
        for col, texto in enumerate(headers):
            label = ctk.CTkLabel(janela_busca, text=texto, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=(5, 10))

        for idx, (matricula, cpf, nome, email, senha, status) in enumerate(resultado, start=1): # COLOCANDO OS DADOS DOS ALUNOS NAS DETERMINADAS VARIÁVEIS E EXIBINDO UMA EM CADA COLUNA.
            # Entrys
            entry_matricula = ctk.CTkEntry(janela_busca, width=40, height=42)
            entry_matricula.insert(0, matricula) # RETORNA A MATRÍCULA
            entry_matricula.configure(state="readonly")  # Matricula não pode ser alterada
            entry_matricula.grid(row=idx, column=0, padx=5, pady=5)

            entry_cpf = ctk.CTkEntry(janela_busca, width=100, height=42)
            entry_cpf.insert(0, cpf) # RETORNA O CPF
            entry_cpf.configure(state="readonly") # Não pode ser alterado
            entry_cpf.grid(row=idx, column=1, padx=5, pady=5)

            entry_nome = ctk.CTkEntry(janela_busca, width=120, height=42)
            entry_nome.insert(0, nome) # RETORNA O NOME
            entry_nome.grid(row=idx, column=2, padx=5, pady=5)

            entry_email = ctk.CTkEntry(janela_busca, width=200, height=42)
            entry_email.insert(0, email) # RETORNA O EMAIL
            entry_email.grid(row=idx, column=3, padx=5, pady=5)

            entry_senha = ctk.CTkEntry(janela_busca, width=80, show="*", height=42)
            entry_senha.insert(0, senha) # RETORNA A SENHA
            entry_senha.grid(row=idx, column=4, padx=5, pady=5)

            if status == 1: # SE O STATUS FOR 1, O ALUNO ESTÁ ATIVO
                status = "Ativo"
            else:
                status = "Inativo"

            entry_status = ctk.CTkEntry(janela_busca, width=50, height=42)
            entry_status.insert(0, status) # RETORNA O STATUS
            entry_status.grid(row=idx, column=5, padx=5, pady=5)
        
            #print(alunos)


    def mostrar_aluno(): # FUNÇÃO PARA MOSTRAR UM ALUNO CADASTRADO(PELA BUSCA DA MATRÍCULA)

        limpar_frame_lista(janela_busca) # Limpa o frame antes de mostrar os dados do aluno
        #aluno = listar_aluno_um(entry_buscar.get())
        #aluno = [listar_aluno_um(entry_buscar.get())] # TRANSFORMA A TUPLA EM LISTA(ARRAY) PARA PODER ITERAR E CONSEGUIR USAR AS POSIÇÕES DO ARRAY.
        tabela = selecionar.get() # SELECIONA O TIPO DE CONSULTA (ALUNO OU PROFESSOR)
        id = int(entry_buscar.get()) # PEGA O VALOR DO ENTRY PARA BUSCAR A MATRÍCULA DO ALUNO OU PROFESSOR

        if not isinstance(id, int): # Verifica se o valor do entry é um número inteiro
            messagebox.showinfo("Consulta", "Digite uma matrícula válida.")
            return

        if tabela == "Aluno": # SE O TIPO DE CONSULTA FOR ALUNO, LISTA OS ALUNOS CADASTRADOS
            tabela = "aluno" # AQUI É ONDE O TIPO DE CONSULTA É DEFINIDO COMO ALUNO
        elif tabela == "Professor": # SE O TIPO DE CONSULTA FOR PROFESSOR, LISTA OS PROFESSORES CADASTRADOS
            tabela = "professor" # AQUI É ONDE O TIPO DE CONSULTA É DEFINIDO COMO PROFESSOR
        else:
            messagebox.showinfo("Consulta", "Selecione um tipo de consulta válido.")
            return

        if tabela == "aluno": # SE O TIPO DE CONSULTA FOR ALUNO, LISTA OS ALUNOS CADASTRADOS
            resultado = [ExibirProfAluno(tabela, id)]
        elif tabela == "professor": # SE O TIPO DE CONSULTA FOR PROFESSOR, LISTA OS PROFESSORES CADASTRADOS
            resultado = [ExibirProfAluno(tabela, id)]
        else:
            messagebox.showinfo("Consulta", "Selecione um tipo de consulta válido.")
            return

        if not resultado:
            messagebox.showinfo("Consulta", "Nenhum aluno encontrado.")
            return
        
        headers = ["MATRÍCULA", "CPF", "NOME", "EMAIL", "SENHA", "STATUS"] # TITULOS DAS COLUNAS
        for col, texto in enumerate(headers):
            label = ctk.CTkLabel(janela_busca, text=texto, font=("Arial", 12, "bold"))
            label.grid(row=0, column=col, padx=5, pady=(5, 10))

        for idx, (matricula) in enumerate(resultado, start=1): # # AQUI É ONDE A FUNÇÃO LISTAR_ALUNO_UM RETORNA UMA TUPLA, ENTÃO PRECISAMOS ITERAR PARA PEGAR OS VALORES INDIVIDUAIS
        # Entrys
            entry_matricula = ctk.CTkEntry(janela_busca, width=40, height=42)
            entry_matricula.insert(0, matricula[0])  # RETORNA A MATRÍCULA
            entry_matricula.configure(state="readonly")  # Matricula não pode ser alterada
            entry_matricula.grid(row=idx, column=0, padx=5, pady=5)

            entry_cpf = ctk.CTkEntry(janela_busca, width=100, height=42)
            entry_cpf.insert(0, matricula[1]) # RETORNA O CPF
            entry_cpf.configure(state="readonly") # Não pode ser alterado
            entry_cpf.grid(row=idx, column=1, padx=5, pady=5)

            entry_nome = ctk.CTkEntry(janela_busca, width=120, height=42)
            entry_nome.insert(0, matricula[2]) # RETORNA O NOME
            entry_nome.grid(row=idx, column=2, padx=5, pady=5)

            entry_email = ctk.CTkEntry(janela_busca, width=200, height=42)
            entry_email.insert(0, matricula[3]) # RETORNA O EMAIL
            entry_email.grid(row=idx, column=3, padx=5, pady=5)

            entry_senha = ctk.CTkEntry(janela_busca, width=80, show="*", height=42)
            entry_senha.insert(0, matricula[4]) # RETORNA A SENHA
            entry_senha.grid(row=idx, column=4, padx=5, pady=5)

            matricula = list(matricula) # CONVERTE A TUPLA EM LISTA PARA PODER ALTERAR O STATUS
            if matricula[5] == 1: # SE O STATUS FOR 1, O ALUNO ESTÁ ATIVO
                matricula[5] = "Ativo"
            else:
                matricula[5] = "Inativo"

            entry_status = ctk.CTkEntry(janela_busca, width=50, height=42)
            entry_status.insert(0, matricula[5]) # RETORNA O STATUS
            entry_status.grid(row=idx, column=5, padx=5, pady=5)
       
    #INTERFACE DA TELA DE CONSULTA
    container = ctk.CTkFrame(consulta_tab)
    container.pack(expand=True, fill="both" )

    titulo = ctk.CTkLabel(container, text="Consulta", font=("Arial", 24, "bold")) # TÍTULO DA TELA DE CONSULTA
    titulo.pack(pady=20)

    botao_buscar = ctk.CTkButton(container, text="Buscar", height=40, command=mostrar_alunos) # BOTÃO PARA MOSTRAR TODOS OS ALUNOS CADASTRADOS
    botao_buscar.pack(pady=10)

    botao_buscar = ctk.CTkButton(container, text="Buscar Por Matrícula",height=40, command=mostrar_aluno) # BOTÃO PARA MOSTRAR UM ALUNO CADASTRADO(PELA BUSCA DA MATRÍCULA)
    botao_buscar.pack(pady=10)

    selecionar = CTkComboBox(container, values=["Aluno", "Professor"], width=200, height=50, state="readonly") # COMBOBOX PARA SELECIONAR O TIPO DE CONSULTA (ALUNO OU PROFESSOR)
    selecionar.pack(padx=5, pady=5)
    selecionar.set("Aluno") # SETANDO O VALOR INICIAL DO COMBOBOX PARA ALUNO

    entry_buscar = ctk.CTkEntry(container, placeholder_text="DIGITE A MATRÍCULA DO ALUNO OU PROFESSOR!") # ENTRY PARA BUSCAR A MATRICULA 
    entry_buscar.pack(pady=10, padx=20, fill="x")

    janela_busca = ctk.CTkScrollableFrame(container) # FRAME SCROLLABLE PARA MOSTRAR OS DADOS DOS ALUNOS CADASTRADOS
    janela_busca.pack(expand=True, fill="both", padx=20, pady=20)
