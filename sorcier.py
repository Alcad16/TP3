from personnage import Personnage

class Sorcier(Personnage):
    """
    Classe représentant un Sorcier. Hérite de Personnage.
    Attributes:
        nb_charmes_defaut (int): Le nombre de charmes par défaut
        nb_charmes_max (int): Le nombre de charmes maximum
        nb_charmes (int): Le nombre de charmes courant
    """
    nbr_charmes_defaut=20
    nbr_charmes_max=20
    nbr_charmes=0
    def __init__(self, nom, energie_depart, energie, nbr_charmes):
        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """

    def to_string(self):
        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """
        return "Le sorcier, {}, a une énergie de {} et {} charmes"\
            .format(self.get_nom(),self.get_energie_courante(),self.get_nbr_charmes())

    def valider_nbr_charmes(self, nb_charmes):
        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """
        return self.get_nbr_charmes()>=0 and self.get_nbr_charmes()<=self.nbr_charmes_max

    def crier(self):
        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """
        return "Je vais tous vous aneantir!"

    def attaquer(self, force_attaque):
        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """
        self.force_attaque=force_attaque
        if self.get_energie_courante()>self.force_attaque:
            sel.get_energie_courante-=self.force_attaque
        else:
            self.energie_courante=0

    def get_nbr_charmes(self):
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.

        """
        return self.nbr_charmes

    def set_nbr_charmes(self, nb_charmes):
        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """
        if int(self.set_nbr_charmes()):
            return True
        else:
            return False
