import pygame
from app import settings


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, settings.BULLET_WIDTH, settings.BULLET_HEIGHT)
        self.color = settings.BULLET_COLOR
        self.speed = settings.BULLET_SPEED

    def update(self):
        # Move the bullet upward
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
