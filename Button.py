#=============================================================================================================
#Nom de l'auteur : lucien
#=============================================================================================================


#=============================================================================================================
#Import
#=============================================================================================================

import sys
import pygame
from Carte import *
#=============================================================================================================
    #Nom de l'auteur : Lucien (Responsable des sous class (Button, ext))
#=============================================================================================================
        
class Button():
    """La class bouton est une sous-class requise pour Pygame et la gestion de Bouton avancé (Très avancé)
        Methode:
            process() [] : Permets de process et de faire l'ensemble des modifications du bouton.
        Attribut:
            X (class Int) : Position X du bouton (Point en haut a gauche)
            Y (class Int) : Position Y du bouton (Point en haut a Gauche)
            WIDTH (class Int) : Longueur du bouton
            HEIGHT (class Int) : Largeur du bouton
            ONCLICKFUNCTION (Fonction) : Contient une autre fonction
            ONEPRESS (class Boolean) : Si True tant que le joueurs clique sur le bouton la fonction s'execute. Si False le joueurs devra unpressed le bouton pour recliquer.
            FILLCOLORS (class Dictionnaire) : Contient l'ensemble des couleurs en fonction de differentes conditions.
            BUTTONSURFACE (class pygame.Surface) : Variables qui contient la surface du Bouton
            BUTTONRECT (class pygame.Rect) : Variables qui contient le rectangle du background
            FENETRE (class pygame.Fenetre) : Variables qui contient la fenetre
            FONT (class pygame.FONT) : Variables qui contient la FONT
            BUTTONSURF (class pygame.Render) : Variables qui contient le text
            HOVER (class String) : Variable qui contient le texte du hoverText
            HOVERTEXT (class List) : List qui contient au même titre que le objects l'ensemble des position graphique et objet du HoverText de ce bouton
            ALREADYPRESSED (class Boolean) : Boolean qui definis si le boutton a êtait pressée recamment.
            APP (class APP) : Contient la Class APP (Responsable de la gestion graphique)
            objects (class List) : Contient l'ensemble des boutons APP
    """
    def __init__(self, objects, x, y, width, height, font, fenetre, app, buttonText='Button', onclickFunction=None, onePress=False, color={'normal': '#ffffff','hover': '#666666','pressed': '#333333', 'transparence': None}, hoverText= None):
        
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.ONCLICKFUNCTION = onclickFunction
        self.ONEPRESS = onePress

        self.FILLCOLORS = color

        self.BUTTONSURFACE = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.BUTTONRECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.FENETRE =fenetre
        self.FONT = font
        self.BUTTONSURF = self.FONT.render(buttonText, True, (20, 20, 20))
        if hoverText != None:
            self.HOVER = hoverText 
            self.HOVERTEXT = [];    
            
        else:
            self.HOVER = None
            self.HOVERTEXT = None
        self.ALREADYPRESSED = False
        self.APP = app
        objects.append(self)

    def process(self):
        if self.HOVERTEXT != None: #A chaque execution il clear tous les anciens hovertext desinés sur la partie graphique
            self.HOVERTEXT.clear()
        mousePos = pygame.mouse.get_pos()
        if self.FILLCOLORS['transparence'] != None: 
            self.BUTTONSURFACE.set_alpha(self.FILLCOLORS['transparence']) 
        if self.FILLCOLORS['normal'] != None:
            self.BUTTONSURFACE.fill(self.FILLCOLORS['normal'])
        if self.BUTTONRECT.collidepoint(mousePos):
            if self.HOVER != None: #Si il y a un hover d'activé le code sera executé et dessinée
                if len(self.APP.partie.terrains[0].container ) > 0 and len(self.APP.partie.terrains[1].container ) > 0:
                    temp = [terrain.get_card() for terrain in self.APP.partie.terrains]
                    win_card = Carte.get_winner(temp)
                    if win_card == False:
                        text = self.HOVER.get_container_str(True)
                    else:
                        text = self.HOVER.get_container_str(False)
                    HOVERTEXT = Button(self.HOVERTEXT, mousePos[0], mousePos[1], 250, 40, self.FONT, self.FENETRE, self.APP,text, self.ONCLICKFUNCTION, self.ONEPRESS, {'normal': '#FFFF00','hover': '#FFFF00','pressed': '#FFFF00', 'transparence': 100}, None)
                    self.HOVERTEXT.append(HOVERTEXT)
                    self.APP.statusUpdate = True
                    for object in self.HOVERTEXT:
                        object.process()
            if self.FILLCOLORS['hover'] != None:
                self.BUTTONSURFACE.fill(self.FILLCOLORS['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if self.FILLCOLORS['hover'] != None:
                    self.BUTTONSURFACE.fill(self.FILLCOLORS['pressed'])

                if self.ONEPRESS == True: 
                    if self.ONCLICKFUNCTION != None:
                        self.ONCLICKFUNCTION() #Execute la fonction renseignée

                elif not self.ALREADYPRESSED:
                    if self.ONCLICKFUNCTION != None:
                        self.ONCLICKFUNCTION() #Execute la fonction renseignée
                    self.ALREADYPRESSED = True

            else:
                self.ALREADYPRESSED = False

        self.BUTTONSURFACE.blit(self.BUTTONSURF, [
            self.BUTTONRECT.width/2 - self.BUTTONSURF.get_rect().width/2,
            self.BUTTONRECT.height/2 - self.BUTTONSURF.get_rect().height/2
        ]) #Draw le text 
        self.FENETRE.blit(self.BUTTONSURFACE, self.BUTTONRECT) #Draw le background