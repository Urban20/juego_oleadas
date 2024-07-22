import pygame,jugador,imagenes,time,enemigos

pygame.init()

reloj = pygame.time.Clock()
resolx = 900
resoly= 500

tiempo_juego = time.time()
tiempo_juego2= time.time()


juego = True
while juego:
    cooldown_disparo = time.time()
    eventos = pygame.event.get()
    teclado = pygame.key.get_pressed()
    for evento in eventos:
            if evento.type == pygame.QUIT:
                juego = False
  
    imagenes.pantalla.fill(imagenes.verde_militar)
#jugador------------------------------------------------------------
    jugador.jugador.dibujo()
    jugador.jugador.barra_salud()
    jugador.jugador.hitbox()
    jugador.jugador.teclas(teclado)
    if cooldown_disparo - tiempo_juego >= 0.25:
        jugador.jugador.disparar(teclado)
        tiempo_juego = cooldown_disparo

    for bala in imagenes.bala_jugador:
        
        bala.disparo()
        if bala.posx <= 0 or bala.posx >= imagenes.resolx:
            imagenes.bala_jugador.remove(bala)
#jugador------------------------------------------------------------
    

#enemigo----------------------
    
#enemigo----------------------

    for zombi in enemigos.grupo_enemigos:
        enemigos.zombi.dibujo()
        enemigos.zombi.hitbox()
        enemigos.zombi.desplazamiento()
        enemigos.zombi.ataque()
   
        cooldown_daño = time.time() * 1.5
    #colision enemigo-jugador
        if jugador.jugador.hitbox().colliderect(zombi.hitbox()) and cooldown_daño - tiempo_juego2 > 1:
            
            jugador.jugador.salud -= 5
            tiempo_juego2 = cooldown_daño

   
    pygame.display.flip()

    
    reloj.tick(60)