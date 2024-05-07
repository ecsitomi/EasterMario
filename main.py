if __name__ == "__main__": #chatgpt szerint ez hasznos, hogy jól fussanak le a fájlok
    import pygame
    from settings import * #settings.py fájlból behúz mindent
    from level import Level
    from sounds import dead

    pygame.init() #inicializálja magát a pygame
    pygame.mixer.init() #hang inicializálása
    screen=pygame.display.set_mode((WIDTH,HEIGHT)) #meghatározza az ablakot
    pygame.display.set_caption('HEJ - Easter Mario') #főcím
    clock=pygame.time. Clock() #időzítő

    #háttérkép
    background_image = pygame.image.load(BG_IMAGE).convert_alpha()
    original_width, original_height = background_image.get_size()
    new_width = WIDTH
    new_height = int(original_height * (WIDTH / original_width))
    bg_surf = pygame.transform.scale(background_image, (new_width, new_height))
    #bg_surf=pygame.image.load(BG_IMAGE).convert_alpha()
    bg_rect=bg_surf.get_rect(bottomleft=(0,HEIGHT))

    #szint
    level=Level(level_map[0]['data'],screen)#hozz létre egy szint objektumot a levelmap(ami most settingsben van) alapján a screenre
                                #levelmap = Level classban ez a layout

    start=True #legyen e kezdőképernyő
    running=True #futtatás
    while running:
        for event in pygame.event.get(): #események loop
            if event.type==pygame.QUIT: #kilépés
                running=False

        screen.fill(BG_COLOR) #háttérszín
        screen.blit(bg_surf,bg_rect) #háttérkép
        #keys=pygame.key.get_pressed() #lehet lenyomni billentyűt

        if start: #kezdőképernyő
            dead.play()
            font=level.setup_font(72) #főcím betűtípusa
            text=font.render('Easter Mario', True, VIOLET) #szövege
            text_rect=text.get_rect(center=(WIDTH/2,HEIGHT/2)) #helye
            screen.blit(text,text_rect) #megjelenítése
            pygame.display.update() #kép frissítése
            pygame.time.delay(2000) #várakozás 2 ms
            start=False #főcím vége
        else: #játék indítása
            level.run() #szint megrajzolása a képernyőn és az azon történő események futtatása

        pygame.display.update() #frissítés
        clock.tick(FPS) #fps alapján megy a frissítése

    pygame.quit() #kilépés

