#=============================================================================================================
#Nom de l'auteur : Arthur, (Un peu Lucien et Theo auu niveau de l'idée de conception pour être fonctionnel avec les autres class)
#=============================================================================================================

#=============================================================================================================
#Import
#=============================================================================================================


from random import *
from Carte import *
from Paquet import *
import time
#=============================================================================================================
#Definition d'une Class
#=============================================================================================================

class Main:
    """!
        Class qui permets de lancer une partie theorique.

        attributs:
            PLAYER (class Int) : Indique le nombre de joueur dans la partie.
            tour (class Int) : Permets d'indiquer le nombre de tour qui s'est passé
            players (class List) : Contient les deux paquets des Joueurs
            terrains (class List) : Contient les deux terrains des Joueurs
            lock (class Boolean) : Si True aucune interaction n'est possible dans le code. 
            type (class String) : Type de lancement (None : Theorique, App : Lancement via l'Application)
            PIOCHE (class Paquet): Contient la pioche est permets par la suite de faire l'ensemble des melanges
            value (class Boolean): Si True or False = Partie terminée, True or False determine si tu as gagnés ou non. Cas autre = Partie pas fini
        methode:
            __init__() []: Constructeur, Contient l'ensemble des parametres obligatoires au lancement d'une partie.
            start() [type = None : String] : Le parametres designe le type de demarrage (Lancement via Console, Lancement via App) et le code sert a mettre en place le lancement d'une partie avec distribution des cartes ext.
            play() []: Cet fonction fait que chaque joueur pose une carte dans leur terrain
            verify() []: Cet fonction verifie plein de propriete liée au carte posé sur la table et fait differentes choses en fonction de ses propriete (Bataille, Gain, Plus de carte, ext)
    """
    def __init__(self):
        """
        Constructeur, Contient l'ensemble des parametres obligatoires au lancement d'une partie.        

        Keyword arguments:
        None

        Return value : 
        None
        """
        self.PLAYER = 2
        self.tour = 0
        self.players = None
        self.terrains = None
        self.lock = False

    def start(self, type= None, Stop = False, Logs = False):
        """
        La methode sert a mettre en place le lancement d'une partie avec distribution des cartes ext.

        Keyword arguments:
        type -- launching type  (Lancement via Console, Lancement via App) (default None)
        Stop -- Mets en pause le code a un point X (default False)
        Logs -- Active les logs permettant de voir chaqu'un des paquet (default False)
        Return value : 
        None
        """
        self.STOP = Stop
        self.LOGS = Logs
        PIOCHE = Paquet("PIOCHE")
        PIOCHE.melanger()
        self.players = PIOCHE.distribution(self.PLAYER)
        self.terrains = [Paquet("Terrain") for _ in range(self.PLAYER)]
        self.type = type
        if type == None:
            while len(self.players) > 1:
                
                value = self.verify()
                if value is True:
                    print("Vous avez gagné")
                elif value is False:
                    print("Vous avez perdu")
                else:
                    self.play()
            print(self.tour)
        return

    def play(self):
        """
        Cet fonction fait que chaque joueur pose une carte dans leur terrain

        Keyword arguments:
        None

        Return value : 
        None
        """
        self.tour += 1
            
        for i, player in enumerate(self.players):
            self.terrains[i].ajouter(player.enlever())
        if self.type != None:
            time.sleep(0.1)
            self.lock = False

    def verify(self):
        """
        Cet fonction verifie plein de propriete liée au carte posé sur la table et fait differentes choses en fonction de ses propriete (Bataille, Gain, Plus de carte, ext)

        Keyword arguments:
        None

        Return value : 
        None
        """
        if len(self.terrains[0]) > 0 and len(self.terrains[1]) > 0:
            if self.LOGS == True:
                print(f"Joueur 1 {self.players[0]} |||| Joueur 2 {self.players[1]}")
                print(f"Terrain du Joueur 1 : {self.terrains[0]} |||| Terrain du Joueur 2 : {self.terrains[1]}")
            temp = [terrain.get_card() for terrain in self.terrains]
            win_card = Carte.get_winner(temp)
            
            if win_card is False: #Si il y a egalité entre deux carte
                x = "Stop"
            else:
                x = next(i for i, card in enumerate(temp) if card == win_card)
            if x == "Stop": #Ce code pose une carte en plus pour simuler la carte a l'envers. 
                if (len(self.players[0]) > 0 and len(self.players[1]) > 0):
                    for i in range(len(self.players)):self.terrains[i].ajouter(self.players[i].enlever())
            else:
                for terrain in self.terrains if random.choice([-1, 1]) == 1 else reversed(self.terrains): #Comme dans une vraie partie les cartes ne sont pas recuperer de manière logique et definitive par consequent une partie d'aleatoire est present pour choisir quel carte du terrains et prise en premiers
                    while len(terrain) > 0:
                        self.players[x].ajouter(terrain.enlever())
            
            x=None #Permets de definir si un joueur gagne
            if len(self.players[1].container) == 0: #
                x= True #
            if len(self.players[0].container) == 0: #
                x= False #
            self.players = [p for p in self.players if len(p) > 0]
            if self.STOP == True:
                while str(input("Press Enter to continue...")) == None:
                    pass
            return x
        return None
    
            
    

#============================================================================================================= 
#Programme Principal / Programme de Test
#=============================================================================================================
if __name__ == "__main__":
    partie = Main()
    partie.start(None, True, True)