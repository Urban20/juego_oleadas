import pygame,jugador,imagenes,time,random,camara


contador_hordas = 0
num_horda = 3
delay_hordas = 2.6
incremento_horda = 1
grupo_enemigos = []
tiempo_horda = time.time()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,posx,posy,vel,salud,img_caminando,img_caminando_izq,img_atacando,img_atacando_izq,img_muerte,img_muerte_izq):
        super().__init__()
        self.posx = posx
        self.posy = posy
        #estados
        self.direccion = None
        self.atacando= False
        self.caminando = True
        self.muerto = False
        self.quitar = False

        self.velx = vel
        self.vely = vel

        self.salud = salud
        self.fotograma_muerte= 0
        self.tiempo_muerte = time.time()
        #imagenes----------------------
        #CAMINANDO
        self.imagen_caminando= img_caminando
        self.imagen_caminando_izq= img_caminando_izq
        #ATACANDO
        self.imagen_atacando = img_atacando
        self.imagen_atacando_izq = img_atacando_izq
        #MUERTE
        self.imagen_muerte = img_muerte
        self.imagen_muerte_izq = img_muerte_izq
        self.tiempo_contador_zombi= time.time()

        #imagenes----------------------
    def dibujo(self):
        if not self.muerto and self.posx > -20 and self.posx < imagenes.resolx and self.posy > 0 and self.posy < imagenes.resoly:
            fotograma= int(time.time()* 4) % 8
            if jugador.jugador.coordx > self.posx:
                self.direccion = 'der'
            else:
                self.direccion = 'izq'

            if self.caminando and self.direccion == 'der':
                imagenes.pantalla.blit(self.imagen_caminando[fotograma],(self.posx,self.posy))
            if self.caminando and self.direccion == 'izq':
                imagenes.pantalla.blit(self.imagen_caminando_izq[fotograma],(self.posx,self.posy))
    def hitbox(self):
        
        hitbox_enemigo = pygame.Rect(self.posx,self.posy,91,91)
        return hitbox_enemigo
    def desplazamiento(self):
        if not self.muerto:
            if jugador.jugador.coordx - 50 > self.posx:
                self.posx += self.velx
            elif jugador.jugador.coordx + 50 < self.posx:
                self.posx -= self.vely

            if jugador.jugador.coordy > self.posy:
                self.posy += self.vely
            elif jugador.jugador.coordy < self.posy:
                self.posy -= self.vely
    def ataque(self):
        if not self.muerto:
            fotograma_atacando = int(time.time()* 5) % 5
            
            if jugador.jugador.coordx > self.posx and jugador.jugador.coordx - self.posx <= 50 or jugador.jugador.coordx < self.posx and self.posx - jugador.jugador.coordx <= 50:
                if self.posy > jugador.jugador.coordy and self.posy - jugador.jugador.coordy <= 50 or jugador.jugador.coordy > self.posy and jugador.jugador.coordy - self.posy <= 50:
                    self.atacando = True
                    self.caminando = False
            else:
                self.atacando = False
                self.caminando = True

            if self.atacando and self.direccion == 'der':
                
                imagenes.pantalla.blit(self.imagen_atacando[fotograma_atacando],(self.posx,self.posy))
            elif self.atacando and self.direccion == 'izq':
                imagenes.pantalla.blit(self.imagen_atacando_izq[fotograma_atacando],(self.posx,self.posy))
    def muerte(self):
        
        if self.muerto and self.direccion == 'der':
            imagenes.pantalla.blit(self.imagen_muerte[self.fotograma_muerte],(self.posx,self.posy))
            if time.time() - self.tiempo_muerte > 0.15:
                self.fotograma_muerte += 1
                self.tiempo_muerte = time.time()
            if self.fotograma_muerte >= 4:
                self.fotograma_muerte = 4
                self.quitar = True
        elif self.muerto and self.direccion == 'izq':
            imagenes.pantalla.blit(self.imagen_muerte_izq[self.fotograma_muerte],(self.posx,self.posy))
            if time.time() - self.tiempo_muerte > 0.15:
                self.fotograma_muerte += 1
                self.tiempo_muerte = time.time()
            if self.fotograma_muerte > 4:
                self.fotograma_muerte = 4
                self.quitar = True
        

def hordas(num,lista_enemigos):

    global incremento_horda,tiempo_horda
   
    if time.time() - tiempo_horda >= delay_hordas:
        
        num = num * incremento_horda
        
        if not lista_enemigos:
            
            
            incremento_horda += 1
            for x in range(num):
                posy= random.randint(0,imagenes.resoly)
                posx = random.choice([0,imagenes.resolx])
                vel= random.uniform(1.0,2.0)
                salud=random.randint(70,90)
                zombi= Enemigo(posx= posx,posy=posy,vel=vel,salud=salud,img_caminando=imagenes.zombi_der_caminando,img_caminando_izq=imagenes.zombi_izq_caminando,img_atacando=imagenes.zombi_der_atacando,img_atacando_izq=imagenes.zombi_izq_atacando,img_muerte=imagenes.muerte_enemigo,img_muerte_izq=imagenes.muerte_enemigo_izq)
                grupo_enemigos.append(zombi)
                camara.camara_contenedor.append(zombi)
           
        tiempo_horda = time.time()
        