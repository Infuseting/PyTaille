from random import *
from Carte import *
from Paquet import *
class Main:
    def __init__(self):
        self.player = 2
    
    def cardplace(self, Terrain, Player):
        for i in range(len(Player)):                
            Terrain[i].ajouter(Player[i].enlever())
            #print(f"Terrain du joueurs {i+1} : {Terrain[i]} ")
        return Terrain, Player
    def getWinnerCard(self, Terrain, Player):
        Temp = []
        for i in range(len(Terrain)):
            s = Terrain[i].enlever()
            Terrain[i].ajouter(s)
            Temp.append(s)
        WinCard = Carte.getWinner(Temp)
        return WinCard, Terrain, Player
    def RemoveCardOnTerrain(self, Terrain, Player, WinCard):
        for i in range(len(Terrain)):
            s = Terrain[i].enlever()
            Terrain[i].ajouter(s)
            if WinCard == None:
                x = "Stop"
            if WinCard == False:
                x = "Stop"
            if WinCard == s:
                x = i
        for i in range(len(Terrain)):
            if x == "Stop":
                s = Terrain[i].enlever()
            else:
                s = Terrain[i].enlever()
                Player[x].ajouter(s)
        return Terrain, Player

    def VerifyLoosePlayer(self, Player):
        
        for i in range(len(Player)):
            if len(Player[i]) == 0:
                Player.pop(i)
        return Player  
    def start(self):
        #while self.setPlayer(int(input("Definir le nombre de joueurs (2-3)"))) == False: #identifier le nombre de joueurs
        #    pass
        pioche = Paquet("PIOCHE") #ON Y CREE ICI LE JEU DE CARTE
        pioche.melanger() #MELANGE
        Player = pioche.distribution(self.getPlayer()) #DISTRIBUTION DES CARTES POUR CHAQUE JOUEURS
        Terrain = []
        for i in range(self.getPlayer()):
            Terrain.append(Paquet("Terrain")) #Creation des zones dans lequel chaque joueurs posera sa carte
        Tour = 0
        while len(Player) > 1: #Code qui s'executera tant que le nombre de joueurs est superieur a 1
            Tour +=1 #Variable dites "Inutile" qui permets juste de compter le nombre de tour pour realiser une bataille complete et permets de melanger de temps a autre le jeu des joueurs
            Terrain, Player = self.cardplace(Terrain, Player) #Fonction qui fait en sorte que chaque joueurs pose une carte sur le terrain
            WinCard, Terrain, Player = self.getWinnerCard(Terrain, Player) #Parmis toute les cartes en tête de file. La fonction y releve la carte la  plus forte
            Terrain, Player= self.RemoveCardOnTerrain(Terrain, Player, WinCard) #Fait une verification sur le type et le moyen donc a êtait gagné la partie (False = Impossible, None = Bataille, Autre = Une carte a gagné. On y va donc y rechercher a quel joueurs appartient la carte)
            Player = self.VerifyLoosePlayer(Player) #Regarde si il n'y a pas des joueurs qui ont perdu. Si oui, ils les eliminent ainsi que leur terrain
            if Tour % 50 == 0: #Petite ligne de code qui melange de temps a autre le jeu de chaque joueurs pour eviter les problemes de repetition infini
                for i in range(len(Player)): random.shuffle(Player[i].container)
                #while str(input("Pour continuer")) == None: pass 
        print(Tour)

    def setPlayer(self, num):
        if num >= 2 and num <= 3:
            self.player = num
            return True
        else:
            return False
    def getPlayer(self):
        return self.player
    

if __name__ == "__main__":
    partie = Main()
    partie.start()