# filepath: c:\Files\MFD Personal\Programming\python\photon3_pygui\photon_main.py
# photon_main

# Import Modules **************************************************************************************
import pygame  						 # you need to install pygame from https://github.com/pygame/pygame
import p_customizations				 # where all your custom configurations for the UI go
import photon_ui                         # import the new UI module

# interface config variables **************************************************************************
pygame_window_width = p_customizations.pygame_window_width
pygame_window_height = p_customizations.pygame_window_height

# Initialize Pygame and create the display ************************************************************
pygame.init()
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption(p_customizations.program_name)

# main game loop *************************************************************************************
running = True
while running:
    for event in pygame.event.get():    			# gets pygame events like mouse clicks & key press
        if event.type == pygame.QUIT:				# quits if the exit is clicked
            running = False

    # DRAW SCREEN
    screen.fill(photon_ui.background_color)  # Use the background color from the UI module

    # Draw main elements in game area
    photon_ui.draw_main_elements(screen)  # Call the function to draw main elements

    # Draw interface foreground
    photon_ui.draw_interface_bars(screen)  # Call the function to draw interface bars

    # Draw interface buttons (if any)
    photon_ui.draw_interface_buttons(screen)  # Call the function to draw buttons

    pygame.display.flip()  # redraw pygame window - this must be the last line