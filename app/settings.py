import os
# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)

# Player settings
PLAYER_SPEED = 5
PLAYER_COLOR = (0, 255, 0)
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 80  # Adjust width and height as needed

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
POWERUP_WIDTH, POWERUP_HEIGHT = 50, 50

POWER_UP_COLORS = {
    "rapid_fire": (0, 255, 0),         # Green for rapid-fire
    "invincibility": (255, 215, 0),    # Gold for invincibility
}

RAPID_FIRE_DELAY = 100  # ms delay for rapid-fire bullets
NORMAL_SHOOT_DELAY = 300  # ms delay for normal bullets

# Get the absolute path to the directory where settings.py is located
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Define paths using the base directory
IMAGE_PLAYER = os.path.join(BASE_DIR, "app/images/player.png")
IMAGE_ALIEN = os.path.join(BASE_DIR, "app/images/alien.png")
IMAGE_BULLET = os.path.join(BASE_DIR, "app/images/bullet.png")
IMAGE_POWERUP = os.path.join(BASE_DIR, "app/images/powerup.png")

# Other settings
SOUND_SHOOT = os.path.join(BASE_DIR, "app/sounds/shoot.mp3")
SOUND_EXPLOSION = os.path.join(BASE_DIR, "app/sounds/explosion.mp3")
SOUND_POWERUP = os.path.join(BASE_DIR, "app/sounds/powerup.mp3")
SOUND_GAME_OVER = os.path.join(BASE_DIR, "app/sounds/game_over.mp3")


DROPPING_ALIEN_SPEED = 5  # Speed of the dropping aliens
DROPPING_ALIEN_SPAWN_RATE = 0.01  # Probability of spawning a dropping alien each frame

DANGER_ZONE_Y = SCREEN_HEIGHT - 50  # Danger zone 50 pixels above the bottom
