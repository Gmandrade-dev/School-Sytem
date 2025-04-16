import tkinter as tk
from tkinter import ttk
 
# Função chamada ao clicar no botão "Enviar"
def enviar():
    nome = entry_nome.get()
    email = entry_email.get()
    idade = entry_idade.get()
    genero = combo_genero.get()
    tipo = tipo_usuario.get()
    resultado["text"] = f"Nome: {nome}\nEmail: {email}\nIdade: {idade}\nGênero: {genero}\nTipo: {tipo}"
 
# Função para limpar os campos
def limpar():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    combo_genero.set("")
    tipo_usuario.set(None)
    resultado["text"] = ""
 
# Criar a janela principal
janela = tk.Tk()
janela.title("Formulário com Radiobutton e Combobox")
janela.geometry("fullsreen")
 
# Mensagem inicial
tk.Label(janela, text="Preencha os dados abaixo:", font=("Arial", 12, "bold")).pack(pady=10)
 
# Campo Nome
tk.Label(janela, text="Nome:").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()
 
# Campo Email
tk.Label(janela, text="Email:").pack()
entry_email = tk.Entry(janela)
entry_email.pack()
 
# Campo Idade
tk.Label(janela, text="Idade:").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()
 
# Combobox para Gênero
tk.Label(janela, text="Gênero:").pack()
combo_genero = ttk.Combobox(janela, values=["Masculino", "Feminino", "Outro", "Prefiro não dizer"])
combo_genero.pack()
 
# Radiobuttons para Tipo de Usuário
tk.Label(janela, text="Tipo de Usuário:").pack()
tipo_usuario = tk.StringVar(value=None)  # armazena o valor selecionado
 
tk.Radiobutton(janela, text="Aluno", variable=tipo_usuario, value="Aluno").pack(anchor="w", padx=20)
tk.Radiobutton(janela, text="Professor", variable=tipo_usuario, value="Professor").pack(anchor="w", padx=20)
tk.Radiobutton(janela, text="Visitante", variable=tipo_usuario, value="Visitante").pack(anchor="w", padx=20)
 
# Botões
tk.Button(janela, text="Enviar", command=enviar).pack(pady=5)
tk.Button(janela, text="Limpar", command=limpar).pack(pady=5)
 
# Resultado
resultado = tk.Label(janela, text="", fg="blue")
resultado.pack(pady=10)
 
# Iniciar a interface
janela.mainloop()