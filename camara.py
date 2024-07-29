import imagenes,jugador,pygame



camara_contenedor = []
class Fondo():
    def __init__(self,posx,posy):
        self.posx = posx
        self.posy = posy
        self.imagen= imagenes.fondo
        self.largo,self.ancho = self.imagen.get_size()
        
    def mostrar(self):
        imagenes.pantalla.blit(self.imagen,(self.posx,self.posy))
    def mapa(self):
        mapa= pygame.Rect(self.posx,self.posy,self.largo,self.ancho)
        return mapa

fondo = Fondo(posx=0,posy=0)
class Camara():
    def __init__(self,vel):
        self.velx = vel
        self.vely = vel
        
        self.limite_der_x = imagenes.resolx - 100
        self.limite_izq_x = 100
        self.limite_arriba = 100
        self.limite_abajo = imagenes.resoly - 200


    def iniciar(self):
        
        if not jugador.fuera_del_mapa:
            #camara en el eje x
            if jugador.jugador.coordx >= self.limite_der_x and jugador.jugador.caminando:
                jugador.jugador.coordx = self.limite_der_x
                fondo.posx -= self.velx
                for elementos in camara_contenedor:
                    elementos.posx -= self.velx
            elif jugador.jugador.coordx <= self.limite_izq_x and jugador.jugador.caminando:
                jugador.jugador.coordx = self.limite_izq_x
                fondo.posx += self.velx

                for elementos in camara_contenedor:
                    elementos.posx += self.velx
            #camara en el eje y
            if jugador.jugador.coordy <= self.limite_arriba and jugador.jugador.caminando:
                jugador.jugador.coordy = self.limite_arriba
                fondo.posy += self.vely
                for elementos in camara_contenedor:
                    elementos.posy += self.velx
            elif jugador.jugador.coordy >= self.limite_abajo and jugador.jugador.caminando:
                jugador.jugador.coordy = self.limite_abajo
                fondo.posy -= self.vely
                for elementos in camara_contenedor:
                    elementos.posy -= self.velx


camara = Camara(vel=jugador.vel_default)