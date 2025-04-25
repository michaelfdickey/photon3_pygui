# photon_main

#******************************************************************************************************
# Import Modules **************************************************************************************
#******************************************************************************************************
import pygame  						 # you need to install pygame from https://github.com/pygame/pygame
#import p_customizations				 # where all your custom configurations for the UI go
import photon_ui as pui # Import the new UI module


#******************************************************************************************************
# interface config variables **************************************************************************
#******************************************************************************************************

"""
## window size, don't change these here, change in p_customizations.py
pygame_window_width = p_customizations.pygame_window_width
pygame_window_height = p_customizations.pygame_window_height

## fonts
pygame.font.init() 								# you have to call this at the start to use this module.
myfont = pygame.font.SysFont('Arial', 15)		# sets font type and size

##interface colors
background_color = (0,0,0)
UI_background_color = (102, 0, 51)
UI_button_border_color = (153, 0, 76)
UI_button_color = (204, 0, 102)
UI_button_click_color = (255, 0, 127)

## regular colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

## UI bar thickness
UI_topBar_height = 24
UI_bottomBar_height = 24
UI_sideBar_left_width = 124
UI_sideBar_right_width = 24 
"""


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

	# redraw the window, this must be the last line
	pygame.display.flip() 							# redraw pygame window - this must be the last line