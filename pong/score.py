import pygame
import game_constants as const

class ScoreBoard():
    def __init__(self):
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.score_font = pygame.font.SysFont("Arial",30,True,False)

    def increaseScore(self,p_player:const.Player) -> None:
        match p_player:
            case const.Player.P1:
                print("P1 Scored!")
                self.scoreP1 += 1
            case const.Player.P2:
                print("P2 Scored!")
                self.scoreP2 += 1

    def render(self,p_canvas: pygame.Surface,p_canvasWidth: int,p_canvasHeight: int) -> None:
        score_surface = self.score_font.render(f"SCORE: P1 {self.scoreP1} | P2 {self.scoreP2}",0,(255,255,255))
        p_canvas.blit(score_surface,(p_canvasWidth/2 - score_surface.get_width()/2,p_canvasHeight/12))
        


