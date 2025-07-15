import pygame
import game_constants as const
import image
import PygameUtils as pu
import sound
import settings

class Menu():

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.menu_surface = pygame.display.set_mode((const.GAME_SURFACE_WIDTH, const.GAME_SURFACE_HEIGHT))
        self.background_surface = pygame.transform.scale(image.background_surface,(const.GAME_SURFACE_WIDTH,const.GAME_SURFACE_HEIGHT))
        self.music_checkbox = Checkbox_overriden("red", 100, 100, 50,50, outline=0,check=settings.enableMusic, text="MUSIC")

    def _run_options(self, p_gameState: const.GameState) -> const.GameState:

        gameState = p_gameState
        self.running = True
 
        self.menu_surface.blit(self.background_surface,(0,0))
        
        while self.running:

            ### Wipe away last frames
            self.menu_surface.blit(self.background_surface,(0,0))

            # Poll for events
            for event in pygame.event.get():
                #print(f"event: {event}")
                if event.type == pygame.QUIT:
                    self.running = False
                    gameState = const.GameState.Off
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        gameState = const.GameState.MainMenu
                elif event.type == pygame.MOUSEBUTTONDOWN:   
                    mouseClickedCoords_tuple = pygame.mouse.get_pos()
                    if self.music_checkbox.isOver(mouseClickedCoords_tuple):
                        self.music_checkbox.convert()
                        if self.music_checkbox.isChecked():
                            sound.enableMusic()
                            sound.playMusic(const.MusicChoice.gameMenu)
                        else:
                            sound.disableMusic()

            self.music_checkbox._draw(self.menu_surface)
            pygame.display.flip()

            # FPS
            self.clock.tick(120)  

        return gameState


class Checkbox_overriden(pu.checkbox):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    #@override
    def _draw(self, win):

        but = pu.button(self.color, self.x, self.y, self.width, self.height, outline=self.outline)
        but.draw(win)

        if self.text != "":
            text = self.font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x + self.width+self.textGap, self.y + (self.height/2 - text.get_height()/2)))

        if self.check:
            pygame.draw.line(win, (255, 255, 255), (self.x, self.y), (self.x + self.width - self.outline, self.y + self.height - self.outline),3)
            pygame.draw.line(win, (255, 255, 255), (self.x - self.outline + self.width, self.y), (self.x, self.y + self.height - self.outline),3)

