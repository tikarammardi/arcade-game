import pygame
from app import settings

class Alien:
    def __init__(self, x, y, is_dropping=False):
        self.image = pygame.image.load(settings.IMAGE_ALIEN).convert_alpha()
        self.image = pygame.transform.scale(self.image, (settings.ALIEN_WIDTH, settings.ALIEN_HEIGHT))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = settings.ALIEN_SPEED
        self.is_dropping = is_dropping  # Flag to indicate if the alien is a dropping alien

    def update(self, direction):
        # Only move horizontally if the alien is not a dropping alien
        if not self.is_dropping:
            self.rect.x += self.speed * direction

    def drop_down(self):
        # If it's a dropping alien, move it vertically
        if self.is_dropping:
            self.rect.y += settings.DROPPING_ALIEN_SPEED  # Set a speed for vertical drop
        else:
            # Regular alien drops down by one row height
            self.rect.y += settings.ALIEN_HEIGHT

    def draw(self, screen):
        screen.blit(self.image, self.rect)
