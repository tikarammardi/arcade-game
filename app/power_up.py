# app/power_up.py

import pygame
import random
from app import settings

class PowerUp:
    def __init__(self, type, x=None, y=None):
        self.type = type
        self.color = settings.POWER_UP_COLORS[type]
        self.rect = pygame.Rect(
            x or random.randint(0, settings.SCREEN_WIDTH - settings.POWER_UP_SIZE),
            y or 0,  # Start at the top of the screen by default
            settings.POWER_UP_SIZE,
            settings.POWER_UP_SIZE
        )

        # Set vertical speed so it falls downward
        self.vy = 2  # Adjust speed as desired
        self.active = False

    def update(self):
        # Move the power-up downward
        self.rect.y += self.vy

        # Remove power-up if it goes off the bottom of the screen
        if self.rect.top > settings.SCREEN_HEIGHT:
            self.active = False  # You can add logic to remove it from the game

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
