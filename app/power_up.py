import pygame
import random
from app import settings

class PowerUp:
    def __init__(self, type, x=None, y=None):
        self.type = type
        # Load and resize the base image
        self.base_image = pygame.image.load(settings.IMAGE_POWERUP).convert_alpha()
        self.base_image = pygame.transform.scale(self.base_image, (settings.POWERUP_WIDTH, settings.POWERUP_HEIGHT))

        # Apply tint based on type
        tint_color = settings.POWER_UP_COLORS[type]
        self.image = self.apply_tint(self.base_image, tint_color)

        # Set position
        self.rect = self.image.get_rect(
            center=(x or random.randint(0, settings.SCREEN_WIDTH - settings.POWERUP_WIDTH), y or 0)
        )
        self.vy = 2  # Vertical speed
        self.active = True

    def apply_tint(self, image, color):
        """Apply a color tint to an image."""
        # Create a copy of the image to apply the tint
        tinted_image = image.copy()
        # Create a surface filled with the tint color
        tint_surface = pygame.Surface(tinted_image.get_size(), pygame.SRCALPHA)
        tint_surface.fill(color)
        # Blend the tint surface onto the copied image
        tinted_image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        return tinted_image

    def update(self):
        self.rect.y += self.vy
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.active = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
