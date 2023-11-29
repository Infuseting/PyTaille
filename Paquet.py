
from Carte import *
import random
class Paquet:
    def __init__(self, type):
        self.container = []
        if type == "PIOCHE":
            for i in range(4):
                for p in range(13):
                    self.container.append(Carte(p, i))
        elif type == "JEU":
            print("Creation d'un jeu de carte pour un joueur ! ")
        elif type == "Terrain":
            print("Creation d'un paquet de terrain")

    def ajouter(self, card):
        self.container.append(card)
    def enlever(self):
        assert len(self.container) > 0
        s = self.container[0]
        self.container.pop(0)
        return s
    def __str__(self):
        temp = f"["
        for i in self.container:
            
            if i.couleur == "Trefle":
                temp +=f"{i.name}♣"
            elif i.couleur == "Pique":
                temp +=f"{i.name}♠"
            elif i.couleur == "Carreau":
                temp +=f"{i.name}♦"
            elif i.couleur == "Coeur":
                temp +=f"{i.name}♥"
            temp+=f","
        temp += f"]"
        return f"{temp}"
    def __len__(self):
        return len(self.container)
    def melanger(self):
        temp = self.container
        random.shuffle(temp)
        self.container = temp
    
    def distribution(self, num):
        ListPaquet, x = [], 0
        for i in range(num): ListPaquet.append(Paquet("JEU"))
        for i in range(len(self.container)):
            ListPaquet[x].ajouter(self.enlever())
            if x >= num-1:
                x= 0
            else:
                x+=1
        return ListPaquet
if __name__ == '__main__':
    paquet = Paquet("PIOCHE")
    print(paquet)
    paquet.melanger()
    print(paquet)
    paquet.distribution(2)