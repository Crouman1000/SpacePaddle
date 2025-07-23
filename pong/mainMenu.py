import pygame
import game_constants as const
import graphics
import audio

class Menu():

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.buttonText_Font = pygame.font.SysFont("Bank Gothic",50,False,False)
        self.menu_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
        self.background_surface = pygame.transform.scale(graphics.imageTools.images.get(const.imageChoice.backgroundMenu),
                                                         (const.GAME_SURFACE_WIDTH,const.GAME_SURFACE_HEIGHT))
        
        self.singlePlayer_Rect = pygame.Rect(const.SINGLEPLAYER_BUTTON_COORDS[0],
                                const.SINGLEPLAYER_BUTTON_COORDS[1],
                                const.MENU_BUTTON_SIZE[0],
                                const.MENU_BUTTON_SIZE[1])
        self.singlePlayerText_surface = self.buttonText_Font.render("SINGLE PLAYER",False,(0,0,0))

        self.multiPlayer_Rect = pygame.Rect(const.MULTIPLAYER_BUTTON_COORDS[0],
                        const.MULTIPLAYER_BUTTON_COORDS[1],
                        const.MENU_BUTTON_SIZE[0],
                        const.MENU_BUTTON_SIZE[1])
        self.multiPlayerText_surface = self.buttonText_Font.render("MULTIPLAYER",False,(0,0,0))
        
        self.options_Rect = pygame.Rect(const.OPTIONS_BUTTON_COORDS[0],
                        const.OPTIONS_BUTTON_COORDS[1],
                        const.MENU_BUTTON_SIZE[0],
                        const.MENU_BUTTON_SIZE[1])                    
        self.optionText_surface = self.buttonText_Font.render("OPTIONS",False,(0,0,0))
        
    def run_mainMenu(self,p_gameState: const.GameState) -> const.GameState:
        
        gameState = p_gameState
        self.running = True    
        
        audio.soundTools.playMusic(const.MusicChoice.gameMenu)

        self.menu_surface.blit(self.background_surface,(0,0))
 
        pygame.draw.rect(self.menu_surface,"gray",self.singlePlayer_Rect,border_radius= const.MENU_BUTTON_BORDER_RAD)   
        self.menu_surface.blit(self.singlePlayerText_surface,
                        (self.singlePlayer_Rect.centerx - self.singlePlayerText_surface.get_width()/2,
                        self.singlePlayer_Rect.centery - self.singlePlayerText_surface.get_height()/2))
        
        pygame.draw.rect(self.menu_surface,"gray",self.multiPlayer_Rect,border_radius= const.MENU_BUTTON_BORDER_RAD)
        self.menu_surface.blit(self.multiPlayerText_surface,
                        (self.multiPlayer_Rect.centerx - self.multiPlayerText_surface.get_width()/2,
                        self.multiPlayer_Rect.centery - self.multiPlayerText_surface.get_height()/2))

        pygame.draw.rect(self.menu_surface,"gray",self.options_Rect,border_radius= const.MENU_BUTTON_BORDER_RAD)    
        self.menu_surface.blit(self.optionText_surface,
                        (self.options_Rect.centerx - self.optionText_surface.get_width()/2,
                        self.options_Rect.centery - self.optionText_surface.get_height()/2))       

        while self.running:
            # Poll for events
            for event in pygame.event.get():
                #print(f"event: {event}")
                if event.type == pygame.QUIT:
                    self.running = False
                    gameState = const.GameState.Off
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseClickedCoords_tuple = pygame.mouse.get_pos()

                    if self.singlePlayer_Rect.collidepoint(mouseClickedCoords_tuple[0],mouseClickedCoords_tuple[1]):
                        self.running = False
                        gameState = const.GameState.Singleplayer
                                         
                    elif self.multiPlayer_Rect.collidepoint(mouseClickedCoords_tuple[0],mouseClickedCoords_tuple[1]):
                        self.running = False
                        gameState = const.GameState.Multiplayer               
                    
                    elif self.options_Rect.collidepoint(mouseClickedCoords_tuple[0],mouseClickedCoords_tuple[1]):  
                        self.running = False
                        gameState = const.GameState.Options
                        
            #menu_surface.fill("black")

            pygame.display.flip()

            self.clock.tick(120)  # limits FPS

        return gameState