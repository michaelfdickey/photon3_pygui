# photon_main

#******************************************************************************************************
# Import Modules **************************************************************************************
#******************************************************************************************************
import pygame  						 # you need to install pygame from https://github.com/pygame/pygame
#import p_customizations			 # where all your custom configurations for the UI go
import photon_ui as pui # Import the new UI module



#*****************************************************************************************************
# pygame display *************************************************************************************
#*****************************************************************************************************
screen = pygame.display.set_mode((pui.pygame_window_width, pui.pygame_window_height))
pygame.display.set_caption(pui.program_name)


#*****************************************************************************************************
# main game loop *************************************************************************************
#*****************************************************************************************************
running = True
while running:
	for event in pygame.event.get():    			# gets pygame events like mouse clicks & key press
		if event.type == pygame.QUIT:				# quits if the exit is clicked
			running = False


	# draw UI background 
	pui.draw_ui_background(screen, pui.pygame_window_width, pui.pygame_window_height)

	# Draw foreground elements
	pui.draw_game_elements(screen)

	# draw UI borders
	pui.draw_ui_borders(screen, pui.pygame_window_width, pui.pygame_window_height)

	# draw buttons:
	pui.draw_example_button(screen, 0, 0, 100, 50, "Example Button") # Example button

	# redraw the window, this must be the last line
	pygame.display.flip() 							# redraw pygame window - this must be the last line