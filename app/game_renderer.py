# app/game_renderer.py
import pygame

class GameRenderer:
    def __init__(self, screen, font, end_game_font):
        self.screen = screen
        self.font = font
        self.end_game_font = end_game_font

    def draw_score(self, current_score, high_score):
        score_text = self.font.render(f"Score: {current_score}", True, (255, 255, 255))
        high_score_text = self.font.render(f"High Score: {high_score}", True, (255, 255, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(high_score_text, (10, 40))

    def draw_game_over(self):
        game_over_text = self.end_game_font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.font.render("Press 'R' to Restart", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 30))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - 120, self.screen.get_height() // 2 + 20))

    def draw_win_message(self):
        win_text = self.end_game_font.render("YOU WIN!", True, (0, 255, 0))
        restart_text = self.font.render("Press 'R' to Restart", True, (255, 255, 255))
        self.screen.blit(win_text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 30))
        self.screen.blit(restart_text, (self.screen.get_width() // 2 - 120, self.screen.get_height() // 2 + 20))

    def draw_game_objects(self, player, bullets, aliens):
        self.screen.fill((0, 0, 0))
        player.draw(self.screen)
        for bullet in bullets:
            bullet.draw(self.screen)
        for alien in aliens:
            alien.draw(self.screen)
