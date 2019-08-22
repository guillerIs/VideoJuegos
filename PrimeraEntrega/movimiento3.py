import pygame, sys
from pygame.locals import*

pygame.init()

ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("Snoopy & woodstock")
ColorFondo=pygame.Color(0,0,255)

snoopy=pygame.image.load("imagenes/snoopy.png")
woodstock=pygame.image.load("imagenes/woodstock.png")
posXs,posYs= 130,70
posXw,posYw= 600,0
speedS= 0.5
speedW=0.35
derecha= True
arriba= True

while True:
    ventana.fill(ColorFondo)
    ventana.blit(snoopy,(posXs,posYs))
    ventana.blit(woodstock,(posXw,posYw))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    if derecha==True:
        if posXs<800:
            posXs+=speedS
        else:
            derecha=False

    else:
        if posXs>1:
            posXs-=speedS
        else:
            derecha=True

    if arriba==True:
        if posYw<600:
            posYw+=speedW
        else:
            arriba=False
    else:
        if posYw>1:
            posYw-=speedW
        else:
            arriba=True


    pygame.display.update()
