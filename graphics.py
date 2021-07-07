# -*- coding: utf-8 -*-

"""Módulo para implementar el manejo de gráficos y superficies"""

#Módulos
import pygame

# Carga una imagen de transparencia y colo transparente opcionales.
def LoadImage(filename, transparent = False, pixel = (0,0)):
    "Carga una imagen al formato interno de pygame"
    
    try: image = pygame.image.load(filename)
    except pygame.error as message:
        raise SystemExit(message)
    
    image = image.convert()

    if transparent:
        color = image.get_at(pixel)
        image.set_colorkey(color, pygame.RLEACCEL)#Que es RLACCEL

    return image

def Text(text, position = (0,0), color = (0,0,0), size = 25):
    "Crea una imagen con texto pasado y su rect"

    font = pygame.font.Font("../images/DroidSans.ttf", size)
    output = pygame.font.Font.render(font, text, 1, color)
    outRect = output.get_rect()
    outRect.center = posiiton

    return output, outRect
    
