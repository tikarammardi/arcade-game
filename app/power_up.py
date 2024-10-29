import pygame
import random
from app import settings

class PowerUp:
    def __init__(self, type, x=None, y=None):
        self.type = type
        # Load and resize the power-up image
        self.image = pygame.image.load(settings.IMAGE_POWERUP).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.POWERUP_WIDTH, settings.POWERUP_HEIGHT))
        self.rect = self.image.get_rect(
            center=(x or random.randint(0, settings.SCREEN_WIDTH - settings.POWERUP_WIDTH), y or 0)
        )
        self.vy = 2  # Vertical speed
        self.active = True

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.active = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
