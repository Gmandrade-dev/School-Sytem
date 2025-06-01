from customtkinter import *
from View.Frames.TelaPerfil import TelaPerfil
from View.Frames.TelaCadrastar import TelaCadastrar
from View.Frames.TelaGestao import TelaGestao
from View.TelaConsulta import TelaConsulta

def TelaProfessor(main, dados,user_nivel, callback_logout):
    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin(main, callback_logout)
        return

    menu = CTkTabview(main)
    menu.pack(fill="both", expand=True)

    consulta_tab = menu.add("Consulta")
    # notas_tab = menu.add("Notas")
    gestao_tab = menu.add("Gestão")
    cadastro_tab = menu.add("Cadastro")
    # displina_tab = menu.add("Disciplinas")
    perfil_tab = menu.add("Perfil")
    


    TelaPerfil(perfil_tab, dados, user_nivel, callback_logout)
    TelaCadastrar(cadastro_tab, dados,user_nivel,callback_logout)
    TelaGestao(gestao_tab, dados, user_nivel, callback_logout)
    TelaConsulta(consulta_tab, dados, user_nivel, callback_logout)
    