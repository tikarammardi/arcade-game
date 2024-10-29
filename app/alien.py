import pygame
from app import settings


class Alien:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, settings.ALIEN_WIDTH, settings.ALIEN_HEIGHT)
        self.color = settings.ALIEN_COLOR
        self.speed = settings.ALIEN_SPEED

    def update(self, direction):
        # Move horizontally based on the direction (+1 for right, -1 for left)
        self.rect.x += self.speed * direction

    def drop_down(self):
        # Move the alien down by one row height
        self.rect.y += settings.ALIEN_HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
