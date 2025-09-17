'''
Main Funcntion
    It needs to call the functions previously established
    And to have a interface that with a button, can check the user directory and if winrar, java and office 2010
    are installed, and return all of them.
    After this, it will procede to with Inno Setup and install all that is needed.
'''
from tkinter import ttk
from tkinter import *
import sys
from PIL import Image, ImageTk
import os
from functions_homolog import *


# Função para obter caminho base do programa (suporta .exe)
def resource_path(relative_path):
    """Retorna caminho absoluto, mesmo quando empacotado em .exe"""
    if getattr(sys, 'frozen', False):
        # Se estiver rodando como executável
        base_path = sys._MEIPASS
    else:
        # Rodando como script .py
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

#Configurações
COR_FUNDO = "grey"     # cor de fundo das janelas
COR_FONTE = "white"       # cor do texto

class HomologMix:
    def __init__(self, master=None):
        master.config(bg=COR_FUNDO)

        # Frame principal
        self.Widget1 = Frame(master, bg=COR_FUNDO)
        self.Widget1.pack()
        self.msg = Label(self.Widget1,
                         text="HomologMix",
                         font=("Calibri", "9", "italic"),
                         bg=COR_FUNDO,
                         fg=COR_FONTE)
        self.msg.pack()

        # Frame da checagem geral
        self.Widget_all_tests = Frame(master, bg=COR_FUNDO)
        self.Widget_all_tests.pack()
        self.msg = Label(self.Widget_all_tests,
                         text="Teste geral",
                         font=("Calibri", "9", "italic"),
                         bg=COR_FUNDO,
                         fg=COR_FONTE)
        self.msg.pack()

        # Frame da homologação
        self.widget_Homolog = Frame(master, bg=COR_FUNDO)
        self.widget_Homolog.pack()

        # Botão homologação
        self.homolog_button = Button(self.widget_Homolog,
                                     font=("Calibri", "9", "italic"),
                                     text="Inicie a homologação!",
                                     bg=COR_FUNDO,
                                     fg=COR_FONTE,
                                     activebackground=COR_FUNDO,
                                     activeforeground=COR_FONTE,
                                     width=40)
        self.homolog_button.bind("<Button-1>", self.homolog_Setup)
        self.homolog_button.pack()

        # Botão checagem geral
        self.check_button = Button(self.Widget_all_tests,
                                   font=("Calibri", "9", "italic"),
                                   text="Checagem geral",
                                   bg=COR_FUNDO,
                                   fg=COR_FONTE,
                                   activebackground=COR_FUNDO,
                                   activeforeground=COR_FONTE,
                                   width=40)
        self.check_button.bind("<Button-1>", self.allChecker)
        self.check_button.pack()

    def allChecker(self, event):
        falses = homolog_check()
        if falses:
            self.msg["text"] = "Os seguintes itens não estão corretos:\n" + "\n".join(falses)
        else:
            self.msg["text"] = "Todas as checagens deram certo! Prosseguindo com a homologação básica da máquina..."

    def homolog_Setup(self, event):
        if check_User():
            janela2 = Toplevel()
            janela2.title("Usuário incorreto!")
            janela2.config(bg=COR_FUNDO)
            label_nome = Label(janela2,
                               text="Usuário incorreto! Não é possível prosseguir com a homologação!",
                               bg=COR_FUNDO,
                               fg=COR_FONTE)
            label_nome.grid(row=0, column=0)
            return_button = Button(janela2,
                                   text='Fechar',
                                   command=sys.exit,
                                   bg=COR_FUNDO,
                                   fg=COR_FONTE,
                                   activebackground=COR_FUNDO,
                                   activeforeground=COR_FONTE)
            return_button.grid(row=1, column=0)


#Janela principal
homologmix = Tk()
homologmix.title("Homolog Mix")
homologmix.geometry("300x250")
homologmix.config(bg=COR_FUNDO)

#Style
style = ttk.Style(homologmix)
style.theme_use("default")

#Icone
homologmix.iconbitmap(resource_path(os.path.join("assets", "images", "HomologMixx.ico")))


#Inicia a interface
app = HomologMix(homologmix)

homologmix.mainloop()
