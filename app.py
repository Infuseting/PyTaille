#=============================================================================================================
#Nom de l'auteur : Lucien et Theo et Arthur
#=============================================================================================================


#=============================================================================================================
#Import
#=============================================================================================================

import pygame
from pygame.locals import *
from Button import *
from main import *
import pygame_textinput
from player import *
import time
#=============================================================================================================
#Definition d'une Class
#=============================================================================================================
class App:
    """)
        Class permettant la compatibilité entre l'affichage graphique et le systeme theorique de la Bataille (Class Main)

        attribut:
            -> Partie (class Partie) : Variable qui permet la sauvegarde et l'interaction simple a la partie.
            -> XSIZE ; YSIZE (Class int) : Variable qui permet de facilement modifier la taille de la fenetre.
            -> continuer (class Boolean): Variable qui permet de lancer la loop FPS (Fonctionnalité de Pygame)
            -> FPS (Class int) : Variable qui permet de definir le nombre de FPS de la fenetre 
            -> player (Class Player) :  Variable qui contient l'ID de l'utilisateur (Nom d'utilisateur). Si le Joueur ne s'est pas connecté la variable reste dans sa forme initial.
            -> objects (Class list) : Variable qui contient l'ensemble des boutons permettant de facilement acceder au parametres de celui-ci (Les elements de la liste sont de la class Button)
            -> status (class String) : Variable nommée en fonction de ce qui doit être affichée et permets d'executer les updates a chaque frame.
            -> statusUpdate (class Boolean): Variable qui permets en cas de True. De refresh la fenetre.
        methode :
            -> __init__() []: Constructeur, Contient les informations obligatoires au lancement du jeu.
            -> start() []: fonction qui permet de lancer la partie et d'effectuer son affichage sur la fenetre.
            -> menu() []: fonction qui permet d'afficher le menu lobby.
            -> stats() []: fonction qui permet d'afficher les stats. /!\ Fonctionnalité non disponible
            -> leave() []: fonction qui permet de fermer la fenetre.
            -> addcard() [] : Fonction qui sert a convertir l'ensemble des requetes graphique vers des requetes theoriques dans le cas d'ajout de carte et de verification sur le gagnant de la manche (Fonctionnalité basique d'une partie).
            -> compte() [username : String] : Fonction qui permets de changer de compte / se connecter a son compte.
            -> render() []: Fonction qui permet de lancer la gestion graphique. Sans les gerer.
            -> executor() [objects : List, FONT : pygame.font, FENETRE : pygame.window, TEXTINPUT: pygame_textinput.textinput]: Doit être lancé uniquement pas render() celui-ci permets de gerer completement les affichages directes les interactions utillisateurs / machine et les updates graphique des fenetres
    """
    def __init__(self):
        self.partie = None
        self.XSIZE, self.YSIZE = 800,800
        self.continuer = True
        self.FPS = 60
        self.player = Player()
        
    #=============================================================================================================
    #Nom de l'auteur : Lucien (Responsable des sous class (Button, ext)) /!\ IL EST AUSSI RESPONSABLE DE LA CLASS BUTTON MIS A PART
    #=============================================================================================================
    def start(self):
        self.objects.clear() #Permets de clear l'ensemble des boutons.
        self.partie = Main()
        self.partie.start("app")
        self.status = "game"
        self.statusUpdate=True
    def menu(self):
        self.status= "Lobby"
        self.objects.clear()
        self.statusUpdate = True
    def login(self):
        self.status = "Login"
        self.objects.clear()
        self.statusUpdate = True        
    def stats(self):
        self.status= "Stats"
        self.objects.clear()
        self.statusUpdate = True        
    def leave(self):
        self.continuer = False
    def addcard(self):
        if self.status == "game":
            if self.partie.lock == False:
                self.partie.lock = True
                value = self.partie.verify()
                if value != None:
                    self.objects.clear()
                    self.status= "End"
                    self.win = value
                    self.statusUpdate = True
                    self.partie.lock = False
                else:
                    self.partie.play()
                self.partie.lock = False       
    def compte(self, username):
        self.Player = Player(username)
    #=============================================================================================================
    #Nom de l'auteur : Theo (Responsable du fonctionnement de l'ensemble du Render) Arthur (Responsable de la capacité a être compatible avec le code + Organisation et Optimisation)
    #=============================================================================================================
    
    def render(self):
        pygame.init()
        self.objects = []
        self.menu()
        
        FENETRE = pygame.display.set_mode((self.XSIZE, self.YSIZE))
        pygame.display.set_caption('Bataille')
        FONT = pygame.font.SysFont('Arial', 30)
    
        FONT2 = pygame.font.SysFont("Consolas", 55)
        MANAGER = pygame_textinput.TextInputManager(validator = lambda input: len(input) <= 16) #Fonctionnalité provenant de la lib pygame_textinput permettant de faire un input de manière graphique les parametres limite le nombre de caractere a 16

        TEXTINPUT_CUSTOM = pygame_textinput.TextInputVisualizer(manager=MANAGER, font_object=FONT2) #Permets de preparer le text a être draw
        #custom
        TEXTINPUT_CUSTOM.cursor_width = 4 # La taille du curseur
        TEXTINPUT_CUSTOM.cursor_blink_interval = 400 # l'interval du blink
        TEXTINPUT_CUSTOM.antialias = False  
        TEXTINPUT_CUSTOM.font_color = (0, 85, 170) #Couleur de la font
        #derniere ligne 
        self.executor(self.objects, FONT, FENETRE, TEXTINPUT_CUSTOM)
    def executor(self, objects, FONT, FENETRE, TEXTINPUT):
        FPSClock = pygame.time.Clock() #Defini le fps cap
        while self.continuer:
            events = pygame.event.get()
            if self.status == "Login":
                fond = pygame.image.load("textures/background.png").convert() ; FENETRE.blit(fond, (0,0))
                text = pygame.font.SysFont('Arial', 50) ; text_surface = text.render(f"Nom d'utilisateur"    , False, (139, 0, 0)) ; FENETRE.blit(text_surface, (250, 300))    
                TEXTINPUT.update(events) #A chaque fps le Text input est update
                FENETRE.blit(TEXTINPUT.surface, (250, 350))
            if self.status == "End":
                if self.statusUpdate == True:
                    
                    fond = pygame.image.load("textures/background.png").convert() ; FENETRE.blit(fond, (0,0))
                    text = pygame.font.SysFont('Arial', 100) ; text_surface = text.render(f"{'Victoire' if self.win == True else 'Defaite'}"    , False, (139, 0, 0)) ; FENETRE.blit(text_surface, (40, 40))
                    start = Button(objects, 250, 350, 300, 50, FONT, FENETRE,self,  'Lancer une partie', lambda: self.start(), False, color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
                    menu = Button(objects, 250, 425, 300, 50, FONT, FENETRE,self,  'Retourner au Menu', lambda: self.menu(), False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
                    leave = Button(objects, 250, 500, 300, 50, FONT, FENETRE,self,  'Retourner au Bureau', lambda: self.leave(), False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
            if self.status == "Lobby":
                if self.statusUpdate == True:
                    fond = pygame.image.load("textures/background.png").convert() ; FENETRE.blit(fond, (0,0))
                    text = pygame.font.SysFont('Arial', 160) ; text_surface = text.render('BATAILLE', False, (139, 0, 0)) ; FENETRE.blit(text_surface, (40, 40))
                    login = Button(objects, 20, 720, 200, 40, FONT, FENETRE, self, f"Se connecter" if self.player.utilisateur == "Utilisateurs Inconnu" else self.player.utilisateur, lambda: self.login(), False, color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 50})
                    start = Button(objects, 250, 350, 300, 50, FONT, FENETRE,self,  'Lancer une partie', lambda: self.start(), False, color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
                    stats = Button(objects, 250, 425, 300, 50, FONT, FENETRE,self,  'Statistiques', lambda: None, False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
                    leave = Button(objects, 250, 500, 300, 50, FONT, FENETRE,self,  'Retourner au Bureau', lambda: self.leave(), False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 1})
                    
            if self.status == "game":
            
                if self.statusUpdate == True:
                    fond = pygame.image.load("textures/background.png").convert() ; FENETRE.blit(fond, (0,0))
                    
                    addcard = Button(objects, 284, 646, 50, 50, FONT, FENETRE,self,  '+', lambda: self.addcard(), False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 100})
                    fond = pygame.image.load("textures/bot.png").convert() ; FENETRE.blit(fond, (716, 80))
                    botusername = Button(objects, 530, 35, 250, 40, FONT, FENETRE,self, str(f"C-3-P-0"),None, False,{'normal': '#ffffff','hover': '#ffffff','pressed': '#ffffff', 'transparence': 100})
                    fond = pygame.image.load("textures/user.png").convert() ; FENETRE.blit(fond, (20, 676))
                    botusername = Button(objects, 20, 745, 250, 40, FONT, FENETRE,self, str(f"{self.player.utilisateur}"), None, False,{'normal': '#ffffff','hover': '#ffffff','pressed': '#ffffff', 'transparence': 100})
                viewcardUser = Button(objects, 284, 506, 50, 50, FONT, FENETRE,self,  '=', None, False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 100}, hoverText=self.partie.terrains[0])
                viewcardBot = Button(objects, 284, 243, 50, 50, FONT, FENETRE,self,  '=', None,  False,  color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': 100}, hoverText=self.partie.terrains[1])
                tour = Button(objects, 20, 20, 150, 40, FONT, FENETRE,self, str(self.partie.tour),None, False,{'normal': '#ffffff','hover': '#ffffff','pressed': '#ffffff', 'transparence': 100})        
                if len(self.partie.players[1]) >= 1: img = pygame.image.load("textures/behind.png").convert() ; FENETRE.blit(img, (353, 61))
                if len(self.partie.players[0]) >= 1: img = pygame.image.load("textures/behind.png").convert() ; FENETRE.blit(img, (353, 604))
                text = pygame.font.SysFont('Arial', 40) ; text_surface = text.render(str(len(self.partie.players[1].container)), False, (0, 0, 0)) ; FENETRE.blit(text_surface, (371, 101))
                text = pygame.font.SysFont('Arial', 40) ; text_surface = text.render(str(len(self.partie.players[0].container)), False, (0, 0, 0)) ; FENETRE.blit(text_surface, (371, 644))
                if len(self.partie.terrains[1].container) ==  1:
                    img = pygame.image.load("textures/" + str(self.partie.terrains[1].container[0]) + ".png").convert();FENETRE.blit(img, (353, 201))
                elif len(self.partie.terrains[1].container) > 1:
                    img = pygame.image.load("textures/" + str(self.partie.terrains[1].container[-1]) + ".png").convert();FENETRE.blit(img, (353, 201))
                if len(self.partie.terrains[0].container) == 1: 
                    img = pygame.image.load("textures/" + str(self.partie.terrains[0].container[0]) + ".png").convert();FENETRE.blit(img, (353, 464))
                elif len(self.partie.terrains[1].container) > 1:
                    img = pygame.image.load("textures/" + str(self.partie.terrains[0].container[-1]) + ".png").convert();FENETRE.blit(img, (353, 464))
            
            self.statusUpdate=False
            for event in events:
                 
                
                if event.type == pygame.QUIT:
                    self.continuer = False
                    exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.player = Player(TEXTINPUT.value)
                    self.menu()
                if self.status == "game":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.addcard()
                        if event.key == pygame.K_ESCAPE:
                            self.continuer = False
            for object in objects:
                object.process() #Object corresponds a un elements de la liste objet de type Button

            pygame.display.flip()
            FPSClock.tick(self.FPS)
            continue
#============================================================================================================= 
#Programme Principal / Programme de Test
#=============================================================================================================
if __name__ == "__main__":
    app = App()
    app.render()
    
    
    