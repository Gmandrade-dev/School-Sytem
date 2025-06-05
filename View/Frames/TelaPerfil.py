from customtkinter import *
from Controller.EditarUserController import EditarUserController, VerificarSenhaController, EditarSenhaController
from tkinter import messagebox

def TelaPerfil(frame, dados, tabela, callback_logout):
    try:
        if not dados:
          callback_logout

        def sair_conta():
            # Em vez de destruir frame e chamar TelaLogin diretamente,
            # chamamos o callback que volta para a tela de login no main
            callback_logout()

        def editar_campos():
            matricula = campo_matricula.get()
            nome = campo_nome.get()
            email = campo_email.get()
            cpf = campo_cpf.get()

            resultado = EditarUserController(matricula, nome, email, cpf, tabela)
            if resultado:
                messagebox.showinfo("Sucesso", "Dados editados com sucesso!")
            else:
                messagebox.showerror("Erro", "Erro ao editar dados.")

        def editar_senha():   
            matricula = campo_matricula.get()
            senha_atual_hash = senha
            senha_antiga_digitada = campo_senha_antiga.get()
            senha1 = nova_senha.get()
            senha2 = nova_senha2.get()

            resultadoSenha = VerificarSenhaController(senha_atual_hash, senha_antiga_digitada, senha1, senha2)
            if resultadoSenha:
                resultado = EditarSenhaController(matricula, senha1, tabela)
                if resultado:
                    messagebox.showinfo("Sucesso", "Senha editada com sucesso!")
                else:
                    messagebox.showerror("Erro", "Erro ao editar senha.")  
            else:
                messagebox.showerror("Erro", "Senha antiga incorreta ou novas senhas não coincidem.")

        matricula, cpf, email, senha, nome = dados

        container = CTkFrame(frame)
        container.pack(expand=True)

        titulo = CTkLabel(container, text="Perfil", font=("Calibri", 20))
        titulo.pack(pady=(10, 20))

        linha1 = CTkFrame(container, fg_color="transparent")
        linha1.pack(pady=5)

        frame_matricula = CTkFrame(linha1, fg_color="transparent")
        frame_matricula.pack(side="left", padx=10)
        label_matricula = CTkLabel(frame_matricula, text="Matrícula", font=("Calibri", 15))
        label_matricula.pack(anchor="w")
        campo_matricula = CTkEntry(frame_matricula, width=200, height=50)
        campo_matricula.insert(0, matricula)
        campo_matricula.configure(state="readonly")
        campo_matricula.pack()

        frame_nome = CTkFrame(linha1, fg_color="transparent")
        frame_nome.pack(side="left", padx=10)
        label_nome = CTkLabel(frame_nome, text="Nome", font=("Calibri", 15))
        label_nome.pack(anchor="w")
        campo_nome = CTkEntry(frame_nome, width=200, height=50)
        campo_nome.insert(0, nome)
        campo_nome.pack()

        linha2 = CTkFrame(container, fg_color="transparent")
        linha2.pack(pady=5)

        frame_email = CTkFrame(linha2, fg_color="transparent")
        frame_email.pack(side="left", padx=10)
        label_email = CTkLabel(frame_email, text="Email", font=("Calibri", 15))
        label_email.pack(anchor="w")
        campo_email = CTkEntry(frame_email, width=200, height=50)
        campo_email.insert(0, email)
        campo_email.pack()

        frame_cpf = CTkFrame(linha2, fg_color="transparent")
        frame_cpf.pack(side="left", padx=10)
        label_cpf = CTkLabel(frame_cpf, text="CPF", font=("Calibri", 15))
        label_cpf.pack(anchor="w")
        campo_cpf = CTkEntry(frame_cpf, width=200, height=50)
        campo_cpf.insert(0, cpf)
        campo_cpf.configure(state="readonly")
        campo_cpf.pack()

        botao_editar_campos = CTkButton(container, text="Editar Campos", width=420, height=40, command=editar_campos)
        botao_editar_campos.pack(pady=(10, 15))

        textosenha = CTkLabel(container, text="Alterar Senha", font=("Calibri", 15))
        textosenha.pack(pady=(0, 5))

        frame_senha_antiga = CTkFrame(container, fg_color="transparent")
        frame_senha_antiga.pack(pady=5)
        campo_senha_antiga = CTkEntry(frame_senha_antiga, width=420, height=50, show="*", placeholder_text="Digite a senha antiga")
        campo_senha_antiga.pack()

        linha3 = CTkFrame(container, fg_color="transparent")
        linha3.pack(pady=5)

        nova_senha = CTkEntry(linha3, width=200, height=50, show="*", placeholder_text="Digite a nova senha")
        nova_senha.pack(side="left", padx=10)

        nova_senha2 = CTkEntry(linha3, width=200, height=50, show="*", placeholder_text="Repita a nova senha")
        nova_senha2.pack(side="left", padx=10)

        botao_editar_senha = CTkButton(container, text="Editar Senha", width=420, height=40, command=editar_senha)
        botao_editar_senha.pack(pady=(10, 15))

        botao_sair = CTkButton(container, text="Sair da Conta", width=420, height=40, fg_color="#be2727", hover_color="#cc0000", command=sair_conta)
        botao_sair.pack(pady=(10, 20))

    except Exception as e:
        print(f"Erro ao obter dados: {e}")
