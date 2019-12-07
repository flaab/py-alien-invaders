# Dependencies
import pygame

# Class Ship
class Ship():

    # Constructor
    def __init__(self, ai_settings, screen):
        """ Initializes the sip and sets position """

        # Set screen
        self.screen = screen

        # Save settings for the object
        self.ai_settings = ai_settings

        # Load ship
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start new ship
        self.rect.centerx = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left  = False 
        self.moving_up = False
        self.moving_down  = False 

    #--------------------------------------------

    # Updates the ship position
    def update(self):
            """ Update ship position based on flag """
            
            # Move Ship
            if(self.moving_right):
                self.rect.centerx = min(self.ai_settings.screen_width, self.rect.centerx + self.ai_settings.ship_speed_factor)
            if(self.moving_left):
                self.rect.centerx = max(0, self.rect.centerx - self.ai_settings.ship_speed_factor)
            if(self.moving_up):
                self.rect.centery = max(0, self.rect.centery - self.ai_settings.ship_speed_factor)
            if(self.moving_down):
                self.rect.centery = min(self.ai_settings.screen_height, self.rect.centery + self.ai_settings.ship_speed_factor)

    #--------------------------------------------

    # Shows the ship
    def blitme(self):
        """ Draws ship in current location """
        self.screen.blit(self.image, self.rect)

    #--------------------------------------------

    # Center ship on the screen
    def center_ship(self):
        """ Move the ship to the center of the screen """
        self.center = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    