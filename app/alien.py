import pygame
from app import settings

class Alien:
    def __init__(self, x, y):
        # Load and resize the alien image
        self.image = pygame.image.load(settings.IMAGE_ALIEN).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.ALIEN_WIDTH, settings.ALIEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = settings.ALIEN_SPEED

    def update(self, direction):
        self.rect.x += self.speed * direction

    def drop_down(self):
        self.rect.y += settings.ALIEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)
