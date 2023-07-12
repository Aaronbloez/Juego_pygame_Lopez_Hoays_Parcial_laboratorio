import pygame
from funciones import *
from pygame.sprite import *

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, path_image:str,size: tuple,top_left:tuple):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path_image).convert_alpha(),size)
        self.rect  =self.image.get_rect()
        self.rect.topleft = top_left
        self.lados = obtener_Rectangulos(self.rect)
        self.HP = 100

    def update(self):
        self.lados = obtener_Rectangulos(self.rect)

    def stop(self):
        self.speed = 0
     
    def activate(self):
        self.speed = 0