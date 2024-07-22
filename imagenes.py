import pygame
import pygame.locals
#memoria jugador--------
jugador_der=[]
jugador_izq = []
jugador_quieto=[]
jugador_quieto_izq=[]
#combate jugador
jugador_disparo=[]
jugador_disparo_izq =[]
bala_jugador=[]
#memoria jugador--------


#memoria enemigo--------
zombi_der_caminando=[]
zombi_izq_caminando=[]
zombi_der_atacando= []
zombi_izq_atacando= []
#memoria jugador--------

enemigos_sprites = []


resolx = 900
resoly= 500

pantalla = pygame.display.set_mode((resolx,resoly))



#colores-----------------
verde_militar = (93,109,98)
salmon = (228, 127, 119)
lila= (163, 119, 228)
gris =(208,215,207)
blanco=(255,255,255)
rojo= (255,0,0)
verde= (0,255,0)
#colores-----------------

#JUGADOR-----------------------------------------------------------------
#jugador derecha
for x in range(1,8):
    jugador_img= pygame.image.load(f'jugador/mov/{x}.PNG')
    
    jugador_der.append(jugador_img)
    #jugador izquierda
    jugador_img_izq= pygame.transform.flip(jugador_img,True,False)
    jugador_izq.append(jugador_img_izq)

    #jugador quieto
    #derecha
    jugadorquieto= pygame.image.load(f'jugador/quieto/quieto{x}.PNG')
    jugadorquieto.set_colorkey(verde_militar)
    jugadorquieto_izq = pygame.transform.flip(jugadorquieto,True,False)
    jugador_quieto.append(jugadorquieto)
    jugador_quieto_izq.append(jugadorquieto_izq)

for x in range(1,5):
    disparo_jugador= pygame.image.load(f'jugador/disparo/disparo{x}.PNG')
    jugador_disparo.append(disparo_jugador)
    disparo_jugador_izq= pygame.transform.flip(disparo_jugador,True,False)
    jugador_disparo_izq.append(disparo_jugador_izq)
#JUGADOR-----------------------------------------------------------------

#balas------------------------------------------
bala= pygame.image.load('elementos/bala.jpg')
bala.set_colorkey(blanco)
bala_izq = pygame.transform.flip(bala,True,False)
bala_izq.set_colorkey(blanco)
#balas------------------------------------------


#zombi------------------------------------------------------------------------
#caminando
for x in range(1,9):
    caminando_der=pygame.image.load(f'enemigo/caminando/caminando{x}.PNG')
    caminando_der.set_colorkey(verde_militar)
    zombi_der_caminando.append(caminando_der)

    caminando_izq=pygame.transform.flip(caminando_der,True,False)
    caminando_izq.set_colorkey(verde_militar)
    zombi_izq_caminando.append(caminando_izq)

for x in range(1,6):
    zombi_atacando= pygame.image.load(f'enemigo/atacando/{x}.PNG')
    zombi_atacando.set_colorkey(verde_militar)
    zombi_der_atacando.append(zombi_atacando)

    zombi_atacando_izq= pygame.transform.flip(zombi_atacando,True,False)
    zombi_atacando_izq.set_colorkey(verde_militar)
    zombi_izq_atacando.append(zombi_atacando_izq)

#zombi------------------------------------------------------------------------