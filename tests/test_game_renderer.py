import pytest
import pygame
from app.game_renderer import GameRenderer
from app.player import Player
from app.bullet import Bullet
from app.alien import Alien

@pytest.fixture(scope="module")
def pygame_setup():
    pygame.init()
    yield
    pygame.quit()

def test_renderer_initialization(pygame_setup):
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 36)
    end_game_font = pygame.font.Font(None, 72)
    renderer = GameRenderer(screen, font, end_game_font)
    assert renderer

def test_draw_score(pygame_setup):
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 36)
    end_game_font = pygame.font.Font(None, 72)
    renderer = GameRenderer(screen, font, end_game_font)
    renderer.draw_score(100, 200)  # Just make sure it runs without errors

def test_draw_game_objects(pygame_setup):
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 36)
    end_game_font = pygame.font.Font(None, 72)
    renderer = GameRenderer(screen, font, end_game_font)
    player = Player(400, 550)
    bullet = Bullet(400, 300)
    alien = Alien(100, 100)
    renderer.draw_game_objects(player, [bullet], [alien])  # Check that it runs without errors
