import pygame
from funciones import *
from sprites import *



class player(pygame.sprite.Sprite):
    def __init__(self, path_image:str,size:tuple, bootom:tuple) -> None:
        super().__init__()
        self.animaciones = animations_atack()
        self.indice = 0
        self.image = self.animaciones[self.indice]
        self.rect = self.image.get_rect()
        self.rect.bottomright = bootom
        #self.lados = obtener_Rectangulos(self.rect)
        self.rect.left
        self.speed_x = 0
        self.speed_y = 0
        self.contador_golpe = 0
        self.contador_mirar_derecha = 0
        self.contador_mirar_izquierda = 0
        self.contador_recibiendo_golpe = 0
        self.mirar_derecha = True
        self.mirar_izquierda = False
        self.saltar = False
        self.caminando = False
        self.pegando = False
        self.animacion_golpe = False
        self.altura_anterior = 550
        self.HP = 200
        self.Mana = 0
        self.contador_kill = 0
        self.HP_anterior = 200
        
        
    def update(self):
        self.lados = obtener_Rectangulos(self.rect)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        #Coliciones
        
        #Animacones
        if self.contador_kill >= 3:
            if self.Mana <= 95:
                self.Mana += 5
            elif self.Mana <100:
                self.Mana = 100
            self.contador_kill = 0

        if self.mirar_derecha:
            self.indice = 10
            if self.caminando and self.saltar != True:
                match self.contador_mirar_derecha:
                    case 0:
                        self.indice = 1
                        self.contador_mirar_derecha += 1
                    case 1:
                        self.indice = 2
                        self.contador_mirar_derecha += 1
                    case 2:
                        self.indice = 3
                        self.contador_mirar_derecha += 1
                    case 3:
                        self.indice = 4
                        self.contador_mirar_derecha += 1
                    case 4:
                        self.indice = 5
                        self.contador_mirar_derecha += 1
                    case 5:
                        self.indice = 6
                        self.contador_mirar_derecha += 1
                    case 6:
                        self.indice = 7
                        self.contador_mirar_derecha += 1
                    case 7:
                        self.indice = 8
                        self.contador_mirar_derecha += 1
                    case 8:
                        self.indice = 9
                        self.contador_mirar_derecha = 0
        
            if self.pegando:
            
                match self.contador_golpe:
                    case 0:
                        self.indice = 11
                        self.contador_golpe += 1
                    case 1:
                        self.indice = 12
                        self.contador_golpe += 1
                    case 2:
                        self.indice = 13
                        self.contador_golpe += 1
                    case 3:
                        self.indice = 14
                        self.pegando = False
                        self.contador_golpe = 0
            if self.saltar:
                if self.rect.y >= self.altura_anterior:
                    self.indice = 15
                else:
                    self.indice = 32
                self.altura_anterior = self.rect.y
            if self.HP != self.HP_anterior or self.animacion_golpe == True:
                self.indice = 35
                self.animacion_golpe = True
                self.contador_recibiendo_golpe += 1
                if self.contador_recibiendo_golpe >= 3:
                    self.animacion_golpe = False
            self.HP_anterior = self.HP

        
        if self.mirar_izquierda:
            self.indice = 26
            
            if self.caminando and self.saltar != True:
                match self.contador_mirar_izquierda:
                    case 0:
                        self.indice = 16
                        self.contador_mirar_izquierda += 1
                    case 1:
                        self.indice = 17
                        self.contador_mirar_izquierda += 1
                    case 2:
                        self.indice = 19
                        self.contador_mirar_izquierda += 1
                    case 3:
                        self.indice = 20
                        self.contador_mirar_izquierda += 1
                    case 4:
                        self.indice = 21
                        self.contador_mirar_izquierda += 1
                    case 5:
                        self.indice = 22
                        self.contador_mirar_izquierda += 1
                    case 6:
                        self.indice = 23
                        self.contador_mirar_izquierda += 1
                    case 7:
                        self.indice = 24
                        self.contador_mirar_izquierda += 1
                    case 8:
                        self.indice = 25
                        self.contador_mirar_izquierda = 0
        
            if self.pegando:
                
                match self.contador_golpe:
                    case 0:
                        self.indice = 27
                        self.contador_golpe += 1
                    case 1:
                        self.indice = 28
                        self.contador_golpe += 1
                    case 2:
                        self.indice = 29
                        self.contador_golpe += 1
                    case 3:
                        self.indice = 30
                        self.pegando = False
                        self.contador_golpe = 0
            if self.saltar:
                if self.rect.y >= self.altura_anterior:
                    self.indice = 31
                else:
                    self.indice = 33
                self.altura_anterior = self.rect.y
            if self.HP != self.HP_anterior or self.animacion_golpe == True:
                self.indice = 36
                self.animacion_golpe = True
                self.contador_recibiendo_golpe += 1
                if self.contador_recibiendo_golpe >= 3:
                    self.animacion_golpe = False

            self.HP_anterior = self.HP

        self.image = self.imagen = self.animaciones[self.indice]
            
    

        
       
    def stop(self):
        self.speed_x = 0
        self.speed_y = 0

    def activate(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
   

 




