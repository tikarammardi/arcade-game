import pygame
from app import settings
from app.bullet import Bullet
from app.player import Player
from app.score_manager import ScoreManager
from app.alien_manager import AlienManager
from app.game_renderer import GameRenderer

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
        self.font = pygame.font.Font(None, 36)
        self.end_game_font = pygame.font.Font(None, 72)
        self.renderer = GameRenderer(self.screen, self.font, self.end_game_font)

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

    def shoot_bullet(self):
        bullet_x = self.player.rect.centerx
        bullet_y = self.player.rect.top
        self.bullets.append(Bullet(bullet_x, bullet_y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-1)
        if keys[pygame.K_RIGHT]:
            self.player.move(1)

        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

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
        self.renderer.draw_score(self.score_manager.current_score, self.score_manager.high_score)
        if self.game_over:
            self.renderer.draw_game_over()
        elif self.won:
            self.renderer.draw_win_message()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
