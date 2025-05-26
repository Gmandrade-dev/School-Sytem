from customtkinter import *
from View.TelaPerfil import TelaPerfil
from View.TelaCadrastar import TelaCadastrar

def TelaProfessor(main, dados,user_nivel, callback_logout):
    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin(main, callback_logout)
        return

    menu = CTkTabview(main)
    menu.pack(fill="both", expand=True)

    
    notas_tab = menu.add("Notas")
    lancamento_tab = menu.add("Lançamento")
    cadastro_tab = menu.add("Cadastro")
    displina_tab = menu.add("Disciplinas")
    perfil_tab = menu.add("Perfil")


    TelaPerfil(perfil_tab, dados, user_nivel, callback_logout)
    TelaCadastrar(cadastro_tab, dados,user_nivel,callback_logout)
    
    # TelaLancamento(lancamento_tab, dados)
    # TelaNota(notas_tab, dados)
