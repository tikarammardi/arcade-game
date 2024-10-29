import pygame
from app import settings
from app.bullet import Bullet
from app.player import Player
from app.score_manager import ScoreManager
from app.alien_manager import AlienManager
from app.game_renderer import GameRenderer
from app.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("Arcade Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.won = False
        self.player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50)
        self.bullets = []

        # Managers and Renderer
        self.score_manager = ScoreManager()
        self.alien_manager = AlienManager()
        self.power_up_manager = PowerUpManager()
        self.font = pygame.font.Font(None, 36)
        self.end_game_font = pygame.font.Font(None, 72)
        self.renderer = GameRenderer(self.screen, self.font, self.end_game_font)

        # Power-up and shooting cooldowns
        self.current_power_up = None
        self.last_shot_time = 0  # Track time of last shot for bullet cooldown

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            if not self.game_over and not self.won:
                self.update()
            self.draw()

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
        self.score_manager.save_high_score()
        self.score_manager.reset_score()
        self.bullets.clear()
        self.alien_manager.create_aliens()
        self.current_power_up = None
        self.power_up_manager.deactivate_power_up()

    def shoot_bullet(self):
        if pygame.time.get_ticks() - self.last_shot_time < self.player.shoot_delay:
            return
        bullet_x = self.player.rect.centerx
        bullet_y = self.player.rect.top
        self.bullets.append(Bullet(bullet_x, bullet_y))
        self.last_shot_time = pygame.time.get_ticks()

    # app/game.py

    def update(self):
        # Spawn a new power-up if none is currently on the screen
        if not self.current_power_up:
            self.current_power_up = self.power_up_manager.spawn_power_up()

        # Update and draw the current power-up
        if self.current_power_up:
            self.current_power_up.update()  # Move the power-up down
            if self.current_power_up.rect.top > settings.SCREEN_HEIGHT:
                self.current_power_up = None  # Remove power-up if it goes off screen

        # Check if player collected the power-up
        if self.current_power_up and self.player.rect.colliderect(self.current_power_up.rect):
            self.power_up_manager.activate_power_up(self.current_power_up)
            self.current_power_up = None

        # Check power-up expiration and apply effects
        self.power_up_manager.check_expired()
        self.power_up_manager.handle_active_effects(self.player)

        # Continue with other game updates...
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move(1)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

        # Alien updates and collision checking
        self.alien_manager.update_aliens()
        self.check_collisions()
        self.check_game_status()


    def check_game_status(self):
        if self.alien_manager.all_aliens_defeated():
            self.won = True
            self.score_manager.save_high_score()
        elif self.alien_manager.check_alien_reached_bottom():
            self.game_over = True
            self.score_manager.save_high_score()

    def check_collisions(self):
        for bullet in self.bullets[:]:
            for alien in self.alien_manager.aliens[:]:
                if bullet.rect.colliderect(alien.rect):
                    self.bullets.remove(bullet)
                    self.alien_manager.remove_alien(alien)
                    self.score_manager.update_score(1)
                    break

    def draw(self):
        self.renderer.draw_game_objects(self.player, self.bullets, self.alien_manager.aliens)

        # Draw current power-up if it exists
        if self.current_power_up:
            self.current_power_up.draw(self.screen)

        # Display score and high score
        self.renderer.draw_score(self.score_manager.current_score, self.score_manager.high_score)

        # Display active power-up message
        if self.power_up_manager.power_up_message:
            power_up_text = self.font.render(self.power_up_manager.power_up_message, True, (0, 255, 0))
            self.screen.blit(power_up_text, (settings.SCREEN_WIDTH // 2 - 100, 10))

        # Display expiry message if applicable
        if self.power_up_manager.show_expiry_message:
            expiry_text = self.font.render("Power-Up Expired", True, (255, 0, 0))
            self.screen.blit(expiry_text, (settings.SCREEN_WIDTH // 2 - 80, 50))
            self.power_up_manager.update_expiry_message()

        # Display game-over or win messages
        if self.game_over:
            self.renderer.draw_game_over()
        elif self.won:
            self.renderer.draw_win_message()

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
