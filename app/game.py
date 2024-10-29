import json
import os.path
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
        self.game_over = False
        self.won = False  # Track if player won
        self.player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50)
        self.bullets = []
        self.aliens = []
        self.alien_direction = 1  # 1 for right, -1 for left
        self.create_aliens()
        self.score = 0
        self.high_score = self.load_high_score()

        self.font = pygame.font.Font(None, 36)
        self.end_game_font = pygame.font.Font(None, 72)

    def run(self):
        while self.running:
            self.clock.tick(60)  # Limit to 60 FPS
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()

    def load_high_score(self):
        try:
            if os.path.exists("high_score.json"):
                with open("high_score.json", "r") as file:
                    data = json.load(file)
                    return data.get("high_score", 0)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading high score. Initializing to 0.")
        return 0

    def save_high_score(self):
        try:
            data = {"high_score": self.high_score}
            with open("high_score.json", "w") as file:
                json.dump(data, file)
        except IOError:
            print("Error saving high score.")

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
            if (self.game_over or self.won) and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset_game()

    def reset_game(self):
        self.game_over = False
        self.won = False
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.player.rect.x = settings.SCREEN_WIDTH // 2
        self.bullets.clear()
        self.aliens.clear()
        self.create_aliens()

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
        self.check_collisions()
        self.check_game_over()

    def check_game_over(self):
        # Check if all aliens are defeated (winning condition)
        if not self.aliens:
            self.won = True
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            return

        # Check if any alien has reached the bottom of the screen (losing condition)
        for alien in self.aliens:
            if alien.rect.bottom >= settings.SCREEN_HEIGHT:
                self.game_over = True
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.save_high_score()
                break

    def draw(self):
        self.screen.fill(settings.BACKGROUND_COLOR)
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for alien in self.aliens:
            alien.draw(self.screen)

        self.display_score()
        pygame.display.flip()

    def display_score(self):
        # Display score and high score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, (255, 255, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(high_score_text, (10, 40))

        if self.game_over:
            # Display game over message
            game_over_text = self.end_game_font.render("GAME OVER", True, (255, 0, 0))
            restart_text = self.font.render("Press 'R' to Restart", True, (255, 255, 255))
            self.screen.blit(game_over_text, (settings.SCREEN_WIDTH // 2 - 100, settings.SCREEN_HEIGHT // 2 - 30))
            self.screen.blit(restart_text, (settings.SCREEN_WIDTH // 2 - 120, settings.SCREEN_HEIGHT // 2 + 20))

        elif self.won:
            # Display winning message
            win_text = self.end_game_font.render("YOU WIN!", True, (0, 255, 0))
            restart_text = self.font.render("Press 'R' to Restart", True, (255, 255, 255))
            self.screen.blit(win_text, (settings.SCREEN_WIDTH // 2 - 100, settings.SCREEN_HEIGHT // 2 - 30))
            self.screen.blit(restart_text, (settings.SCREEN_WIDTH // 2 - 120, settings.SCREEN_HEIGHT // 2 + 20))

    def update_aliens(self):
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

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for alien in self.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.bullets.remove(bullet)
                    self.aliens.remove(alien)
                    self.score += 1
                    break

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
