import pygame, sys
from pygame.locals import *

pygame.init ()

ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("con fondo")

fondo=pygame.image.load("imagenes/nubes2.jpg")
posXf,posYf=0,0

while True:
    ventana.blit(fondo,[0,0])

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
