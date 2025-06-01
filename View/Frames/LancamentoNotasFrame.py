import customtkinter as ctk
from tkinter import messagebox
from Controller.CadastrarController import CadastrarNotasController


def LancamentoNotasFrame(gestao_tab, callback_logou):
    def lancar_notas():
        matricula = mat_aluno.get().strip()
        disciplina = cod_disciplina.get().strip()

        if not matricula or not disciplina:
            messagebox.showerror("Erro", "Preencha a matrícula e a disciplina.")
            return

        try:
            av1 = float(nota1.get().strip())
        except ValueError:
            messagebox.showerror("Erro", "A nota AV1 é obrigatória e precisa ser um número válido.")
            return

        try:
            av2 = float(nota2.get().strip()) if nota2.get().strip() != '' else 0.0
        except ValueError:
            messagebox.showerror("Erro", "A nota AV2 precisa ser um número válido.")
            return

        try:
            av3 = float(nota3.get().strip()) if nota3.get().strip() != '' else 0.0
        except ValueError:
            messagebox.showerror("Erro", "A nota AV3 precisa ser um número válido.")
            return

        # Chamar o controller
        sucesso, mensagem = CadastrarNotasController(matricula, disciplina, av1, av2, av3)

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            # Limpar os campos após sucesso
            mat_aluno.delete(0, 'end')
            cod_disciplina.delete(0, 'end')
            nota1.delete(0, 'end')
            nota2.delete(0, 'end')
            nota3.delete(0, 'end')
        else:
            messagebox.showerror("Erro", mensagem)

    # Interface
    linha1 = ctk.CTkFrame(gestao_tab)
    linha1.pack(pady=5)

    textoNotas = ctk.CTkLabel(linha1, text="Lançamento de Notas", font=("Arial", 18, "bold"))
    textoNotas.pack(side="left", padx=5, pady=5)

    linha2 = ctk.CTkFrame(gestao_tab)
    linha2.pack(pady=5)

    mat_aluno = ctk.CTkEntry(linha2, placeholder_text="Matrícula do Aluno", height=40, width=230)
    mat_aluno.pack(side="left", pady=5, padx=5)

    cod_disciplina = ctk.CTkEntry(linha2, placeholder_text="ID da Disciplina", height=40, width=230)
    cod_disciplina.pack(side="left", pady=5, padx=5)

    linha3 = ctk.CTkFrame(gestao_tab)
    linha3.pack(pady=5)

    nota1 = ctk.CTkEntry(linha3, placeholder_text="AV1", height=40, width=100)
    nota1.pack(side="left", pady=5, padx=5)

    nota2 = ctk.CTkEntry(linha3, placeholder_text="AV2", height=40, width=100)
    nota2.pack(side="left", pady=5, padx=5)

    nota3 = ctk.CTkEntry(linha3, placeholder_text="AV3", height=40, width=100)
    nota3.pack(side="left", pady=5, padx=5)

    btnnota = ctk.CTkButton(linha3, text="Lançar Notas", height=40, command=lancar_notas)
    btnnota.pack(side="left", pady=5, padx=5)
