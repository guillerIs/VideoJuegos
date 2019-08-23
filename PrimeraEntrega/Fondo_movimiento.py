import pygame, sys
from pygame.locals import*

pygame.init()

ventana=pygame.display.set_mode((800,600))
pygame.display.set_caption("Fondo&Movimiento")

fondo=pygame.image.load("imagenes/nubes2.jpg")
snoopy=pygame.image.load("imagenes/snoopy.png")
posXs,posYs=130,70

######desplazamiento#####
speed=5
derecha=True

while True:
    ventana.blit(fondo,[0,0])
    ventana.blit(snoopy,(posXs,posYs))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        #evento presionar tecla
        elif event.type==pygame.KEYDOWN:
            if event.key==K_LEFT:
                posXs-=speed
            elif event.key==K_RIGHT:
                posXs+=speed


    pygame.display.update()