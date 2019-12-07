# Dependencies
import pygame
from pygame.sprite import Group

# Imports
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien

# Runs the game
def run_game():
    """ Runs the game"""

    # start a screen object
    pygame.init()

    # Read settings
    ai_settings = Settings()

    # Screen
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("PyAlien Invaders")

    # make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets
    bullets = Group()

    # Make a group to store aliens
    aliens = Group()

    # Make an alien
    # alien = Alien(ai_settings, screen)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main loop
    while True:
        # Events check using game functions module
        gf.check_events(ai_settings, screen, ship, bullets)

        # Update ship and bullets
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
        
        # Update aliens
        gf.update_aliens(ai_settings, screen, ship, aliens, bullets)

        # Draw screen as set up now
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

# Run game
run_game()
