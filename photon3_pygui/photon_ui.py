# filepath: c:\Files\MFD Personal\Programming\python\photon3_pygui\photon_ui.py

import pygame
import p_customizations

def draw_background(screen):
    screen.fill((0, 0, 0))  # Fill the background with black

def draw_interface_bars(screen):
    # Draw interface background bars
    pygame.draw.rect(screen, p_customizations.UI_background_color, (0, 0, p_customizations.pygame_window_width, p_customizations.UI_topBar_height))  # Top bar
    pygame.draw.rect(screen, p_customizations.UI_background_color, (100, p_customizations.pygame_window_height - p_customizations.UI_bottomBar_height, p_customizations.pygame_window_width, p_customizations.UI_bottomBar_height))  # Bottom bar
    pygame.draw.rect(screen, p_customizations.UI_background_color, (0, 0, p_customizations.UI_sideBar_left_width, p_customizations.pygame_window_height))  # Left side bar
    pygame.draw.rect(screen, p_customizations.UI_background_color, (p_customizations.pygame_window_width - p_customizations.UI_sideBar_right_width, 0, p_customizations.UI_sideBar_right_width, p_customizations.pygame_window_height))  # Right side bar

def draw_buttons(screen):
    # Placeholder for button drawing logic
    pass  # Implement button drawing logic here as needed

def draw_ui(screen):
    draw_background(screen)
    draw_interface_bars(screen)
    draw_buttons(screen)