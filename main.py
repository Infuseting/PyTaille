from random import *
from Carte import *
from Paquet import *
class Main:
    def __init__(self):
        self.player = 2

    def start(self):
        pioche = Paquet("PIOCHE")
        pioche.melanger()
        players = pioche.distribution(self.getPlayer())
        terrains = [Paquet("Terrain") for _ in range(self.getPlayer())]

        tour = 0
        while len(players) > 1:
            tour += 1
            for i, player in enumerate(players):
                terrains[i].ajouter(player.enlever())

            temp = [terrain.getCard() for terrain in terrains]
            win_card = Carte.getWinner(temp)

            if win_card is False:
                x = "Stop"
            else:
                x = next(i for i, card in enumerate(temp) if card == win_card)

            print(f"Terrain 1: {str(terrains[0])}\nTerrain 2: {str(terrains[1])}")
            print(f"Joueurs 1: {str(players[0])}\nJoueurs 2: {str(players[1])}")
            if x == "Stop":
                for i in range(len(players)):terrains[i].ajouter(players[i].enlever())
            else:
                #for card in terrains[x]:
                #    players[x].ajouter(card)
                for terrain in terrains:
                    while len(terrain) > 0: players[x].ajouter(terrain.enlever())

            players = [p for p in players if len(p) > 0]
            if tour % 50 == 0: #Petite ligne de code qui melange de temps a autre le jeu de chaque joueurs pour eviter les problemes de repetition infini
                for i in range(len(players)): random.shuffle(players[i].container)
            #while str(input("Press Enter to continue...")) == None:
            #    pass

        print(tour)

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