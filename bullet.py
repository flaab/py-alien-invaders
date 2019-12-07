# Dependencies
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship """

    # Constructs a bullet
    def __init__(self, ai_settings, screen, ship):
        """ Create a bullet object in the ship position """
        super(Bullet, self).__init__()
        self.screen = screen

        # Create the bullet
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store position as decimal
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    #--------------------------------------------

    # Updates bullet positions
    def update(self):
        """ Move the bullet up the screen """

        # Update position
        self.y -= self.speed_factor

        # Update rect position
        self.rect.y = self.y 

    #--------------------------------------------

    # Draws a bullet
    def draw_bullet(self):
        """ Draw the damn thing """
        pygame.draw.rect(self.screen, self.color, self.rect)