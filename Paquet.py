#=============================================================================================================
#Nom de l'auteur : Lucien et Theo
#=============================================================================================================


#=============================================================================================================
#Import
#=============================================================================================================
from Carte import *
import random

#=============================================================================================================
#Definition de la Class
#=============================================================================================================

#=============================================================================================================
#Nom de l'auteur : Theo
#=============================================================================================================
class Paquet:
    """
        Class qui permets la gestion des paquets. 
        attribut :
            container (class List) : Contient l'ensemble des cartes du paquet
        methode:
            __init__() [type : String] : Permets de crée un paquet de carte de plusieurs type (Pioche, Tas, Paquet Joueur)
            __iter__() [] : Permets de modifier le fonctionnement des iterations pour la class Paquet
            __len__() [] : Renvoie la longueur de la liste
            __str__() [] : En cas de conversions en str de la class Paquet il permet une gestion avancé de la conversion
            get_card() [] : Renvoie la carte au dessus du paquet
            ajouter() [card : Carte] : Ajoute une carte en dessous du paquet
            enlever() [] : Renvoie la première carte au dessus du paquet en plus de supprimer celle-ci du paquet
            melanger() [] : Modifie le paquet de sorte a que le container soit completement modifiée
            distribution() [num : int]: Renvoie une liste contenant l'ensemble des paquets. Le nombre de paquet retourner dans la liste corresponds a la variable num.
            get_container_str() [invisible: Boolean] : Methode utile pour la partie graphique pour afficher l'ensemble des cartes present dans le paquet. Si le boolean est True alors une carte sur deux est remplacée par CR (Carte Retournée)
    """
    def __init__(self, type):
        """
        Constructeur(), Permets de crée un paquet de carte de plusieurs type (Pioche, Tas, Paquet Joueur)

        Keyword arguments:
        type -- Defini le type du paquet seul le type PIOCHE a un impacte sur le code (default)

        Return value : 
        None
        """
        
        self.container = []
        if type == "PIOCHE":
            
            for p in range(13):
                for i in range(4):
                    self.container.append(Carte(p, i))
        
    def __iter__(self):
        """
        Permets de modifier le fonctionnement des iterations pour la class Paquet
        Keyword arguments:
        None

        Return value : 
        self.container (list)
        """
        
        return iter(self.container)
#=============================================================================================================
#Nom de l'auteur : Lucien
#=============================================================================================================

    def get_card(self):
        """
         Renvoie la carte au dessus du paquet

        Keyword arguments:
        None

        Return value : 
        Première carte
        """
        
        return self.container[-1]
    def ajouter(self, card):
        """
        Ajoute une carte en dessous du paquet
        Keyword arguments:
        card -- Une carte de class Carte

        Return value : 
        None
        """
        
        self.container.append(card)
    def enlever(self):
        """
        Renvoie la première carte au dessus du paquet en plus de supprimer celle-ci du paquet
        Keyword arguments:
        None

        Return value : 
        Première carte du paquet
        """
        
        assert len(self.container) > 0
        s = self.container[0]
        self.container.pop(0)
        return s
    def __str__(self):
        """
        En cas de conversions en str de la class Paquet il permet une gestion avancé de la conversion
        Keyword arguments:
        None

        Return value : 
        Renvoie self.container de manière plus jolie (String)
        """
        
        temp = f"["
        for i in self.container:
          
            if i.COULEUR == "Trefle":
                temp +=f"{i.NAME}♣"
            elif i.COULEUR == "Pique":
                temp +=f"{i.NAME}♠"
            elif i.COULEUR == "Carreau":
                temp +=f"{i.NAME}♦"
            elif i.COULEUR == "Coeur":
                temp +=f"{i.NAME}♥"
            temp+=f","
        temp += f"]"
        return f"{temp}"
#=============================================================================================================
#Nom de l'auteur : Theo
#=============================================================================================================

    def __len__(self):
        """
        Renvoie la longueur de la liste

        Keyword arguments:
        None

        Return value : 
        len(self.container) [list]
        """
        
        return len(self.container)
    def melanger(self):
        """
        Modifie le paquet de sorte a que le container soit completement melanger

        Keyword arguments:
        None

        Return value : 
        None
        """
    
        temp = self.container
        random.shuffle(temp)
        self.container = temp
    def distribution(self, num):
        """
        Renvoie une liste contenant l'ensemble des paquets. Le nombre de paquet retourner dans la liste corresponds a la variable num.
            
        Keyword arguments:
        num -- Le nombre de Paquet joueur devant être crée

        Return value : 
        List contenant l'ensemble des paquets des joueurs
        """
        
        list_paquet, x = [], 0
        for i in range(num): list_paquet.append(Paquet("JEU"))
        for i in range(len(self.container)):
            list_paquet[x].ajouter(self.enlever())
            if x >= num-1:
                x=0
            else:
                x+=1
        return list_paquet
    def get_container_str(self, invisible):
        """
        Methode utile pour la partie graphique pour afficher l'ensemble des cartes present dans le paquet. Si le boolean est True alors une carte sur deux est remplacée par CR (Carte Retournée)
    
        Keyword arguments:
        invisible -- Boolean qui permets de definir si une carte sur deux doit être invisible

        Return value : 
        Renvoie self.container de manière plus jolie
        """
        temp = ""
        for p,i in enumerate(self.container):
            if invisible and p % 2 == 0:
                temp += f"{i.NAME}{'♣' if i.COULEUR == 'Trefle' else '♠' if i.COULEUR == 'Pique' else '♦' if i.COULEUR == 'Carreau' else '♥'}|"
            elif not invisible:
                temp += f"{i.NAME}{'♣' if i.COULEUR == 'Trefle' else '♠' if i.COULEUR == 'Pique' else '♦' if i.COULEUR == 'Carreau' else '♥'}|"
            else:
                temp += "CR|"
        return temp



#============================================================================================================= 
#Programme Principal / Programme de Test
#=============================================================================================================
if __name__ == '__main__':
    paquet = Paquet("PIOCHE")
    print(paquet)
    paquet.melanger()
    print(paquet)
    paquet.distribution(2)