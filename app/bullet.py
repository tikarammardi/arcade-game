import pygame
from app import settings

class Bullet:
    def __init__(self, x, y):
        # Load and resize the bullet image
        self.image = pygame.image.load(settings.IMAGE_BULLET).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.BULLET_WIDTH, settings.BULLET_HEIGHT))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = settings.BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
