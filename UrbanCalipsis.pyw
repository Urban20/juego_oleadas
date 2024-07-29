import pygame,jugador,imagenes,time,enemigos,camara,items,hud

pygame.init()
#sonidos---------------------------------------------------
pygame.mixer.init()
musica= pygame.mixer.music.load('elementos/sonidos/musica.ogg')
pygame.mixer.music.play(-1)
viento= pygame.mixer.Sound('elementos/sonidos/wind1.wav')
#sonidos---------------------------------------------------
reloj = pygame.time.Clock()
#textos-----------------------------------------------
pygame.display.set_caption('UrbanCalipsis v1.0')
texto= pygame.font.SysFont('Gill Sans',20)
texto_perdiste= texto.render('JUEGO TERMINADO',True,imagenes.rojo)
tamaño_perdiste= texto_perdiste.get_size()
#textos-----------------------------------------------

tiempo_juego = time.time()
tiempo_juego2= time.time()
tiempo_zombi_muerte = time.time()


#estados
menu = 'menu'
jugando = 'jugando'
perdiste = 'perdiste'
pausa = 'pausa'
estado = menu


juego = True
if estado == jugando:
    viento.play()
while juego:

    
    if estado == menu:
        
        
        teclas = pygame.key.get_pressed()

        imagenes.pantalla.fill(imagenes.negro)
        imagenes.pantalla.blit(texto.render('sobrevivi la mayor cantidad de hordas posibles, en el mapa habrá items aleatorios que te ayudan a sobrevivir',True,imagenes.amarillo),(100,imagenes.resoly - 500))
        imagenes.pantalla.blit(texto.render('ESCAPE para salir',True,imagenes.amarillo),(100,imagenes.resoly-50))
        imagenes.pantalla.blit(texto.render('TECLAS: "w,a,s,d" para moverte, "E" para disparar',True,imagenes.amarillo),(100,imagenes.resoly-450))
        
        imagenes.pantalla.blit(imagenes.urban,(imagenes.resolx - imagenes.urban_tamaño[0],imagenes.resoly - imagenes.urban_tamaño[1]))
        hud.jugar_boton.crear()
        hud.jugar_boton.click()
        if hud.jugar_boton.presionado:
                estado = jugando
            
        elif teclas[pygame.K_ESCAPE]:
            juego = False
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego = False
        
            
        hud.mouse.iniciar()
        pygame.display.flip()
        

       
    #juego corriendo***********************************
    elif estado == jugando:
        if not pygame.mixer.Channel(0).get_busy():
            pygame.mixer.Channel(0).play(viento, loops=-1)

        pygame.mixer.music.pause()
        
        if not enemigos.grupo_enemigos and time.time() - tiempo_zombi_muerte > enemigos.delay_hordas - 0.25:
            enemigos.contador_hordas +=1
            print(enemigos.contador_hordas)
            tiempo_zombi_muerte = time.time()

        imagenes.pantalla.fill(imagenes.negro)
        camara.fondo.mostrar()
        
        cooldown_disparo = time.time()
        eventos = pygame.event.get()
        
        teclado = pygame.key.get_pressed()
        for evento in eventos:
                if evento.type == pygame.QUIT:
                    juego = False
        items.item_spawn()
        for item in items.botiquines:
            item.spawn(items.botiquin_chance)
            item.consumir()
            item.curar()
        
            if item.consumido:
                items.botiquines.remove(item)

        for item in items.item_buff_lista:
            item.spawn(items.buffer_item_chance)
            item.consumir()
            item.buff()
            if item.consumido:
                items.item_buff_lista.remove(item)
        if jugador.jugador.buffeado:
            imagenes.pantalla.blit(imagenes.img_bost,(jugador.jugador.coordx - 17,jugador.jugador.coordy - 10))
        
            
    #jugador------------------------------------------------------------
        jugador.jugador.dibujo()
        jugador.jugador.barra_salud(jugador.jugador_vida)
        jugador.jugador.hitbox()
        jugador.jugador.teclas(teclado)
        camara.camara.iniciar()
        if cooldown_disparo - tiempo_juego >= jugador.cooldown_disparo:
            jugador.jugador.disparar(teclado)
            
            tiempo_juego = cooldown_disparo
    #dsparo-jugador
        for bala in imagenes.bala_jugador:
            
            bala.disparo()
            if bala.posx <= 0 or bala.posx >= imagenes.resolx:
                imagenes.bala_jugador.remove(bala)
        #camara-jugador
        if not camara.fondo.mapa().colliderect(jugador.jugador.hitbox()) and jugador.jugador.direccion == 'izq':
            jugador.fuera_del_mapa = True
        elif not camara.fondo.mapa().colliderect(jugador.jugador.hitbox())  and jugador.jugador.direccion == 'der':
            jugador.fuera_del_mapa = True
        else:
            jugador.fuera_del_mapa = False
        
    #jugador------------------------------------------------------------
        
        
    #enemigo----------------------

    #enemigo----------------------
    #hordas
        
        for zombi in enemigos.grupo_enemigos:

            zombi.dibujo()
            zombi.hitbox()
            zombi.desplazamiento()
            zombi.ataque()
            zombi.muerte()
            if zombi.quitar:
                enemigos.grupo_enemigos.remove(zombi)
            
        #colision enemigo-jugador
            if jugador.jugador.hitbox().colliderect(zombi.hitbox()) and time.time() - tiempo_juego2 > 1 and not zombi.muerto:
                jugador.jugador.vel_default = jugador.vel_debuf
                
                jugador.jugador.salud -= 5
                tiempo_juego2 = time.time()
            if jugador.jugador.salud <= 0:
                estado = perdiste
            
            else:
                jugador.jugador.vel_default = jugador.vel_default
                
        #colision bala-enemigo
            for bala in imagenes.bala_jugador:
                if bala.hitbox().colliderect(zombi.hitbox()):
                    
                    zombi.salud -= bala.daño
                    
                    if zombi.salud <= 0:
                        zombi.muerto = True
                        
        #contador de hordas
        enemigos.hordas(enemigos.num_horda,enemigos.grupo_enemigos)
        hud.mouse.iniciar()


    elif estado == perdiste:

        teclas= pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            juego=False
        pygame.mixer.Channel(0).stop()
        items.botiquines.clear()
        items.item_buff_lista.clear()
     
        
        
        texto_num_horda = texto.render(f'llegaste a la horda: {enemigos.contador_hordas}',True,imagenes.blanco)
        tamaño_numhorda=texto_num_horda.get_size()  
        imagenes.pantalla.fill(imagenes.negro)
        imagenes.pantalla.blit(texto_perdiste,(imagenes.resolx / 2 - tamaño_perdiste[0] / 2,imagenes.resoly / 2))
        imagenes.pantalla.blit(texto_num_horda,(imagenes.resolx / 2 - tamaño_perdiste[0] / 2,imagenes.resoly / 2 + 100) )
        imagenes.pantalla.blit(texto.render('ESCAPE para salir',True,imagenes.amarillo),(100,imagenes.resoly-50))
        hud.reiniciar_boton.crear()
        hud.reiniciar_boton.click()
        hud.mouse.iniciar()
        
        if hud.reiniciar_boton.presionado:
            hud.reiniciar_boton.presionado = False
            enemigos.grupo_enemigos.clear()
            
            if jugador.jugador.buffeado:
                jugador.jugador.buffeado = False
            jugador.jugador.salud = jugador.jugador_vida
            jugador.jugador.coordx = jugador.jugador_spawnx
            jugador.jugador.coordy = jugador.jugador_spawny
            jugador.jugador.velx = jugador.vel_default
            jugador.jugador.vely = jugador.vel_default
            enemigos.contador_hordas = 0
            enemigos.incremento_horda = 1
            jugador.daño_jugador = 20

            
            estado = jugando
           
   

    pygame.display.flip()            
    reloj.tick(60)