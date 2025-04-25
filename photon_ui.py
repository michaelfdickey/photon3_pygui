#******************************************************************************************************
# Customization Area **********************************************************************************
#******************************************************************************************************
# This section contains all customizable settings for the UI. Modify these values as needed.

# Window Settings
program_name = "Photon GUI demo"
pygame_window_width = 1600
pygame_window_height = 1200

pygram_window_center_x = pygame_window_width / 2
pygram_window_center_y = pygame_window_height / 2

centerX = pygame_window_width / 2
centerY = pygame_window_height / 2

height = pygame_window_height   
width = pygame_window_width

# UI Colors
background_color = (0, 0, 0)
UI_background_color = (102, 0, 51)
UI_button_border_color = (153, 0, 76)
UI_button_color = (204, 0, 102)
UI_button_click_color = (255, 0, 127)

# UI Dimensions
UI_topBar_height = 24
UI_bottomBar_height = 24
UI_sideBar_left_width = 124
UI_sideBar_right_width = 24

# Fonts
font_name = "Arial"
font_size = 15

#******************************************************************************************************
# UI Logic and Drawing Functions **********************************************************************
#******************************************************************************************************

import pygame

def draw_ui_background(screen, window_width, window_height):
    """Draws the UI background elements."""
    screen.fill(background_color)

def draw_game_elements(screen):
    """Draws the main game elements."""
    # create red full size cross hairs 1 pixel thick and window center
    pygame.draw.lines(screen, (255, 0, 0), False, [(0, centerY), (width, centerY)], 1)      # horizontal center line
    pygame.draw.lines(screen, (255, 0, 0), False, [(centerX, 0), (centerX, height)], 1)     # vertical center line

    # create red circle centered at the window origin
    pygame.draw.circle(screen, (255, 0, 0), (centerX, centerY), 550, 1)

def draw_ui_borders(screen, window_width, window_height):
    """Draws UI borders."""

    # border background colors
    pygame.draw.rect(screen, UI_background_color, (0, 0, window_width, UI_topBar_height))  # Top bar
    pygame.draw.rect(screen, UI_background_color, (0, 0, UI_sideBar_left_width, window_height))  # Left sidebar
    pygame.draw.rect(screen, UI_background_color, (window_width - UI_sideBar_right_width, 0, UI_sideBar_right_width, window_height))  # Right sidebar
    pygame.draw.rect(screen, UI_background_color, (0, window_height - UI_bottomBar_height, window_width, UI_bottomBar_height))  # Bottom bar

    # border lines
    pygame.draw.rect(screen, UI_button_border_color, (0, 0, window_width, UI_topBar_height), 1)  # Top bar border
    pygame.draw.rect(screen, UI_button_border_color, (0, 0, UI_sideBar_left_width, window_height), 1)  # Left sidebar border
    pygame.draw.rect(screen, UI_button_border_color, (window_width - UI_sideBar_right_width, 0, UI_sideBar_right_width, window_height), 1)  # Right sidebar border
    pygame.draw.rect(screen, UI_button_border_color, (0, window_height - UI_bottomBar_height, window_width, UI_bottomBar_height), 1)  # Bottom bar border