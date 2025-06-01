from customtkinter import *
from View.Frames.TelaPerfil import TelaPerfil
from View.Frames.TelaNota import TelaNota

def TelaAluno(main, dados, nivel, callback_logout):
    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin(main, callback_logout)
        return

    menu = CTkTabview(main)
    menu.pack(fill="both", expand=True)

    notas_tab = menu.add("Notas")
    perfil_tab = menu.add("Perfil")

    TelaNota(notas_tab, dados)
    TelaPerfil(perfil_tab, dados, nivel, callback_logout)
   
