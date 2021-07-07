# -*- encoding: utf-8 -*-

import pygame
import config as cfg
import graphics as gfx

class Pallet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gfx.LoadImage(cfg.sprites + "pala.png", True)
        self.rect = self.image.get_rect()
        self.rect.top = 420
        self.rect.centerx = (cfg.width-140)/2
        self.speed = 0.5

    def Update(self, drctr, time):
        if drctr == 1:
            if self.rect.left >= 15:
                self.rect.x -= self.speed*time

        elif drctr == 2:
            if self.rect.right <= 485:
                self.rect.x += self.speed*time

    def draw(self, screen):
        screen.blit(self.image, self.rect)


