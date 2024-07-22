import pygame,time,imagenes


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.coordx = imagenes.resolx / 2
        self.coordy = imagenes.resoly / 2
        self.velx = 5
        self.vely = 5
        self.direccion = 'der'
        self.quieto = True
        self.disparando = False
        self.salud = 90
    def barra_salud(self):
        #barra roja
        pygame.draw.rect(imagenes.pantalla,imagenes.rojo,(self.coordx,self.coordy - 10,90,5))
        #barra verde
        pygame.draw.rect(imagenes.pantalla,imagenes.verde,(self.coordx,self.coordy - 10,self.salud,5))

    def hitbox(self):
        hitbox= pygame.Rect(self.coordx,self.coordy,75,91)
        return hitbox

    def dibujo(self):
        fotogramas= int(time.time()*5) % 7
        if self.direccion == 'der' and not self.quieto and not self.disparando:
            imagenes.pantalla.blit(imagenes.jugador_der[fotogramas],(self.coordx,self.coordy))
        elif self.direccion == 'izq' and not self.quieto and not self.disparando:
            imagenes.pantalla.blit(imagenes.jugador_izq[fotogramas],(self.coordx,self.coordy))
            
    def teclas(self,teclado):
        fotograma_disparo= int(time.time()* 10) % 4
        if teclado[pygame.K_a] and not self.disparando:
            self.coordx -= self.velx
            self.direccion = 'izq'
            self.quieto = False
        elif teclado[pygame.K_d] and not self.disparando:
            self.coordx += self.velx
            self.direccion = 'der'
            self.quieto = False
        elif teclado[pygame.K_s] and not self.disparando:
            self.coordy += self.vely
            self.quieto = False
        elif teclado[pygame.K_w] and not self.disparando:
            self.coordy -= self.vely
            self.quieto = False
      
        else:
            self.quieto = True
            self.corriendo = False
        #estado quieto---------------------------------------------------
        if self.quieto and self.direccion == 'der':
            fotogramas= int(time.time()*5) % 7
            imagenes.pantalla.blit(imagenes.jugador_quieto[fotogramas],(self.coordx,self.coordy))
        elif self.quieto and self.direccion == 'izq':
            fotogramas= int(time.time()*5) % 7
            imagenes.pantalla.blit(imagenes.jugador_quieto_izq[fotogramas],(self.coordx,self.coordy))
        #disparo------------------------------------------------------------
        if self.disparando and self.direccion == 'der':
            
            imagenes.pantalla.blit(imagenes.jugador_disparo[fotograma_disparo],(self.coordx,self.coordy))
        elif self.disparando and self.direccion == 'izq':
            
            imagenes.pantalla.blit(imagenes.jugador_disparo_izq[fotograma_disparo],(self.coordx,self.coordy))
        


    def disparar(self,teclas):
        
        if teclas[pygame.K_e]:
            self.disparando = True
            self.quieto = False
            
           
            bala1= Bala(self.direccion,self.coordx + 78,self.coordy + 12)
            imagenes.bala_jugador.append(bala1)
              
        else:
            self.disparando = False
            
        
        
jugador = Jugador()

class Bala(pygame.sprite.Sprite):
    def __init__(self,direccion,posx,posy):
        
        self.imagen = imagenes.bala
        self.rect= self.imagen.get_rect()
        self.posx = posx
        self.posy = posy
        self.direccion= direccion
        self.velx = 100

    def disparo(self):
        if self.direccion == 'der':
            imagenes.pantalla.blit(imagenes.bala,(self.posx,self.posy))
            self.posx += self.velx
        elif self.direccion == 'izq':
            imagenes.pantalla.blit(imagenes.bala_izq,(self.posx-85,self.posy))
            self.posx -= self.velx

