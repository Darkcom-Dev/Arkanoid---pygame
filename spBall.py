# -*- encoding: utf-8: -*-

import pygame
import config as cfg
import graphics as gfx
import math

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = gfx.LoadImage(cfg.sprites + "ball.png", True)
        self.rect = self.image.get_rect()
        self.rect.centery = cfg.height / 2
        self.rect.centerx = (cfg.width - 140)/2
        self.speed = [0.4, 0.4]

    def Update(self, time, pallet):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        

        # Colisiones con las paredes
        if self.rect.left <= 10:
            self.rect.left = 10
            self.speed[0] = -self.speed[0]
        if self.rect.right >= 490:
            self.rect.right = 490
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 10:
            self.rect.top = 10
            self.speed[1] = -self.speed[1]
        if self.rect.bottom >= 470:
            self.rect.bottom = 470
            self.speed[1] = -self.speed[1]

        # Colisiones de la pala
        if pygame.sprite.collide_rect(self, pallet):
            if self.rect.centerx <= pallet.rect.centerx:
                dist = pallet.rect.centerx - self.rect.centerx #Entender que hace esto
                self.speed[0] = -math.sin(math.radians(dist)) / 1.25
                
            elif self.rect.centerx > pallet.rect.centerx:
                dist = self.rect.centerx - pallet.rect.centerx
                self.speed[0] = math.sin(math.radians(dist)) / 1.25
            self.speed[1] = -self.speed[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
