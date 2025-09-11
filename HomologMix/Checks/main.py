'''
Main Funcntion
    It needs to call the functions previously established
    And to have a interface that with a button, can check the user directory and if winrar, java and office 2010
    are installed, and return all of them.
    After this, it will procede to with Inno Setup and install all that is needed.
'''

from checkUser import check_User
from checkWinrar import checkWinrar
from checkOffice import checkOffice
from checkJava import checkJava
from tkinter import *
from booleanChecker import function_checker


class HomologMix:
    def __init__(self, master=None):

        self.Widget1 = Frame(master)
        self.Widget1.pack()
        self.msg = Label(self.Widget1, text="HomologMix")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()

        self.Widget_all_tests = Frame(master)
        self.Widget_all_tests.pack()
        self.msg = Label(self.Widget_all_tests, text="Teste geral")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()

        self.check_button = Button(self.Widget_all_tests)
        self.check_button["font"] = ("Calibri", "9", "italic")
        self.check_button["text"] = "Checagem"
        self.check_button["width"] = 40
        self.check_button.bind("<Button-1>", self.allChecker)
        self.check_button.pack()


    def allChecker(self, event):
        falses = function_checker()

        if falses:
            self.msg["text"] = "Os seguintes itens não estão corretos:\n" + "\n".join(falses)
        else:
            self.msg["text"] = "Todas as checagens deram certo! Prosseguindo com a homologação básica da máquina..."



root = Tk()
HomologMix(root)
root.mainloop()