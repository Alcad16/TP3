
from tkinter import *
from tkinter.filedialog import *

from gestion_personnages import GestionPersonnages


class Interface(Frame):
    """
    Classe héritant d'un Frame de TKInter et permetant d'afficher et de gérer l'interface graphique.
    """
    gp = GestionPersonnages()

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
