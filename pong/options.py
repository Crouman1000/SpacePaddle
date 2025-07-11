import pygame
import game_constants as const
import image
import PygameUtils as pu

def run_options() -> const.GameState:

    gameState = const.GameState.Options
    
    clock = pygame.time.Clock()


    buttonText_Font = pygame.font.SysFont("Bank Gothic",50,False,False)

    menu_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
    image.background_surface = image.background_surface.convert()
    image.background_surface = pygame.transform.scale(image.background_surface,(const.GAME_SURFACE_WIDTH,const.GAME_SURFACE_HEIGHT))
    menu_surface.blit(image.background_surface,(0,0))


    checkb = Checkbox_overriden("red", 100, 100, 50,50, outline=0, text="MUSIC")
    
    running = True
    while running:

        ### Wipe away last frames
        menu_surface.blit(image.background_surface,(0,0))

        # Poll for events
        for event in pygame.event.get():
            #print(f"event: {event}")
            if event.type == pygame.QUIT:
                running = False
                gameState = const.GameState.Off
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    gameState = const.GameState.MainMenu
            elif event.type == pygame.MOUSEBUTTONDOWN:   
                mouseClickedCoords_tuple = pygame.mouse.get_pos()
                if checkb.isOver(mouseClickedCoords_tuple):
                    checkb.convert()
                    
                #    running = False
                #    gameState = const.GameState.Multiplayer
                #    sound.menu_sound.stop()
                
        checkb.draw(menu_surface)
        pygame.display.flip()

        clock.tick(120)  # limits FPS



    return gameState

class Checkbox_overriden(pu.checkbox):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def draw(self, win):

        but = pu.button(self.color, self.x, self.y, self.width, self.height, outline=self.outline)
        but.draw(win)

        if self.text != "":
            text = self.font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + self.width+self.textGap, self.y + (self.height/2 - text.get_height()/2)))

        if self.check:
            pygame.draw.line(win, (255, 255, 255), (self.x, self.y), (self.x + self.width - self.outline, self.y + self.height - self.outline),3)
            pygame.draw.line(win, (255, 255, 255), (self.x - self.outline + self.width, self.y), (self.x, self.y + self.height - self.outline),3)
