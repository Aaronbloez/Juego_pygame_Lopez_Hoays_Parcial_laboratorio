import pygame
from sprites import *


class Flecha(pygame.sprite.Sprite):
    def __init__(self, path_image:str,size: tuple,center:tuple,Volumen,speed:int = 10):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(),size)
        #self.animaciones = animations_flechas()
        self.rect =self.image.get_rect()
        self.volumen = Volumen
        self.sonidos = sonido_flechas()
        self.rect.center = center
        self.speed_origin = speed
        self.speed = speed
        self.pego = False

    def update(self):
        self.rect.x += self.speed

        if self.pego:
            
            self.kill()

    def stop(self):
        self.speed = 0

    def activate(self):
        self.speed = self.speed_origin
  

      
