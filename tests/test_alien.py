from app.alien import Alien

def test_alien_initial_position():
    alien = Alien(100, 100)
    assert alien.rect.x == 100
    assert alien.rect.y == 100

def test_alien_update():
    alien = Alien(100, 100)
    initial_x = alien.rect.x
    alien.update(1)  # Move right
    assert alien.rect.x > initial_x
