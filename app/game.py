
import pygame

from app import settings
from app.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Arcade Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50)

    def run(self):
        while self.running:
            self.clock.tick(60)  # Limit to 60 FPS
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move(1)

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
