import pygame, sys
from pygame.locals import *

pygame.init()
#objeto ventana de tipo superficie = lienzo
ventana = pygame.display.set_mode((600,400))
pygame.display.set_caption("Hola mundo")

#objeto para cargar imagen
imagen1 = pygame.image.load("imagenes/snoopy.png")
#posición para la imagen
posX,posY= 130,70
#alternativa
#posX=130
#posY=70

#dibujar en ventana
ventana.blit(imagen1,(posX,posY))

# existen dos formas para crear colores RGB 0 a 255
Color=(100,130,60)
Color2=(50,50,50)
Color3=(200,90,180)
Color4=(56,45,20)
ColorFondo= pygame.Color(0,0,255)

posX,posY= 130,70
speed=0.5 #numero de pixeles que se va a mover cada vez
derecha= True


while True:
    #rellenar lienzo
    #ventana.fill(Color)
    ventana.fill(ColorFondo)
    pygame.draw.circle(ventana, Color, (80, 150), 20)
    pygame.draw.line(ventana, Color2, (60, 80), (160, 80), 8)
    pygame.draw.rect(ventana, Color3, (0, 0, 100, 50))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    #pygame.display.flip()

    pygame.display.update()
