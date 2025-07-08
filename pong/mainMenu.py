import pygame
import game_constants as const
import image
import sound

def run_mainMenu() -> const.GameState:

    # INITIALIZE PYGAME
    
    gameState = const.GameState.Off
    sound.menu_sound.play(-1,0,500)
    
    clock = pygame.time.Clock()

    buttonText_Font = pygame.font.SysFont("Bank Gothic",50,False,False)

    menu_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
    image.background_surface = image.background_surface.convert()
    image.background_surface = pygame.transform.scale(image.background_surface,(const.GAME_SURFACE_WIDTH,const.GAME_SURFACE_HEIGHT))
    menu_surface.blit(image.background_surface,(0,0))


    singlePlayer_Rect = pygame.draw.rect(menu_surface,"gray",
                    (const.SINGLEPLAYER_BUTTON_COORDS[0],
                    const.SINGLEPLAYER_BUTTON_COORDS[1],
                    const.MENU_BUTTON_SIZE[0],
                    const.MENU_BUTTON_SIZE[1]),
                    border_radius = const.MENU_BUTTON_BORDER_RAD)
    
    singlePlayerText_surface = buttonText_Font.render("SINGLE PLAYER",False,(0,0,0))
    menu_surface.blit(singlePlayerText_surface,
                    (singlePlayer_Rect.centerx - singlePlayerText_surface.get_width()/2,
                    singlePlayer_Rect.centery - singlePlayerText_surface.get_height()/2))

    
    multiPlayer_Rect = pygame.draw.rect(menu_surface,"gray",
                    (const.MULTIPLAYER_BUTTON_COORDS[0],
                    const.MULTIPLAYER_BUTTON_COORDS[1],
                    const.MENU_BUTTON_SIZE[0],
                    const.MENU_BUTTON_SIZE[1]),
                    border_radius = const.MENU_BUTTON_BORDER_RAD)
    multiPlayerText_surface = buttonText_Font.render("MULTIPLAYER",False,(0,0,0))
    menu_surface.blit(multiPlayerText_surface,
                    (multiPlayer_Rect.centerx - multiPlayerText_surface.get_width()/2,
                    multiPlayer_Rect.centery - multiPlayerText_surface.get_height()/2))

    options_Rect = pygame.draw.rect(menu_surface,"gray",
                    (const.OPTIONS_BUTTON_COORDS[0],
                    const.OPTIONS_BUTTON_COORDS[1],
                    const.MENU_BUTTON_SIZE[0],
                    const.MENU_BUTTON_SIZE[1]),
                    border_radius = const.MENU_BUTTON_BORDER_RAD)
    optionText_surface = buttonText_Font.render("OPTIONS",False,(0,0,0))
    menu_surface.blit(optionText_surface,
                    (options_Rect.centerx - optionText_surface.get_width()/2,
                    options_Rect.centery - optionText_surface.get_height()/2))
    
    running = True
    while running:
        # Poll for events
        for event in pygame.event.get():
            #print(f"event: {event}")
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseClickedCoords_tuple = pygame.mouse.get_pos()

                if multiPlayer_Rect.collidepoint(mouseClickedCoords_tuple[0],mouseClickedCoords_tuple[1]):
                    running = False
                    gameState = const.GameState.Multiplayer
                    sound.menu_sound.stop()
                    
        
       

        #menu_surface.fill("black")

        pygame.display.flip()

        clock.tick(120)  # limits FPS



    return gameState