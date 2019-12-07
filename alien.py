# Imports
import pygame
from pygame.sprite import Sprite

# Alien class
class Alien(Sprite):
    """ A class to represent a single alien in the fleet """

    # Constructor
    def __init__(self, ai_settings, screen):
        """ Initialize the alien and set position """

        # Super constructor
        super(Alien, self).__init__()

        # Screen settings
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien and imge
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Start alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store position
        self.x = float(self.rect.x)

    #--------------------------------------------

    # Shows the alien
    def blitme(self):
        """ Draw the alien """
        self.screen.blit(self.image, self.rect)

    #--------------------------------------------

    # Check edges
    def check_edges(self):
        """ Return true if alien is at edge """
        screen_rect = self.screen.get_rect()
        if(self.rect.right >= screen_rect.right):
            return(True)
        elif(self.rect.left <= 0):
            return(True)

    #--------------------------------------------

    # Update the alien
    def update(self):
        """ Move the alien to the right or left """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x