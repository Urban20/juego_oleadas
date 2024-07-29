import pygame,imagenes

class Boton():
    def __init__(self,posx,posy,largo,alto,color_boton,color_txt,texto,tamaño_texto):
        self.posx = posx
        self.posy = posy
        self.largo = largo
        self.alto = alto
        self.color_texto = color_txt
        self.texto= texto 
        self.tamaño_texto = tamaño_texto
        self.presionado = False
        self.color = color_boton
        self.fuente_texto = None
        self.boton = None
    def crear(self):
        self.fuente_texto = pygame.font.SysFont('Gill Sans',self.tamaño_texto)
       
        self.boton= pygame.draw.rect(imagenes.pantalla,self.color,(self.posx,self.posy,self.largo,self.alto))
        imagenes.pantalla.blit(self.fuente_texto.render(self.texto,True,self.color_texto),(self.posx + 3,self.posy))
    def click(self):

        mouse= pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if self.boton.collidepoint(mouse) and evento.type == pygame.MOUSEBUTTONDOWN:
                self.presionado = True
                
            else: 
                self.presionado = False
        

class Mouse():
    def __init__(self,imagen):
        self.imagen= imagen
    def iniciar(self):
        mouse_pos=pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        imagenes.pantalla.blit(self.imagen,(mouse_pos))

mouse = Mouse(imagen=imagenes.mouse)

#pantalla de perdiste
reiniciar_boton= Boton(posx=(imagenes.resolx / 2) - 37.5,posy= imagenes.resoly - 50,largo=100,alto=20,color_boton=imagenes.negro,color_txt=imagenes.amarillo,texto='REINICIAR',tamaño_texto=20)
#pantalla de menu
salir_boton = Boton(posx=(imagenes.resolx / 2) - 37.5,posy= imagenes.resoly - 100,largo=60,alto=30,color_boton=imagenes.violeta,color_txt=imagenes.amarillo,texto='SALIR',tamaño_texto=20)
jugar_boton= Boton(posx=(imagenes.resolx / 2) - 37.5,posy= imagenes.resoly - 600,largo=66,alto=24,color_boton=imagenes.negro,color_txt=imagenes.rojo,texto='JUGAR',tamaño_texto= 20)