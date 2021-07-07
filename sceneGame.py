# -*- encoding: utf-8 -*-
import scene as scn
import config as cfg
import graphics as gfx
import spPallet, spBall
import pygame

class SceneGame(scn.Scene):
    "Escena inicial del juego, esta es la primera que se carga cuando inicia"

    def __init__(self, director):
        scn.Scene.__init__(self, director)
        self.back = gfx.LoadImage(cfg.backgrounds + "back_game.png")
        # Constructor
        self.pallet = spPallet.Pallet()
        self.ball = spBall.Ball()

    def on_update(self):
        self.time = self.director.time
        self.ball.Update(self.time, self.pallet)

    def on_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pallet.Update(1, self.time)
        if keys[pygame.K_RIGHT]:
            self.pallet.Update(2, self.time)
    
    def on_draw(self, screen):
        screen.blit(self.back, (0,0))
        self.pallet.draw(screen)
        self.ball.draw(screen)
