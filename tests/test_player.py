
from app import settings
from app.player import Player


def test_player_move_within_bounds():
    player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT - 50)
    # Move left and right and check if the player stays within bounds
    player.move(-1)
    assert player.rect.x >= 0
    player.move(1)
    assert player.rect.x <= settings.SCREEN_WIDTH - settings.PLAYER_WIDTH

def test_player_initial_position():
    player = Player(400, 550)
    assert player.rect.x == 400
    assert player.rect.y == 550

def test_player_move():
    player = Player(400, 550)
    player.move(-1)
    assert player.rect.x < 400
