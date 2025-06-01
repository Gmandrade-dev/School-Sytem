from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
from View.Frames.LancamentoNotasFrame import LancamentoNotasFrame
from View.Frames.CadastroDisciplinaFrame import CadastroDisciplinaFrame
from View.Frames.ExibirNotasDisciplinas import ExibirNotasDisciplinas

def TelaGestao(gestao_tab, dados, user_nivel, callback_logou):

    if not dados:
        callback_logou()
        messagebox.showerror("Erro", "Dados não encontrados.")
        return
    
    CadastroDisciplinaFrame(gestao_tab, callback_logou)
    
    LancamentoNotasFrame(gestao_tab, callback_logou)
    
    ExibirNotasDisciplinas(gestao_tab, callback_logou)