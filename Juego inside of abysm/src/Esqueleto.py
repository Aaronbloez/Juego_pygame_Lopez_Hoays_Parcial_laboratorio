import pygame
import random
from sprites import *


class Esqueleto(pygame.sprite.Sprite):


    def __init__(self, path_image:str,size:tuple, bootom:tuple,oleada:int,Volumen:float) -> None:
        super().__init__()
        self.animaciones = animations_skeleton()
        self.sonidos = sonido_esqueletos()
        self.indice = 0
        self.volumen = Volumen
        self.image = self.animaciones[self.indice]
        self.rect = self.image.get_rect()
        self.rect.midbottom = bootom
        self.rect.left
        self.speed_x = 2
        self.speed_y = 0
        self.contador_movimiento_derecha = 0
        self.contador_muerte = 0
        self.mirar_derecha = True
        self.vivo = True
        self.pegando = False
        self.contador_golpe = 0
        self.muriendo = False
        if oleada == 0:
            self.HP = 1
        elif oleada == 1:
            self.HP = 2
        elif oleada == 2:
            self.HP = 3
        elif oleada == 3:
            self.HP = 4
        elif oleada == 4:
            self.HP = 5
        elif oleada == 5:
            self.HP = 6
        elif oleada == 6:
            self.HP = 7
        elif oleada == 7:
            self.HP = 8
        elif oleada > 8:
            self.HP = 9
        elif oleada == 16:
            self.HP = 10
        elif oleada == 32:
            self.HP = 16
        else:
            self.HP = 1
        
    
    def update(self):
        if self.HP == None:
            self.HP = 1
            print("arreglado")
        

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.HP <= 0:
                self.muriendo = True
                match self.contador_muerte:
                    case 0:
                        #self.rect.bottom = (self.rect.x,550)
                        #self.rect.bottom =  (self.rect.y)
                        #self.rect.bottom = 550
                        #self.rect.y += 15
                        self.indice = 11
                        #self.sonidos['Muerte_esqueleto'].set_volume(self.volumen)
                        #self.sonidos['Muerte_esqueleto'].play()
                        self.contador_muerte += 1
                    case 1:
                        self.indice = 11
                        self.contador_muerte += 1
                    case 2:
                        #self.rect.y -= 10
                        self.indice = 12
                        self.contador_muerte += 1
                    case 3:

                        self.indice = 12
                        self.contador_muerte += 1
                    case 4:
                        self.indice = 13
                        self.contador_muerte += 1
                    case 5:
                        self.indice = 13
                        self.contador_muerte += 1
                    case 6:
                        #self.rect.y += 30
                        self.indice = 14
                        self.contador_muerte += 1
                    case 7:
                        self.indice = 14
                        self.contador_muerte += 1
                    case 8:
                        
                        self.indice = 15
                        self.contador_muerte += 1
                    case 9:
                        self.indice = 15
                        self.contador_muerte += 1
                    case 10:
                        self.rect.y = 490
                        self.indice = 16
                        self.contador_muerte += 1
                    case 11:
                        self.indice = 16
                        self.contador_muerte += 1
                    case 12:
                        self.rect.y = 500
                        self.indice = 17
                        self.contador_muerte += 1
                    case 13:
                        self.indice = 17
                        self.contador_muerte += 1
                    case 14:
                        #self.rect.y += 1
                        #self.rect.y = 530
                        #self.indice = 18
                        self.contador_muerte += 1
                    case 15:
                        #self.indice = 18
                        self.kill()
                        self.vivo = False
        elif self.mirar_derecha:
                if self.pegando and self.muriendo != True:
                    match self.contador_golpe:
                        case 0:
                            self.indice = 18
                            self.contador_golpe += 1
                        case 1:
                            self.indice = 18
                            self.contador_golpe += 1
                        case 2:
                            self.indice = 19
                            self.contador_golpe += 1
                        case 3:
                            self.indice = 19
                            self.contador_golpe += 1
                        case 4:
                            self.indice = 20
                            self.contador_golpe += 1
                        case 5:
                            self.indice = 21
                            self.contador_golpe += 1
                        case 6:
                            self.indice = 21
                            self.contador_golpe = 0
                            self.pegando = False
                else:     
                    match self.contador_movimiento_derecha:
                        case 0:
                            self.indice = 0
                            self.contador_movimiento_derecha += 1
                        case 1:
                            self.indice = 0
                            self.contador_movimiento_derecha += 1
                        case 2:
                            self.indice = 1
                            self.contador_movimiento_derecha += 1
                        case 3:
                            self.indice = 1
                            self.contador_movimiento_derecha += 1
                        case 4:
                            self.indice = 2
                            self.contador_movimiento_derecha += 1
                        case 5:
                            self.indice = 2
                            self.contador_movimiento_derecha += 1
                        case 6:
                            self.indice = 3
                            self.contador_movimiento_derecha += 1
                        case 7:
                            self.indice = 3
                            self.contador_movimiento_derecha += 1
                        case 8:
                            self.indice = 4
                            self.contador_movimiento_derecha += 1
                        case 9:
                            self.indice = 4
                            self.contador_movimiento_derecha += 1
                        case 10:
                            self.indice = 5
                            self.contador_movimiento_derecha += 1
                        case 11:
                            self.indice = 5
                            self.contador_movimiento_derecha += 1
                        case 12:
                            self.indice = 6
                            self.contador_movimiento_derecha += 1
                        case 13:
                            self.indice = 6
                            self.contador_movimiento_derecha += 1
                        case 14:
                            self.indice = 7
                            self.contador_movimiento_derecha += 1
                        case 15:
                            self.indice = 7
                            self.contador_movimiento_derecha += 1
                        case 16:
                            self.indice = 8
                            self.contador_movimiento_derecha += 1
                        case 17:
                            self.indice = 8
                            self.contador_movimiento_derecha += 1
                        case 18:
                            self.indice = 9
                            self.contador_movimiento_derecha += 1
                        case 19:
                            self.indice = 9
                            self.contador_movimiento_derecha += 1
                        case 20:
                            self.indice = 10
                            self.contador_movimiento_derecha += 1
                        case 21:
                            self.indice = 10
                            self.contador_movimiento_derecha = 0

        self.image = self.imagen = self.animaciones[self.indice]

    def stop(self):
       self.speed_x = 0

    def activate(self):
        self.speed_x = 2




