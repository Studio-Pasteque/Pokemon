import pygame
from utilities import Window, Color
from objects import *

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
pygame.display.set_caption("Pokemon")
clock = pygame.time.Clock()

player = Player(Window.WIDTH / 2, Window.HEIGHT / 2, "assets/Player.png")
obstacle = Object(200, 200, "assets/Player.png")

running = True
while running:
    clock.tick(Window.FPS)
    
    # draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update
    player.update()
    obstacle.update()
    player.collide_with(obstacle.bounds)
    
    screen.fill(Color.BLACK)
    screen.blit(obstacle.image, obstacle.bounds)
    screen.blit(player.image, player.bounds)
    
    pygame.display.update()

pygame.quit()