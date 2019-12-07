# Dependencies
import sys
import pygame
from time import sleep

# Imports
from bullet import Bullet
from alien import Alien

# The ship has been hit. The game resets.
def ship_hit(ai_settings, screen, ship, aliens, bullets):
    """ A ship has been hit """
    
    # Clean aliens and bullets
    aliens.empty()
    bullets.empty()

    # Reset the game
    restart_difficulty(ai_settings)
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    sleep(1)

#--------------------------------------------

# Checks key down events    
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Handles key down events """
    if(event.key == pygame.K_RIGHT): # Move right
        ship.moving_right = True
    if(event.key == pygame.K_LEFT):  # Move left 
        ship.moving_left = True
    if(event.key == pygame.K_UP):  # Move up 
        ship.moving_up = True
    if(event.key == pygame.K_DOWN):  # Move down
        ship.moving_down = True
    if(event.key == pygame.K_SPACE):  # Space fire bullets
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
    if(event.key == pygame.K_q): # Key q
        sys.exit()

#--------------------------------------------

# Checks key up events
def check_keyup_events(event, ship):
    """ Handles key up events """
    if(event.key == pygame.K_RIGHT): # Stop moving right
        ship.moving_right = False
    if(event.key == pygame.K_LEFT): # Stop moving left
        ship.moving_left = False
    if(event.key == pygame.K_UP): # Stop moving up
        ship.moving_up = False
    if(event.key == pygame.K_DOWN): # Stop moving down
        ship.moving_down = False

#--------------------------------------------

# Checks events
def check_events(ai_settings, screen, ship, bullets):
    """ Responds to keys and mouse events """
    
    for event in pygame.event.get():
        # Exit
        if event.type == pygame.QUIT:
            sys.exit()

        # Keydown events
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        # Key up events
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

#--------------------------------------------

# Handles collisions between bullets and aliens
def handle_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """ Checks if bullets hit aliens and recreates the fleet """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # If no more aliens
    if(len(aliens) == 0):

        # Destroy all bullets and aliens
        bullets.empty()

        # Start over
        create_fleet(ai_settings, screen, ship, aliens)

        # Reset difficulty
        increase_difficulty(ai_settings)

#--------------------------------------------

# Increase the gameplay by one
def increase_difficulty(ai_settings):
    """ Make ship speed faster by one step """
    ai_settings.alien_speed_factor = ai_settings.alien_speed_factor + ai_settings.alien_speed_factor_step
    ai_settings.fleet_drop_speed = ai_settings.fleet_drop_speed + ai_settings.fleet_drop_speed_step
    ai_settings.bullet_width = max(ai_settings.bullet_width_min, ai_settings.bullet_width - ai_settings.bullet_width_step)
    ai_settings.bullet_height = max(ai_settings.bullet_height_min, ai_settings.bullet_height - ai_settings.bullet_height_step)
    ai_settings.bullet_speed_factor = min(ai_settings.bullet_speed_factor_start, ai_settings.bullet_speed_factor + ai_settings.bullet_speed_factor_step)

#--------------------------------------------

# Restart game difficulty
def restart_difficulty(ai_settings):
    """ Make difficulty easy again"""
    ai_settings.alien_speed_factor = ai_settings.alien_speed_factor_start
    ai_settings.fleet_drop_speed = ai_settings.fleet_drop_speed_start
    ai_settings.bullet_width = ai_settings.bullet_width_start
    ai_settings.bullet_height = ai_settings.bullet_height_start
    ai_settings.bullet_speed_factor = ai_settings.bullet_speed_factor

#--------------------------------------------

# Updates bullets positions
def update_bullets(ai_settings, screen, ship, bullets, aliens):
    """ Update position of bullets """
    bullets.update()

    # Get rid of bullets that go off
    for bullet in bullets.copy():
        if(bullet.rect.bottom <= 0):
            bullets.remove(bullet)

    # Check collisions
    handle_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

#--------------------------------------------

# Get the number of rows
def get_number_rows(ai_settings, ship_height, alien_height):
    """ Determines number of rows """
    #available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    available_space_y = (ai_settings.screen_height / 2.5)
    number_rows   = int(available_space_y / (1.5 * alien_height))
    return(number_rows)

#--------------------------------------------

# Get number of aliens
def get_number_of_aliens_x(ai_settings, alien_width):
    """ Returns number of aliens per row """
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return(number_aliens_x)

#--------------------------------------------

# Creates an alien
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ Create an alien and place it in a row """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width 
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number
    aliens.add(alien)

#--------------------------------------------

# Change fleet direction
def change_fleet_direction(ai_settings, aliens):
    """ Drop the fleet and change direction """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    
    # Change direction
    if(ai_settings.fleet_direction == 1):
        ai_settings.fleet_direction = -1
    else:
        ai_settings.fleet_direction = 1

#--------------------------------------------

# Check fleet edges
def check_fleet_edges(ai_settings, aliens):
    """ Respond if any alien reaches the edge """
    for alien in aliens.sprites():
        if(alien.check_edges()):
            change_fleet_direction(ai_settings, aliens)
            break

#--------------------------------------------

# Creates the fleet
def create_fleet(ai_settings, screen, ship, aliens):
    """ Creates a fleet of aliens """
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the first row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
           create_alien(ai_settings, screen, aliens, alien_number, row_number)

#--------------------------------------------

# Updates screen
def update_screen(ai_settings, screen, ship, aliens, bullets):
    """ Updates screen """
    # Background image
    background_image = pygame.image.load("images/background.jpg").convert()

    # Redraw screen
    # screen.fill(ai_settings.bg_color)
    screen.blit(background_image, [0,0])
    
    # Redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Display ship
    ship.blitme()

    # Display alient
    #alien.blitme()

    # Show aliens
    aliens.draw(screen)

    # Make screen visible
    pygame.display.flip()

#--------------------------------------------

# Checks if aliens reach the bottom of the screen
def check_aliens_bottom(ai_settings, screen, ship, aliens, bullets):
    """ Checks if aliens reach the center of the screen """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if(alien.rect.bottom >= screen_rect.bottom):
            ship_hit(ai_settings, screen, ship, aliens, bullets)

#--------------------------------------------

# Update aliens
def update_aliens(ai_settings, screen, ship, aliens, bullets):
    """ Check edges and update """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Check collision with our ship
    if(pygame.sprite.spritecollideany(ship, aliens)):
        ship_hit(ai_settings, screen, ship, aliens, bullets)
    
    # Check aliens reaching the bottom of the screen
    check_aliens_bottom(ai_settings, screen, ship, aliens, bullets)
