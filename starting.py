
import pygame
pygame.init()
from pygame.locals import * 

# partie retirable plus tard
pygame.display.set_caption ("Pokémon DD")
screen = pygame.display.set_mode((1200, 950))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print ("Fermeture du Jeu")

