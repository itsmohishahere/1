import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((360,540), pygame.RESIZABLE)

color=(54, 158, 227)


running= True

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the game
    screen.fill(color)
    pygame.display.flip()


pygame.quit()
