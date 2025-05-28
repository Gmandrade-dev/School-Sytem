from customtkinter import *
from View.TelaPerfil import TelaPerfil
from View.TelaCadrastar import TelaCadastrar
from View.TelaGestao import TelaGestão
from View.TelaConsulta import TelaConsulta

def TelaProfessor(main, dados,user_nivel, callback_logout):
    if not dados:
        from View.TelaLogin import TelaLogin
        print("Dados não encontrados.")
        TelaLogin(main, callback_logout)
        return

    menu = CTkTabview(main)
    menu.pack(fill="both", expand=True)

    
    notas_tab = menu.add("Notas")
    gestao_tab = menu.add("Gestão")
    cadastro_tab = menu.add("Cadastro")
    displina_tab = menu.add("Disciplinas")
    perfil_tab = menu.add("Perfil")
    consulta_tab = menu.add("Consulta")


    TelaPerfil(perfil_tab, dados, user_nivel, callback_logout)
    TelaCadastrar(cadastro_tab, dados,user_nivel,callback_logout)
    TelaGestão(gestao_tab, dados, user_nivel, callback_logout)
    TelaConsulta(consulta_tab, dados, user_nivel, callback_logout)
    
    # TelaLancamento(lancamento_tab, dados)
    # TelaNota(notas_tab, dados)
