from typing import Iterable, Union, Literal, Tuple
import pygame
import audio
import game_constants as const



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
        self.coordXY = None
        

    def render_(self,
               p_text: str | bytes | None,
               p_antialias: bool | Literal[0, 1],
               p_color: colorType  = (255,255,255),
               p_background: colorType | None = None) -> pygame.Surface:
         
        return self.font.render(p_text,p_antialias,p_color,p_background)
        
        
class ScoreBoard(GameText):

    def __init__(self,p_name,p_size,p_bold,p_italic):
        super().__init__(p_name,p_size,p_bold,p_italic)
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.lastWinner = None
        self.gameOver = False

        self.scoreSurface = self.render_(f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}",0,(255,255,255))
        self.startSurface = self.render_(f"PRESS SPACEBAR TO START",0,(255,255,255))
        self.whoScoredSurface = None
        self.winnerSurface = None
       

    def increaseScore(self,p_player:const.Player) -> None:
        self.lastWinner = p_player.value
        match p_player:
            case const.Player.P1:                
                self.scoreP1 += 1
                
            case const.Player.P2:
                self.scoreP2 += 1
        if self.scoreP1 == const.GAME_MAXSCORE or self.scoreP2 == const.GAME_MAXSCORE:
            self.gameOver = True

        
        self.scoreSurface = self.render_(f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}",0,(255,255,255))
            

    def showScore(self,p_canvas: pygame.Surface) -> None:
    
        self.coordXY = ((p_canvas.get_width() - self.scoreSurface.get_width())/2,p_canvas.get_height()/12)
        p_canvas.blit(self.scoreSurface,self.coordXY)

    def showWinner(self,p_canvas: pygame.Surface) -> None:         

        if self.lastWinner:

            messageColor_tuple = (255,0,0) if self.lastWinner == 1 else (0,255,0)

            if self.gameOver:

                audio.soundTools.playSound(const.SoundChoice.victory)     
                self.winnerSurface = self.render_(f"Player {self.lastWinner} HAS WON THE GAME!",0,messageColor_tuple)
                self.coordXY = ((p_canvas.get_width() - self.winnerSurface.get_width())/2,3*p_canvas.get_height()/10)
                p_canvas.blit(self.winnerSurface,self.coordXY)
                self.resetScore__()
                
            else:

                self.whoScoredSurface = self.render_(f"PLAYER {self.lastWinner} SCORED !",0,messageColor_tuple)
                self.coordXY = ((p_canvas.get_width() - self.whoScoredSurface.get_width())/2,3*p_canvas.get_height()/10)
                p_canvas.blit(self.whoScoredSurface,self.coordXY)
        
       
    def showStart(self,p_canvas: pygame.Surface) -> None:
        
        self.coordXY = ((p_canvas.get_width() - self.startSurface.get_width())/2,4*p_canvas.get_height()/10)
        p_canvas.blit(self.startSurface,self.coordXY)
    
    def resetScore__(self) -> None:
        self.lastWinner = None
        self.gameOver = False
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.scoreSurface = self.render_(f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}",0,(255,255,255))
        


