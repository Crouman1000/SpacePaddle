
import pygame

pygame.mixer.init()
menu_sound = pygame.mixer.Sound("pong/assets/sounds/gameMenu.mp3")
gameplay_sound = pygame.mixer.Sound("pong/assets/sounds/gameplay.mp3")
paddleHit_sound = pygame.mixer.Sound("pong/assets/sounds/paddle_hit.mp3")
YwallHit_sound = pygame.mixer.Sound("pong/assets/sounds/yWall_hit.mp3")
victory_sound = pygame.mixer.Sound("pong/assets/sounds/victory.mp3")
