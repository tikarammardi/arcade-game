import pygame
import random
from app import settings

class PowerUp:
    def __init__(self, type, x=None, y=None):
        self.type = type
        self.base_image = pygame.image.load(settings.IMAGE_POWERUP).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (settings.POWERUP_WIDTH, settings.POWERUP_HEIGHT))

        # Apply color tint based on type
        self.image = self.base_image.copy()
        tint_color = settings.POWER_UP_COLORS[type]
        self.image.fill(tint_color, special_flags=pygame.BLEND_RGBA_MULT)

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
