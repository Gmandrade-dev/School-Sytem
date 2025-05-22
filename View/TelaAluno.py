from customtkinter import *
from View.TelaPerfil import TelaPerfil
from View.TelaNota import TelaNota

def TelaAluno(frame, dados):

    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin()  
        return  

    menu = CTkTabview(frame)
    
    menu.pack(pady=5, padx=5, fill="both", expand=True)
    menu.add("Notas")
    menu.add("Perfil")
    
    notas_tab  = menu.tab("Notas")
    perfil_tab = menu.tab("Perfil")

    TelaNota(notas_tab, dados)
    TelaPerfil(perfil_tab, dados)
