class Settings():
    """ A class to store all settings for the game """

    # Function: Init    
    def __init__(self):
        """ Initialize the game settings """

        # Ship speed factor -never changes-
        self.ship_speed_factor = 10

        # Bullet settings
        self.bullet_speed_factor_start = 10
        self.bullet_speed_factor_step  = 2
        self.bullet_speed_factor_max   = 30
        self.bullet_speed_factor       = self.bullet_speed_factor_start

        # Bullet width
        self.bullet_width_start = 10
        self.bullet_width_step  = 2
        self.bullet_width_min   = 2
        self.bullet_width       = self.bullet_width_start

        # Bullet height
        self.bullet_height_start = 20
        self.bullet_height_step  = 2
        self.bullet_height_min   = 5
        self.bullet_height       = self.bullet_height_start

        # Bullet color
        self.bullet_color = (255, 255, 0)
    
        # Screen Settings
        self.screen_width = 900
        self.screen_height = 569 
        self.bg_color = (230, 230, 230)

        # Alien sideways speed
        self.alien_speed_factor_start     = 4
        self.alien_speed_factor_step      = 1
        self.alien_speed_factor           = self.alien_speed_factor_start

        # Alien drop speed
        self.fleet_drop_speed_start       = 4
        self.fleet_drop_speed_step        = 1
        self.fleet_drop_speed             = self.fleet_drop_speed_start
        self.fleet_direction = 1    # 1 = right, -1 left