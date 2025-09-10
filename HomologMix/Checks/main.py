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

class HomologMix:
    def __init__(self, master=None):
        self.bv = Frame(master)
        self.bv.pack()
        self.msg = Label(self.bv, text="Homolog Mix")
        self.msg["font"] = ("Arial", "10", "bold", "italic")
        self.msg.pack()
        self.iniciar = Button(self.bv)
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Arial", "10")
        self.iniciar["width"] = 5
        self.iniciar["height"] = 1
        self.iniciar["command"] = self.bv.quit
        self.iniciar.pack (side=RIGHT)
root = Tk()
HomologMix(root)
root.mainloop()