class Personnage:
    """
       Attributes:
           energie_depart_defaut (int): L'énergie de départ par défaut
           energie_depart_min (int): L'énergie de départ minimum
           energie_max (int): L'énergie maximum en tout temps
           longueur_nom_min (int) : La longueur minimale du nom
           longueur_nom_max (int) : La longueur maximale du nom
           nom (str) : Le nom
           energie_depart (int): L'énergie de départ
           energie_courante (int): L'énergie courante

       """
    energie_depart_defaut = 20
    energie_depart_min = 1
    energie_max = 100
    longueur_nom_min = 3
    longueur_nom_max = 30
    nom = " "
    energie_depart = 0
    energie_courante = 0

    def __init__(self, nom=nom, energie_depart=energie_depart_defaut):
        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """
        self.nom = nom
        self.energie_depart = energie_depart
        self.energie_courante = energie_depart

    def reset_energie(self):
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """
        self.energie_courante = self.get_energie_depart()

    def est_mort(self):
        """
        Retourne vrai lorsque l’énergie du personnage est à 0.
        Returns (bool): True si le personnage est mort, False sinon.
        """
        return self.get_energie_courante() == 0

    def valider_nom(self):
        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """
        return len(self.get_nom()) >= self.longueur_nom_min and len(self.get_nom()) <= self.longueur_nom_max

    def valider_energie_depart(self):
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """
        return self.get_energie_depart() >= self.energie_depart_min and self.get_energie_depart() <= self.energie_max

    def valider_energie_courante(self):
        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.

        """
        return self.get_energie_courante() >= 0 or self.get_energie_courante() <= self.energie_max

    def crier(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self):
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def to_string(self):
        """
        Affiche l'énergie du personnage en question
        """
        print("{} a une énergie de {}".format(self.get_nom(), self.get_energie_courante()))

    def get_energie_courante(self):
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """
        return self.energie_courante

    def set_energie_courante(self, energie_courante):
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_courante():
            return True
        else:
            return False

    def get_nom(self):
        """
        Retourne le nom.
        Returns (str): Le nom.
        """
        return self.nom

    def set_nom(self, nom):
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_nom():
            return True
        else:
            return False


    def get_energie_depart(self):
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """
        return self.energie_depart


    def set_energie_depart(self, energie_depart):
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """
        if self.valider_energie_depart():
            # self.energie_depart = self.energie_depart ???
            return True
        else:
            return False

if __name__ == "__main__":
    alicia = Personnage("Alicia", 30)
    assert alicia.energie_depart == 30
    assert alicia.nom == "Alicia"
    alicia.energie_courante = 20
    alicia.reset_energie()
    assert alicia.energie_courante == 30
    assert alicia.est_mort() == False
    assert alicia.valider_energie_courante() == True
    assert alicia.valider_nom() == True
    assert alicia.valider_energie_depart() == True
    