import pygame, sys
from pygame.locals import *

pygame.init()

ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("moviendo con tecla")

ColorFondo=pygame.Color(0,0,255)

snoopy=pygame.image.load("imagenes/snoopy.png")
posX,posY= 130,70
speed=7
derecha=True

while True:
    ventana.fill(ColorFondo)
    ventana.blit(snoopy,(posX,posY))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN: #si el evento fue una tecla presionada
            if event.key==K_LEFT: #preguntar que tecla fue
                posX-=speed #mover imagen a la izquierda
            elif event.key==K_RIGHT:
                posX+=speed

    pygame.display.update()
