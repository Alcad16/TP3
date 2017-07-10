import tkinter as tk
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
        self.widget_personnages = Listbox(self, exportselection=False)
        self.widget_personnages.grid(row=0, column=1,  padx=5, pady=5)
        self.bouton_creer_sorcier = Button(text="Créer un sorcier", height=5, width=40)
        self.bouton_creer_sorcier.grid(row=0, column=2, padx=5, pady=5)
        self.bouton_creer_guerrier = Button(text="Créer un guerrier", height=5, width=40)
        self.bouton_creer_guerrier.grid(row=1, column=2, padx=5, pady=5)
        self.bouton_attaquer = Button(text="Attaquer", height=5, width=40)
        self.bouton_attaquer.grid(row=2, column =2, padx=5, pady=5)
        self.bouton_reinitialiser = Button(text="Réinitialiser l'énergie", height=5, width=40)
        self.bouton_reinitialiser.grid(row=3, column=2, padx=5, pady=5)
        self.bouton_crier = Button(text="Crier", height=5, width=40)
        self.bouton_crier.grid(row=4, column=2, padx=5, pady=5)


    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")

if __name__ == "__main__":
    # Instanciation de la fenêtre et démarrage de sa boucle principale.
    root = tk.Tk()
    fenetre = Interface(root)
    root.mainloop()