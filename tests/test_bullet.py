from app.bullet import Bullet

def test_bullet_initial_position():
    bullet = Bullet(400, 300)
    assert bullet.rect.x == 400
    assert bullet.rect.y == 300

def test_bullet_update():
    bullet = Bullet(400, 300)
    initial_y = bullet.rect.y
    bullet.update()
    assert bullet.rect.y < initial_y  # Bullet moves upward
