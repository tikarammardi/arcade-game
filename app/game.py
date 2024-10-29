
import pygame

from app import settings
from app.alien import Alien
from app.bullet import Bullet
from app.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Arcade Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50)
        self.bullets = []
        self.aliens = []
        self.alien_direction = 1 # 1 for right, -1 for left
        self.create_aliens()

    def run(self):
        while self.running:
            self.clock.tick(60)  # Limit to 60 FPS
            self.handle_events()
            self.update()
            self.draw()
    def create_aliens(self):
        for row in range(settings.NUM_ALIEN_ROWS):
            for col in range(settings.NUM_ALIEN_COLS):
                x = col * (settings.ALIEN_WIDTH + 10) + 50
                y = row * (settings.ALIEN_HEIGHT + 10) + 50
                alien = Alien(x, y)
                self.aliens.append(alien)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.shoot_bullet()

    def shoot_bullet(self):
        bullet_x = self.player.rect.centerx
        bullet_y = self.player.rect.top
        bullet = Bullet(bullet_x, bullet_y)
        self.bullets.append(bullet)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move(1)

        for bullet in self.bullets[:]:
            bullet.update()
            # Remove bullets that have moved off-screen
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        self.update_aliens()

        # Check for collisions between bullets and aliens
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    break

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for alien in self.aliens:
            alien.draw(self.screen)
        pygame.display.flip()

    def update_aliens(self ):
        move_down = False
        # Move aliens horizontally i.e. left or right
        for alien in self.aliens:
            alien.update(self.alien_direction)
            if alien.rect.right >= settings.SCREEN_WIDTH or alien.rect.left <= 0:
                move_down = True
        # Move aliens down and change direction
        if move_down:
            self.alien_direction *= -1
            for alien in self.aliens:
                alien.drop_down()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
