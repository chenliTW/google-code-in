import sys

import pygame
from pygame.locals import QUIT

pygame.init()
window_surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('two-circles')
window_surface.fill((255, 255, 255))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()