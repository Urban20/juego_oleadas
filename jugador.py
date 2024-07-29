import pygame,time,imagenes
pygame.mixer.init()
fuera_del_mapa = None
#stats del jugador------------------
jugador_spawnx= imagenes.resolx / 2
jugador_spawny= imagenes.resoly / 2
vel_default = 2.7
vel_debuf = 1
daño_jugador = 20
jugador_vida = 50
cooldown_disparo = 0.25
#stats del jugador------------------

rifle = pygame.mixer.Sound('elementos/sonidos/Futuristic Sniper Rifle Single Shot.wav')

class Jugador(pygame.sprite.Sprite):
    def __init__(self,vel,spawnx,spawny,salud,sonido):
        super().__init__()
        self.coordx = spawnx
        self.coordy = spawny
        self.velx = vel
        self.vely = vel
        self.direccion = 'der'
        self.quieto = True
        self.disparando = False
        self.caminando = False
       
        self.salud = salud
        self.buffeado = False
        self.sonido = sonido
  
        self.tiempo = time.time()
    def barra_salud(self,jugador_vida):
        #barra roja
        pygame.draw.rect(imagenes.pantalla,imagenes.rojo,(self.coordx,self.coordy - 10,jugador_vida,5))
        #barra verde
        pygame.draw.rect(imagenes.pantalla,imagenes.verde,(self.coordx,self.coordy - 10,self.salud,5))

    def hitbox(self):
        hitbox= pygame.Rect(self.coordx,self.coordy,75,91)
        return hitbox

    def dibujo(self):
        fotogramas= int(time.time()*5) % 7
        if self.direccion == 'der' and not self.quieto and not self.disparando and self.caminando:
            imagenes.pantalla.blit(imagenes.jugador_der[fotogramas],(self.coordx,self.coordy))
        elif self.direccion == 'izq' and not self.quieto and not self.disparando and self.caminando:
            imagenes.pantalla.blit(imagenes.jugador_izq[fotogramas],(self.coordx,self.coordy))
        
            
    def teclas(self,teclado):
        fotograma_disparo= int(time.time()* 10) % 4
        
        if teclado[pygame.K_a] and not self.disparando:
            self.coordx -= self.velx
            self.direccion = 'izq'
            self.quieto = False
            self.caminando = True
        elif teclado[pygame.K_d] and not self.disparando:
            self.coordx += self.velx
            self.direccion = 'der'
            self.quieto = False
            self.caminando = True
        elif teclado[pygame.K_s] and not self.disparando:
            self.coordy += self.vely
            self.quieto = False
            self.caminando = True
        elif teclado[pygame.K_w] and not self.disparando:
            self.coordy -= self.vely
            self.quieto = False
            self.caminando = True
        
        else:
            self.quieto = True
            self.caminando = False
        #estado quieto---------------------------------------------------
        if self.quieto and self.direccion == 'der' and not self.disparando:
            fotogramas= int(time.time()*5) % 7
            imagenes.pantalla.blit(imagenes.jugador_quieto[fotogramas],(self.coordx,self.coordy))
        elif self.quieto and self.direccion == 'izq'and not self.disparando:
            fotogramas= int(time.time()*5) % 7
            imagenes.pantalla.blit(imagenes.jugador_quieto_izq[fotogramas],(self.coordx,self.coordy))
        #disparo------------------------------------------------------------
        if self.disparando and self.direccion == 'der':
            self.quieto = False
            imagenes.pantalla.blit(imagenes.jugador_disparo[fotograma_disparo],(self.coordx,self.coordy))
            self.caminando = False
            
        elif self.disparando and self.direccion == 'izq':
            self.quieto = False
            imagenes.pantalla.blit(imagenes.jugador_disparo_izq[fotograma_disparo],(self.coordx,self.coordy))
            
            self.caminando = False
        if self.disparando and time.time() - self.tiempo >= cooldown_disparo:
            pygame.mixer.Channel(2).play(self.sonido)
            self.tiempo = time.time()

    def disparar(self,teclas):
        
        if teclas[pygame.K_e]:
            self.disparando = True
            self.quieto = False
            
           
            bala1= Bala(self.direccion,self.coordx + 78,self.coordy + 12,daño_jugador)
            imagenes.bala_jugador.append(bala1)
              
        else:
            self.disparando = False
            
        
        
jugador = Jugador(vel=vel_default,spawny=jugador_spawny,spawnx=jugador_spawnx,salud=jugador_vida,sonido=rifle)

class Bala():
    def __init__(self,direccion,posx,posy,daño):
        
        self.imagen = imagenes.bala
        
        self.posx = posx
        self.posy = posy
        self.direccion= direccion
        self.velx = 100
        self.daño = daño

    def disparo(self):
        if self.direccion == 'der':
            imagenes.pantalla.blit(imagenes.bala,(self.posx,self.posy))
            self.posx += self.velx
        elif self.direccion == 'izq':
            imagenes.pantalla.blit(imagenes.bala_izq,(self.posx-85,self.posy))
            self.posx -= self.velx
    def hitbox(self):
        hitbox_bala= pygame.Rect(self.posx,self.posy,15,15)
        return hitbox_bala