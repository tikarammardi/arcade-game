import pygame
import random
from app.power_up import PowerUp
from app import settings

class PowerUpManager:
    def __init__(self):
        self.active_power_up = None
        self.power_up_end_time = 0
        self.power_up_message = ""         # Message to display for active power-up
        self.show_expiry_message = False   # Flag to show expiry message briefly
        self.expiry_message_start_time = 0 # Track when the expiry message started
        self.is_invincible = False         # Track invincibility status

    def spawn_power_up(self):
        """Randomly spawn a power-up."""
        if random.random() < settings.POWER_UP_SPAWN_RATE:
            power_up_type = random.choice(["rapid_fire", "invincibility"])
            return PowerUp(power_up_type)
        return None

    def activate_power_up(self, power_up):
        """Activate the specified power-up effect."""
        self.active_power_up = power_up.type
        self.power_up_end_time = pygame.time.get_ticks() + settings.POWER_UP_DURATION
        self.power_up_message = f"Power-Up Activated: {self.active_power_up.capitalize()}"

        # Activate specific power-up effects
        if self.active_power_up == "invincibility":
            self.is_invincible = True  # Enable invincibility

    def deactivate_power_up(self):
        """Deactivate the current power-up effect."""
        if self.active_power_up == "invincibility":
            self.is_invincible = False  # Disable invincibility

        self.active_power_up = None
        self.power_up_message = ""  # Clear active message
        self.show_expiry_message = True  # Show expiry message
        self.expiry_message_start_time = pygame.time.get_ticks()  # Set expiry start time

    def handle_active_effects(self, player):
        """Apply effects of the active power-up to the player."""
        if self.active_power_up == "rapid_fire":
            player.shoot_delay = settings.RAPID_FIRE_DELAY
        else:
            player.shoot_delay = settings.NORMAL_SHOOT_DELAY

    def check_expired(self):
        """Check if the active power-up has expired and deactivate it if so."""
        if self.active_power_up and pygame.time.get_ticks() > self.power_up_end_time:
            self.deactivate_power_up()

    def update_expiry_message(self):
        """Show the 'Power-Up Expired' message for 1 second."""
        if self.show_expiry_message and pygame.time.get_ticks() - self.expiry_message_start_time > 1000:
            self.show_expiry_message = False
