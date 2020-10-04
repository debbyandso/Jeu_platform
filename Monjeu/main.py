import pygame
pygame.init()


# 1/ GENERER LES FENETRES 
pygame.display.set_caption('Les aventures de Nono')
screen = pygame.display.set_mode((1080,1000))
# 2/ Importation d'un background pour le jeu
background= pygame.image.load('assetsjeuplatform/Background.png')
running = True

# 3/ boucles pour la fenetre reste ouverte running

while running:
    #Arriere plan
    #(0.0), c'est pour que le background soit centré et ensuite, ca fait des zooms selo les valeurs
    screen.blit(background, (0,0))

    #mettre a jour ecran
    pygame.display.flip()

    #si joueur ferme fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()