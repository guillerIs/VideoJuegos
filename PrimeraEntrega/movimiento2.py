import pygame, sys
from pygame.locals import *

pygame.init()

ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("Sin embargo se mueve")
ColorFondo=pygame.Color (0,0,255)
imagen1=pygame.image.load("imagenes/woodstock.png")
posX,posY= 400,0

speed=0.25
arriba=True

while True:
    ventana.fill(ColorFondo)
    ventana.blit(imagen1,(posX,posY))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    if arriba== True:
        if posY<600:
            posY+=speed
        else:
            arriba=False
    else:
        if posY>1:
            posY-=speed
        else:
            arriba= True
    pygame.display.update()



