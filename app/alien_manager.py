from app.alien import Alien
from app import settings

class AlienManager:
    def __init__(self):
        self.aliens = []
        self.direction = 1  # 1 for right, -1 for left
        self.create_aliens()

    def create_aliens(self):
        self.aliens.clear()
        for row in range(settings.NUM_ALIEN_ROWS):
            for col in range(settings.NUM_ALIEN_COLS):
                x = col * (settings.ALIEN_WIDTH + 10) + 50
                y = row * (settings.ALIEN_HEIGHT + 10) + 50
                alien = Alien(x, y)
                self.aliens.append(alien)

    def update_aliens(self):
        move_down = False
        for alien in self.aliens:
            alien.update(self.direction)
            if alien.rect.right >= settings.SCREEN_WIDTH or alien.rect.left <= 0:
                move_down = True
        if move_down:
            self.direction *= -1
            for alien in self.aliens:
                alien.drop_down()

    def check_alien_reached_bottom(self):
        for alien in self.aliens:
            if alien.rect.bottom >= settings.SCREEN_HEIGHT:
                return True
        return False

    def remove_alien(self, alien):
        if alien in self.aliens:
            self.aliens.remove(alien)

    def all_aliens_defeated(self):
        return len(self.aliens) == 0
