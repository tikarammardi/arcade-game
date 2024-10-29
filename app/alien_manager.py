from app.alien import Alien
from app import settings
import random

class AlienManager:
    def __init__(self):
        self.aliens = []
        self.direction = 1  # 1 for right, -1 for left
        self.create_aliens()


    def create_aliens(self):
        """Create the initial set of regular aliens."""
        self.aliens.clear()
        for row in range(settings.NUM_ALIEN_ROWS):
            for col in range(settings.NUM_ALIEN_COLS):
                x = col * (settings.ALIEN_WIDTH + 10) + 50
                y = row * (settings.ALIEN_HEIGHT + 10) + 50
                alien = Alien(x, y)
                self.aliens.append(alien)

    def spawn_dropping_alien(self):
        """Randomly spawn a dropping alien at the top of the screen."""
        x = random.randint(0, settings.SCREEN_WIDTH - settings.ALIEN_WIDTH)
        dropping_alien = Alien(x, 0, is_dropping=True)  # Set is_dropping to True for this alien
        self.aliens.append(dropping_alien)

    def update_aliens(self):
        """Update the position of all aliens and handle dropping aliens separately."""
        move_down = False

        for alien in self.aliens:
            if alien.is_dropping:
                # Make dropping aliens fall vertically
                alien.drop_down()  # Dropping aliens fall straight down
            else:
                # Regular aliens move horizontally
                alien.update(self.direction)
                if alien.rect.right >= settings.SCREEN_WIDTH or alien.rect.left <= 0:
                    move_down = True

        # Change direction and move regular aliens down if they reach screen edges
        if move_down:
            self.direction *= -1
            for alien in self.aliens:
                if not alien.is_dropping:
                    alien.drop_down()

        # Randomly spawn a dropping alien based on spawn rate
        if random.random() < settings.DROPPING_ALIEN_SPAWN_RATE:
            self.spawn_dropping_alien()

    def check_alien_reached_bottom(self):
        """Check if any alien has reached the bottom of the screen."""
        for alien in self.aliens:
            if alien.rect.bottom >= settings.SCREEN_HEIGHT:
                return True
        return False

    def remove_alien(self, alien):
        """Remove a specific alien from the list."""
        if alien in self.aliens:
            self.aliens.remove(alien)

    def all_aliens_defeated(self):
        """Check if all aliens have been defeated."""
        return len(self.aliens) == 0
