import pygame
import random
import json
import csv
from Flechas import *
from ultimate import *
from Esqueleto import Esqueleto
from Config import *

def generar_esqueletos(g_sprites,g_esqueletos,oleada:int,volumen,count = 5):
        if len(g_esqueletos) == 0:
            for i in range(count):
                    x = random.randrange(-300,0)
                    esqueleto = Esqueleto("assets\sprites\Esqueleto\Esquyeleto movimiento0.png",(GOBLIN_SIZE),(x,550),oleada,volumen)
                    g_esqueletos.add(esqueleto)
                    g_sprites.add(esqueleto)


def GenerarFlechas(g_sprites,g_proyectiles,screen:pygame.Surface,volumen,count = 5):
        if len(g_proyectiles) == 0:
            for i in range(count):
                x = random.randrange(-1600,0)
                y = random.randrange(300,HEIGHT-50)
                flecha = Flecha(r"assets\sprites\Ataques\Flecha fuego png.png",(50,25),(x,y),10)
                
                g_proyectiles.add(flecha)
                g_sprites.add(flecha)

def GenerarUltimate(g_sprites,g_ulti,volumen,eje_x_personaje,eje_y_personaje,mirar_derecha):
    if mirar_derecha:
        Ult = Ulti(r"assets\sprites\Movimiento player\ATTACK\ULT VELORIA_derecha_bien_hecho.png",(100,200),(eje_x_personaje,eje_y_personaje),volumen,10)
    else:
        Ult = Ulti(r"assets\sprites\Movimiento player\ATTACK\ULT VELORIA_izquierda_bien_hecho.png",(100,200),(eje_x_personaje,eje_y_personaje),volumen,-10)
    g_ulti.add(Ult)
    g_sprites.add(Ult)
    return Ult
                


#def Generar_plataforas():
     

              
def Guardar_score(score:int,oleada_sobrevivivdas:int):
    with open("Historial_puntajes.csv","a") as file:

        file.write(str(score) +"," +str(oleada_sobrevivivdas) + "\n")

def Sacar_score_del_csv():
    lista = []
    score_mayor_flag = True

    with open("Historial_puntajes.csv","r") as file:

        lineas = csv.reader(file)
        casa = list(lineas)
    
    for i in casa:

        a = int(i[0])

        if score_mayor_flag:
            score_mayor = a
            score_mayor_flag = False
            b = int(i[1])
        elif a > score_mayor:
            score_mayor = a
            b = int(i[1])
    lista.append(score_mayor)
    lista.append(b)
    return score_mayor
        
def obtener_Rectangulos(principal)->dict:
    diccionario = {}
    diccionario['main'] = principal

    diccionario['bottom'] = pygame.Rect(principal.left,principal.bottom -6, principal.width, 6)
    diccionario['right'] = pygame.Rect(principal.right-6,principal.top, 6, principal.height)
    diccionario['left'] = pygame.Rect(principal.left,principal.top ,6, principal.height)
    diccionario['top'] = pygame.Rect(principal.left,principal.top, principal.width, 6)
    return diccionario

def Barra_de_vida_jugador(screen,vida_actual:str,vida_total:str):
    largo = 200
    alto = 12
    borde = 4
    vida_relativa = vida_actual/vida_total
    pygame.draw.rect(screen, ROJO, (100- largo // 2, 50, largo, alto))
    pygame.draw.rect(screen, VERDE, (100 - largo // 2, 50, 100 *vida_relativa, alto))
    pygame.draw.rect(screen, NEGRO, (100 - largo //2,50, largo,alto), borde)

def Barra_de_vida_Puerta(screen,vida_actual:str,vida_total:str):
    largo = 200
    alto = 12
    borde = 4
    vida_relativa = vida_actual/vida_total
    pygame.draw.rect(screen, ROJO, (400+ largo // 3, 50, largo, alto))
    pygame.draw.rect(screen, VERDE, (400 + largo // 3, 50, 200 *vida_relativa, alto))
    pygame.draw.rect(screen, NEGRO, (400 + largo //3,50, largo,alto), borde)

def Barra_de_mana(screen,Mana_actual:str,Mana_total:str):
    largo = 200
    alto = 12
    borde = 4
    vida_relativa = Mana_actual/Mana_total
    pygame.draw.rect(screen, CELESTITO, (100- largo // 2, 63, largo, alto))
    pygame.draw.rect(screen, AZUL, (100 - largo // 2, 63, largo *vida_relativa, alto))
    pygame.draw.rect(screen, NEGRO, (100 - largo //2,63, largo,alto), borde)
      

#pygame.draw.rect(screen, ROJO, (borde // 2+100- largo // 2, 50, largo, alto))
 #   pygame.draw.rect(screen, VERDE, (borde // 2+100 - largo // 2, 50, largo *vida_relativa, alto))
  #  pygame.draw.rect(screen, NEGRO, (borde//2+100 - largo //2,50, largo,alto), borde)
#
#
    
    

