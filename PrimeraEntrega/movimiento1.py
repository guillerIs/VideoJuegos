import pygame, sys
from pygame.locals import *


pygame.init()

ventana = pygame.display.set_mode((800,400))
pygame.display.set_caption("Sin embargo se mueve")
ColorFondo= pygame.Color(0,0,255)
imagen1 = pygame.image.load("imagenes/snoopy.png")
posX,posY= 130,70

################
#desplazamiento
################
speed=0.5 #numero de pixeles que se va a mover cada vez
derecha= True


while True:
    ventana.fill(ColorFondo)
    ventana.blit(imagen1, (posX, posY))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if derecha==True:
        if posX<800:
            posX+=speed
        else:
            derecha=False
    else:
        if posX>1:
            posX-=speed
        else:
            derecha=True
    pygame.display.update() #actualiza (refresca) pantalla