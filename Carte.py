#=============================================================================================================
#Nom de l'auteur : Arthur
#=============================================================================================================

#=============================================================================================================
#Definition de la Class
#=============================================================================================================

class Carte:
    """
        Class qui permets la gestion individuelle de chacune des cartes

        attributs:
            COULEUR (class String) :  Contient la couleur de la carte permettant de faciliter les affichages visuelles.
            PUISSANCE (class Int): Contient la puissance de la carte (2 < A) 
            NAME (class String) : Contient le nom de la Carte (A,R,D,V,...)
        Methode :
            __init__() [chiffre = None : Int, Type = None : Int] : Chiffre designe le chiffre de la carte (0 = A, 13 = R), Type designe la couleur. Initialise l'ensemble des attributs de la carte couleur, puissance, nom ext.
            __str__() []: Permets de convertir la Class Carte en str de manière plus appropriées.
            get_winner() [card: List]: Permets d'obtenir la meilleur carte dans la liste.
    """
    def __init__(self, chiffre = None, type = None):
        """
        Chiffre designe le chiffre de la carte (0 = A, 13 = R), Type designe la couleur. Initialise l'ensemble des attributs de la carte couleur, puissance, nom ext.
        
        Keyword arguments:
        chiffre -- La valeur du chiffre correspondra a sa puissance (default None)
        type -- La couleur de la carte (default None)

        Return value : 
        None
        """
        if chiffre != None and type != None:
            self.COULEUR = couleur[type]
            if chiffre == 0:
                self.PUISSANCE = 13
            else:
                self.PUISSANCE = chiffre
            self.NAME = carte[self.PUISSANCE]
    def __str__(self):
        """
        Permets de convertir la Class Carte en str de manière plus appropriées.
        Keyword arguments:

        Return value : 
        L'ecrit de la Carte (String)
        """
        return f"{self.NAME}{self.COULEUR}"
    def get_winner(card):
        """
        Permets d'obtenir la meilleur carte dans la liste.

        Keyword arguments:
        card -- Liste contenant l'ensemble des cartes mis en concurrence ()
        
        Return value : 
        La meilleur des cartes
        """
        cardvar = card[0]
        for i in range(1, len(card)): #Passe une a une les cartes present dans la liste pour trouver la meilleur
            if cardvar.PUISSANCE == card[i].PUISSANCE:
                return False
            elif cardvar.PUISSANCE < card[i].PUISSANCE:
                cardvar = card[i]
        return cardvar
    






#============================================================================================================= 
#Programme Principal / Programme de Test
#=============================================================================================================
couleur = ["Trefle", "Pique", "Carreau", "Coeur"]
carte = ["ANTIBUG", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]

if __name__ == '__main__':
    list = [Carte(10, 2), Carte(0, 3), Carte(3, 2)]
    print(Carte.get_winner(list))