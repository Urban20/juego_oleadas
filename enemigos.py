import pygame,jugador,imagenes,time


grupo_enemigos = []

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy,vel,salud):
        super().__init__()
        self.posx = posx
        self.posy = posy
        self.direccion = None
        self.atacando= False
        self.caminando = True
        self.daño = False
        self.muerte = False

        self.velx = vel
        self.vely = vel

        self.salud = salud

    def dibujo(self):
        fotograma= int(time.time()* 4) % 8
        if jugador.jugador.coordx > self.posx:
            self.direccion = 'der'
        else:
            self.direccion = 'izq'

        if self.caminando and self.direccion == 'der':
            imagenes.pantalla.blit(imagenes.zombi_der_caminando[fotograma],(self.posx,self.posy))
        if self.caminando and self.direccion == 'izq':
            imagenes.pantalla.blit(imagenes.zombi_izq_caminando[fotograma],(self.posx,self.posy))
    def hitbox(self):
        hitbox_enemigo = pygame.Rect(self.posx,self.posy,91,91)
        return hitbox_enemigo
    def desplazamiento(self):
        if jugador.jugador.coordx - 50 > self.posx:
            self.posx += self.velx
        elif jugador.jugador.coordx + 50 < self.posx:
            self.posx -= self.vely

        if jugador.jugador.coordy > self.posy:
            self.posy += self.vely
        elif jugador.jugador.coordy < self.posy:
            self.posy -= self.vely
    def ataque(self):
        fotograma_atacando = int(time.time()* 5) % 5

        if jugador.jugador.coordx > self.posx and jugador.jugador.coordx - self.posx <= 50 or jugador.jugador.coordx < self.posx and self.posx - jugador.jugador.coordx <= 50:
            self.atacando = True
            self.caminando = False
        else:
            self.atacando = False
            self.caminando = True

        if self.atacando and self.direccion == 'der':
            
            imagenes.pantalla.blit(imagenes.zombi_der_atacando[fotograma_atacando],(self.posx,self.posy))
        elif self.atacando and self.direccion == 'izq':
            imagenes.pantalla.blit(imagenes.zombi_izq_atacando[fotograma_atacando],(self.posx,self.posy))
    
zombi = Enemigo(posx=400,posy=250,vel=1,salud=5)
grupo_enemigos.append(zombi)