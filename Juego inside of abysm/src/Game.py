import pygame
import sys
from player import *
from Plataforma import *
from Menus import *
from Config import *
from Puerta import *
from sprites import *
from Esqueleto import *
from ultimate import *
from funciones import *
  #  
class Game:
    def __init__(self) -> None:
        pygame.init()
      

        self.MASTER_VOLUMEN = 0.5
        self.reloj = pygame.time.Clock()
        self.fuente = pygame.font.Font(r"assets\Fuente\King Arthur Legend.ttf",18)
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Valor's Defense")
        self.icono = pygame.image.load(r"assets\Fondos y cosa\Castillo valoria.jpg").convert_alpha()
        self.icono = pygame.transform.scale(self.icono,(SIZE_ICON))
        self.fondo = pygame.transform.scale(pygame.image.load(
            r"assets\sprites\Fondo_abysm.jpg").convert(),(WIDTH,HEIGHT))
        self.musica = Musica_juego()
        self.sprites = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.ulti = pygame.sprite.Group()
        self.superficies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.jugador = pygame.sprite.Group()
        self.goblin_slayer = player(r"assets\sprites\0.png",(GOBLIN_SIZE),(DISPLAY_RIGHT,0))
        self.sprites.add(self.goblin_slayer)
        self.jugador.add(self.goblin_slayer)
        self.suelo_1 = pygame.image.load(r"assets\sprites\Piso_lindo.png").convert_alpha()
        self.suelo = pygame.transform.scale(self.suelo_1,(200,50))
        self.puerta = Puerta("assets\Gran Puerta.png",(100,500),(700,100))
        self.plataforma = Plataforma(r"assets\sprites\Piso_lindo.png",(200,50),(DISPLAY_RIGHT-300,350))
        self.sprites.add(self.plataforma)
        self.superficies.add(self.plataforma)
        self.sprites.add(self.puerta)
        self.superficies.add(self.puerta)
        self.suelo_rect = self.suelo.get_rect()
        self.contador_salto = 0
        self.player_gravity = 0
        self.flag_esqueleto = False
        self.rectangulo_left = pygame.Rect(self.goblin_slayer.rect.x-900,self.goblin_slayer.rect.y-900,150,70)
        #self.rectangulo = pygame.image.load(r"assets\sprites\Movimiento player\ATTACK\Fueguito rojo_.png").convert_alpha()
        #s##elf.rectangulo_left = self.rectangulo.get_rect
        #self.ultimate = Ulti(r"assets\sprites\Movimiento player\ATTACK\ULT VELORIA.png",(50,25),(x,y),10)
        #self.sprites.add(self.ultimate)
        self.puerta_castillo = pygame.Rect(700,200,100,400)
        self.bajar_tecla = False
        self.esta_jugando = False
        self.is_running = False
        self.is_game_over = False
        self.cayendo = True
        self.flag_musica_juego = True
        self.flag_musica_Menu = True
        self.flag_musica_Game_Over = True
        pygame.display.set_icon(self.icono)
        self.score = 0
        self.timer = 300
        self.Num_oleada = 0
        self.score = 0
        self.contador_tiempo_saltado = 0
        
                         
    def comenzar(self):
        self.is_playing = False
        self.is_running = True
        self.elementos_pausados = False

        while self.is_running:
            self.reloj.tick(FPS)
            if self.is_playing:
                self.manejador_de_eventos()
            self.update()
            self.render()

    def manejador_de_eventos(self):
        #self.cayendo = True
        self.bajar_tecla = False
        if self.flag_musica_juego:
            self.musica['Musica_Juego'].set_volume(self.MASTER_VOLUMEN)

            self.musica['Musica_Juego'].play()
            self.flag_musica_juego = False
        if self.cayendo:
            for sprite in self.superficies:
                if sprite.lados['top'].colliderect(self.goblin_slayer.lados['bottom']):
                    if self.goblin_slayer.speed_y < 0:
                        pass
                    else:
                        self.goblin_slayer.speed_y = 0
                        self.goblin_slayer.saltar = False
                        self.goblin_slayer.rect.bottom = sprite.rect.top
                        self.contador_salto = 0
                    
                    self.colisionando_plataforma = True
                    self.goblin_slayer.rect.y += 1
                    self.contador_salto = 0
                else:
                    self.colisionando_plataforma = False
        if self.goblin_slayer.rect.bottom >= HEIGHT-50:
                self.goblin_slayer.speed_y = 0
                self.cayendo = False
                self.goblin_slayer.rect.bottom = HEIGHT-50
                self.goblin_slayer.saltar = False
                self.contador_salto = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.elementos_pausados == False:
                    self.Mostar_pantalla_pausa()
                    self.parar_elementos()
                elif event.key == pygame.K_ESCAPE and self.elementos_pausados == True:
                    self.despausar_elementos()
                if self.elementos_pausados != True:
                    if event.type == pygame.KEYDOWN:
                        self.bajar_tecla = True
                        if event.key == pygame.K_SPACE and self.contador_salto <= 1:
                            self.contador_tiempo_saltado = 0
                            self.goblin_slayer.saltar = True
                            self.goblin_slayer.speed_y = -15
                            self.contador_salto += 1
                            self.cayendo = True
                        if event.key == pygame.K_x and self.goblin_slayer.Mana > 25:
                            if self.goblin_slayer.HP > 150:
                                self.goblin_slayer.HP = 200
                            else:
                                self.goblin_slayer.HP += 50
                            self.goblin_slayer.Mana -= 25
                        if event.key == pygame.K_z and self.goblin_slayer.Mana > 99:
                            self.ultimate = GenerarUltimate(self.sprites,self.ulti,self.MASTER_VOLUMEN,self.goblin_slayer.rect.x,self.goblin_slayer.rect.y,self.goblin_slayer.mirar_derecha)
                            self.goblin_slayer.Mana -= 100
                            
                            self.goblin_slayer.Mana -= 100
                            pass
                        if event.key == pygame.K_c:
                            self.goblin_slayer.pegando = True
                            
                            if self.goblin_slayer.mirar_derecha:
                                self.rectangulo_left = pygame.Rect(self.goblin_slayer.rect.x+40,self.goblin_slayer.rect.y-10,100,70)
                            else:
                                self.rectangulo_left = pygame.Rect(self.goblin_slayer.rect.x-80,self.goblin_slayer.rect.y-10,200,70)
                        else:
                            self.rectangulo_left = pygame.Rect(self.goblin_slayer.rect.x-900,self.goblin_slayer.rect.y-900,80,70)
        if self.elementos_pausados != True:

            if  self.bajar_tecla != True:
                self.rectangulo_left = pygame.Rect(self.goblin_slayer.rect.x-900,self.goblin_slayer.rect.y-900,80,70)
                key = pygame.key.get_pressed()
                #generar_esqueletos(self.sprites,self.enemys,self.screen,5)
                if key[pygame.K_LEFT]:
                    if self.goblin_slayer.rect.x > DISPLAY_LEFT:
                        self.goblin_slayer.caminando = True
                        self.goblin_slayer.rect.x -= SLAYER_SPEED
                        self.goblin_slayer.mirar_derecha = False
                        self.goblin_slayer.mirar_izquierda = True
                elif key[pygame.K_RIGHT]:
                    if self.goblin_slayer.rect.x < DISPLAY_RIGHT:
                        self.goblin_slayer.caminando = True
                        self.goblin_slayer.rect.x += SLAYER_SPEED
                        self.goblin_slayer.mirar_derecha = True
                        self.goblin_slayer.mirar_izquierda = False
                else:
                    self.goblin_slayer.caminando = False 
                
        self.colisionando_plataforma = False

        if self.colisionando_plataforma:
            self.goblin_slayer.speed_y = 0
        else:
            self.goblin_slayer.speed_y += 1
            self.contador_tiempo_saltado += 1
            

       
        GenerarFlechas(self.sprites,self.projectiles,self.screen,self.MASTER_VOLUMEN,5)
        generar_esqueletos(self.sprites,self.enemys,self.Num_oleada,self.MASTER_VOLUMEN,5)

        if self.goblin_slayer.HP <= 0:
            self.musica['Musica_Juego'].stop()
            self.flag_musica_juego = True
            self.is_game_over = True
            self.is_playing = False
        if self.elementos_pausados == False:
            self.timer -= 1
            if self.timer == 0:
                print("Cambio de oleada")
                self.Num_oleada += 1
                self.timer = 300




    def update(self):
        self.eliminar_elementos_fuera_de_pantalla()
        self.detectar_coliciones()
        self.sprites.update()
        
    def detectar_coliciones(self):
        if self.elementos_pausados != True:
            for flecha in self.projectiles:
                if self.rectangulo_left.colliderect(flecha.rect):
                    flecha.sonidos['Flecha_rota'].set_volume(self.MASTER_VOLUMEN)
                    flecha.sonidos['Flecha_rota'].play()
                    flecha.pego = True
                    self.score += 20
                if flecha.rect.colliderect(self.goblin_slayer.rect):
                    self.goblin_slayer.HP -= 5
                    flecha.sonidos['Flecha_impacto_jugador'].play()
                    if self.goblin_slayer.rect.x > 500:
                        pass
                    else:
                        self.goblin_slayer.rect.x += 20
                    flecha.pego = True

            for esqueleto in self.enemys:
                
                if self.rectangulo_left.colliderect(esqueleto.rect):
                    self.score += 20
                    esqueleto.HP -= 1
                    self.goblin_slayer.contador_kill += 1
                for ultimate in self.ulti:
                    if ultimate.rect.colliderect(esqueleto.rect):
                        esqueleto.HP -= 50
                if esqueleto.rect.colliderect(self.goblin_slayer.rect):
                    esqueleto.sonidos['Golpe_jugador'].set_volume(self.MASTER_VOLUMEN)
                    esqueleto.sonidos['Golpe_jugador'].play()
                    esqueleto.pegando = True
                    if self.goblin_slayer.rect.x > 600:
                        pass
                    else:
                        self.goblin_slayer.rect.x += 20
                    self.goblin_slayer.HP -= 1
                if esqueleto.rect.colliderect(self.puerta.rect):
                    esqueleto.sonidos['Golpe_puerta'].set_volume(self.MASTER_VOLUMEN)
                    esqueleto.sonidos['Golpe_puerta'].play()
                    self.puerta.HP -= 1
                    if self.puerta.HP <= 0:
                        self.musica['Musica_Juego'].stop()
                        self.flag_musica_juego = True
                        self.is_game_over = True
                        self.is_playing = False
                    print(self.puerta.HP)
                    esqueleto.pegando = True
                    esqueleto.rect.x -= SLAYER_SPEED
            #for ultimate in self.ulti:
            #    for esqueleto in self.enemys:
            #        if ultimate.rect.colliderect(esqueleto.rect):
            #            esqueleto.HP -= 50
            
        

            #for player in self.jugador:
            #    if self.superficies.rect.colliderect(player.rect):
            ##        if player.mirar_derecha:
            #          player.rect.right = self.superficies.rect.left
            #      elif player.self.mirar_izquierda:
          #          player.rect.left = self.superficies.rect.right

        pass
    def eliminar_elementos_fuera_de_pantalla(self):
        for flecha in self.projectiles:
            if flecha.rect.right > DISPLAY_RIGHT+50:
                flecha.kill()


    def render(self):
        if self.is_playing:
            self.screen.blit(self.fondo, ORIGIN)
            self.screen.blit(self.suelo,(0,HEIGHT-50),self.suelo_rect)
            self.screen.blit(self.suelo,(200,HEIGHT-50),self.suelo_rect)
            self.screen.blit(self.suelo,(400,HEIGHT-50),self.suelo_rect)
            self.screen.blit(self.suelo,(600,HEIGHT-50),self.suelo_rect) 
            self.screen.blit(self.fuente.render("Score " + str(self.score),True,ROJO),  SCORE_POS) 
            self.screen.blit(self.fuente.render("Oleada " + str(self.Num_oleada),True,(0,255,0)),(50,200)) 
            Barra_de_vida_jugador(self.screen,self.goblin_slayer.HP,100)
            Barra_de_vida_Puerta(self.screen,self.puerta.HP,300)
            Barra_de_mana(self.screen,self.goblin_slayer.Mana,100)
            #pygame.draw.rect(self.screen,(255,0,0),self.rectangulo_left)
            pygame.draw.rect(self.screen,(255,0,0),self.puerta_castillo)
            self.sprites.draw(self.screen)
            #self.screen.blit(self.esqueleto_enemigo,self.esqueleto_enemigo.rect)
        elif self.is_game_over:
            self.show_game_over_screen()
        elif self.elementos_pausados:
            self.Mostar_pantalla_pausa()
        else:
            self.Mostrar_menu_juego()
        
        #else:
        pygame.display.flip()

    
    def parar_elementos(self):
        self.is_playing = False
        for sprite in self.sprites:
            self.elementos_pausados = True
            sprite.stop()
    
    def despausar_elementos(self):
        self.is_playing = True
        for sprite in self.sprites:
            self.elementos_pausados = False
            sprite.activate()

            

    def Mostar_pantalla_pausa(self):
        fondo_pausa = pygame.transform.scale(pygame.image.load(
            r"assets\Fondos y cosa\Menu Defend of valoria.jpg").convert(),(WIDTH,HEIGHT))
        texto = self.fuente.render("Pause",True,(0,0,255))
        texto_rect = texto.get_rect()
        texto_rect.center = (WIDTH//2,HEIGHT//2)
        self.screen.blit(fondo_pausa, ORIGIN)
        self.screen.blit(texto,texto_rect)
        self.screen.blit(self.fuente.render("Score " + str(self.score),True,ROJO),  SCORE_POS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_playing = True
                    self.despausar_elementos()

    def exit(self):
        self.is_running = False

    def show_game_over_screen(self):
        self.parar_elementos()  
        fondo_game_over = pygame.transform.scale(pygame.image.load(
            r"assets\Fondos y cosa\Game over foto.jpg").convert(),(WIDTH,HEIGHT))
        if self.flag_musica_Game_Over:
            self.flag_musica_Game_Over = False
            self.musica['Musica_Game_over'].set_volume(self.MASTER_VOLUMEN)
            self.musica['Musica_Game_over'].play()
            print("entra")
        texto = self.fuente.render("Game Over",True,(0,0,255))
        texto1 = self.fuente.render("Varoia a caido",True,(0,0,255))
        texto_rect = texto.get_rect()
        texto1_rect = texto1.get_rect()
        texto_rect.center = (WIDTH//2,HEIGHT//2)
        texto1_rect.center = (WIDTH//2,HEIGHT-50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Guardar_score(self.score,self.Num_oleada)
                    self.flag_musica_Game_Over = True
                    #self.musica['Musica_Game_over'].stop()
                    self.despausar_elementos()
                    self.Reiniciar_el_juego()
                #elif event.key == pygame.K_RETURN:
                #    print("guarda")
                #    Guardar_score(self.score,self.Num_oleada)
                elif event.key == pygame.K_w:
                    b = Sacar_score_del_csv()
                    print(b)
                   # a = Mostar_score_mas_alto()
                   #print(a)

        self.screen.blit(fondo_game_over,ORIGIN)
        self.screen.blit(texto,texto_rect)
        self.screen.blit(texto1,texto1_rect)
        self.screen.blit(self.fuente.render("Score final: " + str(self.score),True,ROJO),  SCORE_POS) 
        pygame.display.flip()
        

    

    def Reiniciar_el_juego(self):

        self.is_game_over = False
        self.is_playing = True
        self.score = 0
        self.Num_oleada = 0
        self.goblin_slayer.HP = 200
        self.goblin_slayer.Mana = 0
        self.sprites.empty()
        self.enemys.empty()
        self.projectiles.empty()
        self.superficies.empty()
        self.sprites.add(self.goblin_slayer)
        self.goblin_slayer.rect.center = (DISPLAY_RIGHT-50,200)
        self.sprites.add(self.plataforma)
        self.sprites.add(self.puerta)
        self.superficies.add(self.plataforma)

    def Mostrar_menu_juego(self):
        fondo_Menu = pygame.transform.scale(pygame.image.load(
            r"assets\Fondos y cosa\Menu Inicio Valoria.png").convert(),(WIDTH,HEIGHT))
        Score_mas_alto = Sacar_score_del_csv()
        if self.flag_musica_Menu:
            self.flag_musica_Menu = False
            self.musica['Musica_menu'].set_volume(self.MASTER_VOLUMEN)
            self.musica['Musica_menu'].play()
        texto_volumen_lindo = str(self.MASTER_VOLUMEN)
        Volumen_mostrar = []
        contador_numero = 0
        for numero in texto_volumen_lindo:
            if contador_numero < 3:
                Volumen_mostrar.append(numero)
                contador_numero += 1
        b = Sacar_score_del_csv()
        
        Volumen_mostrar = str(Volumen_mostrar).replace("'","").replace("[","").replace("]","").replace(" ","").replace(",","").replace(".",",")
        Score_mas_alto = str(Score_mas_alto).replace("'","").replace("[","").replace("]","").replace(" ","").replace(".",",")
        Score_mas_alto_mostar = self.fuente.render("Score mas alto:"+str(Score_mas_alto),True,(0,0,255))
        Score_mas_alto_mostar_rect = Score_mas_alto_mostar.get_rect()
        Score_mas_alto_mostar_rect.center = (450,200)
        texto = self.fuente.render("Menu Inicio",True,(0,0,255))
        texto_volumen = self.fuente.render("Volument"+str(Volumen_mostrar),True,(0,0,255))
        texto_volumen_rect = texto_volumen.get_rect()
        texto_volumen_rect.center = (175,200)
        texto_rect = texto.get_rect()
        texto_rect.center = (315,80)

        self.screen.blit(fondo_Menu,ORIGIN)
        self.screen.blit(texto,texto_rect)
        self.screen.blit(Score_mas_alto_mostar,Score_mas_alto_mostar_rect)
        self.screen.blit(texto_volumen,texto_volumen_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicion_clic = pygame.mouse.get_pos()
            key = pygame.key.get_pressed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.MASTER_VOLUMEN > 0.2:
                    self.MASTER_VOLUMEN -= 0.1
                if event.key == pygame.K_UP and self.MASTER_VOLUMEN < 1:
                    self.MASTER_VOLUMEN += 0.1
                if event.key == pygame.K_ESCAPE:
                    #self.musica['Musica_menu'].stop()
                    self.flag_musica_Menu = True
                    self.is_playing = True
               

        #self.screen.blit(self.fuente.render("Score " + str(self.score),True,ROJO),  SCORE_POS) 
        pygame.display.flip()
 


