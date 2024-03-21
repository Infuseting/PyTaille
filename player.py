from main import *
from Paquet import *
from Carte import *

class Player:
    """
        Class qui contient l'ensemble des parametres liée a un compte de joueurs

        Variables : 
            utilisateur (class String) : Contient le nom de l'utilisateur

        Methode :
            __init__() [Utilisateur = "Utilisateurs Inconnu" : String] : Permets de definir le nom d'utilisateur du Joueur
    """
    def __init__(self, utilisateur = "Utilisateurs Inconnu"):
        self.utilisateur = utilisateur
        