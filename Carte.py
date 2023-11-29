class Carte:
    def __init__(self, chiffre = None, type = None):
        if chiffre != None and type != None:
            self.couleur = couleur[type]
            if chiffre == 0:
                self.puissance = 13
            else:
                self.puissance = chiffre
            self.name = carte[self.puissance]
    def __str__(self):
        return f"{self.name}{self.couleur}"
    def getWinner(card):
        cardvar = card[0]
        for i in range(1, len(card)):
            if cardvar.puissance and card[i].puissance == 13:
                return None
            if cardvar.puissance == card[i].puissance:
                return False
            elif cardvar.puissance < card[i].puissance:
                cardvar = card[i]
        return cardvar
    




couleur = ["Trefle", "Pique", "Carreau", "Coeur"]
carte = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "A"]

if __name__ == '__main__':
    list = [Carte(10, 2), Carte(0, 3), Carte(3, 2)]
    print(Carte().getWinner(list))