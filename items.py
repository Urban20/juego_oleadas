import imagenes,jugador,pygame,camara,random,time
botiquines = []
item_buff_lista = []
num_boti = 4

id_botiquin = 1
id_item_buff = 2
pygame.mixer.init()
item_sonido = pygame.mixer.Sound('elementos/sonidos/items.wav')
class Item():
    def __init__(self,posx,posy,imagen,id_item,sonido):
        super().__init__()
        self.posx= posx
        self.posy= posy
        self.imagen= imagen
        self.largo,self.altura = self.imagen.get_size()
        self.consumido = False
        self.activo = False
        self.rect = None
        self.tiempo2 = time.time()
        self.tiempo1 = None
        self.azar = None
        self.id= id_item
        self.sonido = sonido
    def spawn(self,chance):
        self.tiempo1 = time.time()
        if self.tiempo1 - self.tiempo2 >= 60:
            self.azar = random.choice(chance)
            if self.azar == self.id:
                self.activo = True
            self.tiempo2 = self.tiempo1
        if self.activo:
            imagenes.pantalla.blit(self.imagen,(self.posx,self.posy))
        


    def consumir(self):
        self.rect = pygame.Rect(self.posx,self.posy,self.largo,self.altura)
        if jugador.jugador.hitbox().colliderect(self.rect) and self.activo:
            self.consumido = True
            self.activo = False
        else:
            self.consumido = False
        
        if self.consumido:
            pygame.mixer.Channel(1).play(self.sonido)

        return self.consumido
            

class Botiquin(Item):
    def __init__(self,posx,posy,imagen,id_item,sonido):
        super().__init__(posx,posy,imagen,id_item,sonido)
    def curar(self):
        if self.consumido:
            jugador.jugador.salud = jugador.jugador_vida


class Item_buff(Item):
    def __init__(self,posx,posy,imagen,id_item,sonido):
        super().__init__(posx,posy,imagen,id_item,sonido)
        self.activado = False
        self.buffo_vel = 3.3
        self.buffo_daño = 25
        
  
    def buff(self):
        
        if self.consumido:
            self.activado = True
            
        if self.activado:
            
            jugador.jugador.velx = self.buffo_vel
            jugador.jugador.vely = self.buffo_vel
            camara.camara.vely = self.buffo_vel
            camara.camara.velx = self.buffo_vel
            jugador.jugador.buffeado = True
        

def item_spawn():
    if not botiquines and not item_buff_lista:
        for x in range(num_boti):
            posx= random.randint(20, imagenes.resolx)
            posy = random.randint(20,imagenes.resoly)
            botiquin = Botiquin(posx= posx,posy=posy,imagen=imagenes.botiquin,id_item=id_botiquin,sonido=item_sonido)

            botiquines.append(botiquin)
            camara.camara_contenedor.append(botiquin)
        item_buff = Item_buff(posx= posx,posy=posy,imagen=imagenes.item_vel,id_item=id_item_buff,sonido= item_sonido)
        item_buff_lista.append(item_buff)
        camara.camara_contenedor.append(item_buff)


botiquin_chance = [id_botiquin,0,0,0,0]
buffer_item_chance = [id_item_buff,0,0,0,0,0,0,0,0,0]



        