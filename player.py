from main import *
from Paquet import *
from Carte import *

class Player:
    def __init__(self, Paquet, utilisateur = None):
        self.container = Paquet
        self.utilisateur = utilisateur
    def __len__(self):
        return len(self.container)
    def ajouter(self, card):
        self.container.append(card)
    def enlever(self):
        s = self.container[0]
        self.container.pop(0)
        return s