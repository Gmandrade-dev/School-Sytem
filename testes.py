import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def mostrar_erro():
    messagebox.showerror("Erro", "Algo deu errado!")

def mostrar_info():
    messagebox.showinfo("Informação", "Operação realizada com sucesso!")

def mostrar_aviso():
    messagebox.showwarning("Aviso", "Você tem certeza?")

app = ttk.Window(themename="darkly")
app.title("Exemplo de Message Box")

ttk.Button(app, text="Mostrar Erro", command=mostrar_erro).pack(pady=10)
ttk.Button(app, text="Mostrar Informação", command=mostrar_info).pack(pady=10)
ttk.Button(app, text="Mostrar Aviso", command=mostrar_aviso).pack(pady=10)

app.mainloop()
