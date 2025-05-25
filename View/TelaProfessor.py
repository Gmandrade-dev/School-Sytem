from customtkinter import *
from View.TelaPerfil import TelaPerfil

def TelaProfessor(main, dados, nivel, callback_logout):
    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin(main, callback_logout)
        return

    menu = CTkTabview(main)
    menu.pack(fill="both", expand=True)

    perfil_tab = menu.add("Perfil")

    TelaPerfil(perfil_tab, dados, nivel, callback_logout)
