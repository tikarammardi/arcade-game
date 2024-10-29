import pygame
from app import settings

class Player:
    def __init__(self, x, y):
        # Load and resize the player image
        self.image = pygame.image.load(settings.IMAGE_PLAYER).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.PLAYER_WIDTH, settings.PLAYER_HEIGHT))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center=(x, y))
        self.shoot_delay = settings.NORMAL_SHOOT_DELAY

    def move(self, dx):
        self.rect.x += dx * settings.PLAYER_SPEED
        self.rect.x = max(0, min(self.rect.x, settings.SCREEN_WIDTH - self.rect.width))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
