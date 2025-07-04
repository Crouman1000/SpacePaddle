import pygame
import game_constants as const
from typing import Hashable, Iterable, Union, Literal, Tuple

colorType = Union[
    Tuple[int,int,int],
    Tuple[int,int,int,int],
    str,
    pygame.Color
]

class GameText():

    def __init__(self,
                 p_fontName: Union[str, bytes, Iterable[Union[str, bytes]], None],
                 p_fontSize: int,          
                 p_isFontBold: bool = False,
                 p_isFontItalic: bool = False,
                 ):
        
        self.font = pygame.font.SysFont(p_fontName,p_fontSize,p_isFontBold,p_isFontItalic)
        self.surface = None
        self.message = None
        self.coordXY = None

    def render(self,
               p_text: str | bytes | None,
               p_antialias: bool | Literal[0, 1],
               p_color: colorType  = (255,255,255),
               p_background: colorType | None = None) -> None:
         
         self.surface = self.font.render(p_text,p_antialias,p_color,p_background)
        
        
class ScoreBoard(GameText):

    def __init__(self,p_name,p_size,p_bold,p_italic):
        super().__init__(p_name,p_size,p_bold,p_italic)
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.message = f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}"

    def increaseScore(self,p_player:const.Player) -> None:
        match p_player:
            case const.Player.P1:
                print("P1 Scored!")
                self.scoreP1 += 1
                
            case const.Player.P2:
                print("P2 Scored!")
                self.scoreP2 += 1
                

    def showScore(self,p_canvas: pygame.Surface) -> None:
        self.message = f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}"
        self.render(self.message,0,(255,255,255))
        self.coordXY = ((p_canvas.get_width() - self.surface.get_width())/2,p_canvas.get_height()/12)
        p_canvas.blit(self.surface,self.coordXY)
   
        

class StartText(GameText):

    def __init__(self,p_name,p_size,p_bold,p_italic):
        super().__init__(p_name,p_size,p_bold,p_italic)
        self.message = f"PRESS ANY KEY TO START"

    def showMessage(self,p_canvas: pygame.Surface) -> None:
        
        self.render(self.message,0,(255,255,255))
        self.coordXY = ((p_canvas.get_width() - self.surface.get_width())/2,4*p_canvas.get_height()/10)
        p_canvas.blit(self.surface,self.coordXY)



