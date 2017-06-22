from personnage import Personnage
class Guerrier(Personnage):
    """
    Classe représentant un Guerrier. Hérite de Personnage.
    Attributes:
        force_defaut (int): La valeur par défaut de la force
        force_max (int): La valeur maximum de la force
        perte_force_defaut (int): La perte de force lors d'une attaque
        gain_force_defaut (int): Le gain de force lors d'une resitution d'énergie
        force (int): La force courante du guerrier
    """
    force_defaut = 20
    force_max = 80
    perte_force_defaut = 2
    gain_force_defaut = 10
    force = 0

    def __init__(self, nom, energie_depart, force=force_defaut):
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """
        super().__init__(nom, energie_depart)
        self.energie_courante = energie_depart
        self.force = force
        self.force_attaque = 0
    def to_string(self):
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."

        Returns (str): La chaîne représentant le guerrier. 
        """
        return "Le guerrier, {}, a une énergie de valeur {} et une force de valeur {}"\
            .format(self.get_nom(), self.get_energie_courante(), self.get_force())

    def valider_force(self):
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).

        Returns (bool): True si la force est valide, False sinon
        """
        return self.get_force() >= 0 and self.get_force() <= self.force_max

    def crier(self):
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """
        return "Vous allez goûter à la puissance de mon épée!"

    def attaquer(self, force_attaque):
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """
        self.force_attaque = force_attaque
        if self.get_energie_courante() > self.force_attaque:
            self.energie_courante -= self.force_attaque
            if self.get_force() > self.perte_force_defaut:
                self.force -= self.perte_force_defaut
            else:
                self.force = 0
        else:
            self.energie_courante = 0
            self.force = 0

    def reset_energie(self):
        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """
        self.energie_courante = self.get_energie_depart()
        if self.get_force() + self.gain_force_defaut < self.force_max:
            self.force += self.gain_force_defaut
        else:
            self.force = self.force_max

    def get_force(self):
        """
        Retourne la force.
        Returns (int): La force.
        """
        return self.force

    def set_force(self):
        """
        Assigne le nom s'il est valide. 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_force():
            return True
        else:
            return False

if __name__ == "__main__":
    ouellet = Guerrier("Ouellet", 30, 50)
    assert ouellet.nom == "Ouellet"
    assert ouellet.energie_courante == 30
    assert ouellet.valider_force()
    assert ouellet.force == 50
    ouellet.attaquer(20)
    assert ouellet.energie_courante == 10
    assert ouellet.force == 48
    ouellet.reset_energie()
    assert ouellet.energie_courante == 30
    assert ouellet.force == 58
    ouellet.attaquer(30)
    assert ouellet.energie_courante == 0
    assert ouellet.force == 0
    ouel = Guerrier("Ouel", 30, 72)
    ouel.reset_energie()
    assert ouel.force == 80
