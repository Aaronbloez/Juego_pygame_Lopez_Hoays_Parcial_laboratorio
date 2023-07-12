import pygame
import sys
from Config import *
from player import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Inside of abysm")

fondo = pygame.image.load("assets\sprites\Fondo medieval.jpg").convert()
fondo = pygame.transform.scale(fondo,(WIDTH,HEIGHT))

suelo_1 = pygame.image.load("assets\sprites\Piso_lindo.png").convert_alpha()
suelo = pygame.transform.scale(suelo_1,(200,50))
suelo_rect = suelo.get_rect()


sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
suelo_grupo = pygame.sprite.Group()

goblin_slayer = player("assets\sprites\Slayer_not_moving_Left.png",GOBLIN_SIZE,(DISPLAY_CENTER_X,DISLAY_BOTTOM))
sprites.add(goblin_slayer)




contador_salto = 0
player_gravity = 0

rectangulo_left = pygame.Rect(goblin_slayer.rect.x-80,goblin_slayer.rect.y,80,70)

jumping = False
no_tocando_piso = True

while True:
    
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        key = pygame.key.get_pressed()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and contador_salto <= 1:
                player_gravity = -15
                contador_salto += 1
    
    if key[pygame.K_LEFT]:
        if goblin_slayer.rect.x > DISPLAY_LEFT:
            goblin_slayer.rect.x -= SLAYER_SPEED
            rectangulo_left = pygame.Rect(goblin_slayer.rect.x-80,goblin_slayer.rect.y-10,80,70)
    if key[pygame.K_RIGHT]:
        if goblin_slayer.rect.x < DISPLAY_RIGHT:
            goblin_slayer.rect.x += SLAYER_SPEED
            rectangulo_left = pygame.Rect(goblin_slayer.rect.x+40,goblin_slayer.rect.y-10,80,70)
     
    
    #rectangulo.topright = (goblin_slayer.rect.x + 120, goblin_slayer.rect.y)
    
    player_gravity += 1
    goblin_slayer.rect.y += player_gravity
    #if goblin_slayer.rect.colliderect(suelo_rect):
    #    goblin_slayer.rect.bottom = HEIGHT-50
    #    print(goblin_slayer.rect.y)
    #    contador_salto = 0
    if goblin_slayer.rect.bottom >= HEIGHT-50:
        goblin_slayer.rect.bottom = HEIGHT-50
        contador_salto = 0

                





    goblin_slayer.update()
    
    screen.blit(fondo, ORIGIN)
    screen.blit(suelo,(0,HEIGHT-50),suelo_rect)
    screen.blit(suelo,(200,HEIGHT-50),suelo_rect)
    screen.blit(suelo,(400,HEIGHT-50),suelo_rect)
    screen.blit(suelo,(600,HEIGHT-50),suelo_rect)  


    pygame.draw.rect(screen,(255,0,0),rectangulo_left)
    screen.blit(goblin_slayer.image,goblin_slayer.rect)
    


    pygame.display.flip()



