import tkinter as tk
 
# Funções para os botões
def dizer_ola():
    texto["text"] = "Olá! Você clicou no primeiro botão."
 
def dizer_tchau():
    texto["text"] = "Tchau! Você clicou no segundo botão."
 
# Criar a janela principal
janela = tk.Tk()
janela.title("Exemplo com Dois Botões")
janela.geometry("300x200")
 
# Rótulo de texto
texto = tk.Label(janela, text="Clique em um dos botões abaixo:")
texto.pack(pady=20)
 
# Primeiro botão
botao1 = tk.Button(janela, text="Dizer Olá", command=dizer_ola)
botao1.pack(pady=5)
 
# Segundo botão
botao2 = tk.Button(janela, text="Dizer Tchau", command=dizer_tchau)
botao2.pack(pady=5)
 
# Iniciar a interface
janela.mainloop()