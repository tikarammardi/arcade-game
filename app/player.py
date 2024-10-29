import pygame
from app import settings

class Player:
    def __init__(self,x, y):
        self.rect = pygame.Rect(x, y, settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT)
        self.color = settings.PLAYER_COLOR
        self.shoot_delay = settings.NORMAL_SHOOT_DELAY

    def move(self, dx):
        self.rect.x += dx * settings.PLAYER_SPEED
        # Prevent player from moving off-screen
        min_x = min(self.rect.x, settings.SCREEN_WIDTH - settings.PLAYER_WIDTH)
        self.rect.x = max(0, min_x)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
