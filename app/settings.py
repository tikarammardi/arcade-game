# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# Player settings
PLAYER_SPEED = 5
PLAYER_COLOR = (0, 255, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30

# Bullet settings
BULLET_COLOR = (255, 255, 255)
BULLET_SPEED = 7
BULLET_WIDTH = 5
BULLET_HEIGHT = 15

# Alien settings
ALIEN_COLOR = (255, 0, 0)
ALIEN_WIDTH = 40
ALIEN_HEIGHT = 30
ALIEN_SPEED = 2


# Number of rows and columns of aliens
NUM_ALIEN_ROWS = 3
NUM_ALIEN_COLS = 10


# Power-Up settings
POWER_UP_DURATION = 5000  # Duration of power-up effect in milliseconds
POWER_UP_SPAWN_RATE = 0.01  # Probability of spawning a power-up per frame
POWER_UP_SIZE = 20  # Size of the power-up

POWER_UP_COLORS = {
    "rapid_fire": (0, 255, 0),         # Green for rapid-fire
    "invincibility": (255, 215, 0),    # Gold for invincibility
}

RAPID_FIRE_DELAY = 100  # ms delay for rapid-fire bullets
NORMAL_SHOOT_DELAY = 300  # ms delay for normal bullets
