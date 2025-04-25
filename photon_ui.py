import pygame

program_name = 'Photon3 GUI'    # name of the program, used in the window title bar

#window size
pygame_window_width = 1800
pygame_window_height = 1200

# UI Colors
background_color = (0, 0, 0)
UI_background_color = (102, 0, 51)
UI_button_border_color = (153, 0, 76)
UI_button_color = (204, 0, 102)
UI_button_click_color = (255, 0, 127)

# Regular Colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

# UI Dimensions
UI_topBar_height = 24
UI_bottomBar_height = 24
UI_sideBar_left_width = 124
UI_sideBar_right_width = 24

def draw_ui_background(screen, window_width, window_height):
    """Draws the UI background elements."""
    screen.fill(background_color)

def draw_ui_borders(screen, window_width, window_height):
    """Draws the UI borders."""
    pygame.draw.rect(screen, UI_background_color, (0, 0, window_width, UI_topBar_height))  # Top bar
    pygame.draw.rect(screen, UI_background_color, (0, 0, UI_sideBar_left_width, window_height))  # Left sidebar
    pygame.draw.rect(screen, UI_background_color, (window_width - UI_sideBar_right_width, 0, UI_sideBar_right_width, window_height))  # Right sidebar
    pygame.draw.rect(screen, UI_background_color, (100, window_height - UI_bottomBar_height, window_width, UI_bottomBar_height))  # Bottom bar

def draw_game_elements(screen):
    """Draws the main game elements."""
    pygame.draw.lines(screen, red, False, [(0, 600), (1200, 600)], 1)
    pygame.draw.lines(screen, red, False, [(600, 0), (600, 1200)], 1)
    pygame.draw.circle(screen, red, (600, 600), 550, 1)