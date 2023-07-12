import pygame
from Config import *


def animations_atack():
    animaciones = [pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Caer_derecha.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha0.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha2.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha3.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha4.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha5.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha6.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha7.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha8.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Corre_derecha9.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\0.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\ATTACK\ataqueDerecha0.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\ATTACK\ataqueDerecha1.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\ATTACK\ataqueDerecha2.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\ATTACK\ataqueDerecha3.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Salto_derecha.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_Izuierda0.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda1.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda2.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda3.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda4.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda5.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda6.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda7.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda8.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Corre_izquierda9.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Quito_izquierda.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Ataque_izquierda\ataqueizquierda0.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Ataque_izquierda\ataqueizquierda1.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Ataque_izquierda\ataqueizquierda2.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Ataque_izquierda\ataqueizquierda3.png").convert_alpha(),(100,60)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Salto_izquierda.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Correr\Caer_derecha.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Corre_Izquierda\Caer_izquierda.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Ojo_volador\0.png").convert_alpha(),(GOBLIN_SIZE)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Hits\Golpe_caballero_derecha.png").convert_alpha(),(60,50)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Movimiento player\Hits\Golpe_caballero_izquierda.png").convert_alpha(),(60,50)),]

    return animaciones

def animations_skeleton():
    animaciones = [pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha0.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha1.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha2.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha3.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha4.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha5.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha6.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha7.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha8.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha9.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha10.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_derecha11.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_0.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_1.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_2.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_muerto4 (1).png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_muerto5.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Esqueleto_caido_6.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Golpe_derecha0.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Golpe_derecha1.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Golpe_derecha2.png").convert_alpha(),(90,70)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_3.png").convert_alpha(),(60,20)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_3.png").convert_alpha(),(60,20)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_3.png").convert_alpha(),(60,20)),
                   pygame.transform.scale(pygame.image.load(r"assets\sprites\Esqueleto\Muerte_esqueleto_3.png").convert_alpha(),(60,20)),]
    return animaciones
def sonido_esqueletos():
    diccionario = {}
    diccionario['Muerte_esqueleto'] = pygame.mixer.Sound(r"assets\Sonido\death.ogg")
    diccionario['Golpe_puerta'] = pygame.mixer.Sound(r"assets\Sonido\Golpe_esqueleto_puerta.wav")
    diccionario['Golpe_jugador'] = pygame.mixer.Sound(r"assets\Sonido\Golpe_esqueleto_para_jugador.wav")
    return diccionario

def sonido_flechas():
    diccionario = {}
    diccionario['Flecha_impacto_jugador'] = pygame.mixer.Sound(r"assets\Sonido\Flecha golpeando.wav")
    diccionario['Flecha_rota'] = pygame.mixer.Sound(r"assets\Sonido\Flecha_rompiendose.wav")
    return diccionario

def Musica_juego():
    diccionario = {}
    diccionario['Musica_menu'] = pygame.mixer.Sound(r"assets\Sonido\Musica\Theme of Reg  Made in Abyss OST cover.mp3")
    diccionario['Musica_Juego'] = pygame.mixer.Sound(r"assets\Sonido\Musica\RPG Combat Music  The Rise Of The Valkyries.mp3")
    diccionario['Musica_Game_over'] = pygame.mixer.Sound(r"assets\Sonido\Musica\Gwyn, Lord of Cinder - Dark Souls Soundtrack.mp3")
    #diccionario['Musica_Pausa'] = pygame.mixer.Sound(r"assets\Sonido\death.ogg")
    return diccionario

def Golpe_esqueleto():
    diccionario = {}
    diccionario['Golpe_puerta'] = pygame.mixer.Sound(r"assets\Sonido\Golpe_esqueleto_puerta.wav")
    diccionario['Golpe_jugador'] = pygame.mixer.Sound(r"assets\Sonido\Golpe_esqueleto_para_jugador.wav")


    
    
    


    




