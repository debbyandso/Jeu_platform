import pygame
pygame.init()

#classe representant le joueur

class Player (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        #vitesse deplacement du joeur
        self.velocity= 5
        self.image = pygame.image.load('assetsjeuplatform/Character.png')
        self.rect= self.image.get_rect()


# 1/ GENERER LES FENETRES 
pygame.display.set_caption('Les aventures de Nono')
screen = pygame.display.set_mode((1920,1080))
# 2/ Importation d'un background pour le jeu
background= pygame.image.load('assetsjeuplatform/Background.png')
#charger player ( variable player =  nouvelle instance player)
player = Player()
running = True

# 3/ boucles pour la fenetre reste ouverte running

while running:
    #Arriere plan
    #(0.0), c'est pour que le background soit centré et ensuite, ca fait des zooms selo les valeurs
    screen.blit(background, (0,0))

    #appliquer image du joueur ( player = classe)

    screen.blit(player.image, player.rect)

    #mettre a jour ecran
    pygame.display.flip()

    #si joueur ferme fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

#video 8m55
