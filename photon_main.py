# photon_main

# Import Modules **************************************************************************************
#******************************************************************************************************
import pygame  						 # you need to install pygame from https://github.com/pygame/pygame
import p_customizations				 # where all your custom configurations for the UI go


# interface config variables **************************************************************************
#******************************************************************************************************

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
UI_topBar_height = 40
UI_bottomBar_height = 40
UI_sideBar_left_width = 120
UI_sideBar_right_width = 20 




# pygame display *************************************************************************************
#*****************************************************************************************************
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption(p_customizations.program_name)


# main game loop *************************************************************************************
#*****************************************************************************************************
running = True
while running == True:
	for event in pygame.event.get():    			# gets pygame events like mouse clicks & key press
		if event.type == pygame.QUIT:				# quits if the exit is clicked
			running = False

	# DRAW SCREEN
	## draw background
	screen.fill(background_color)

	## draw main elements in game area
	pygame.draw.lines(screen, red, False, [(0,600), (1200,600)], 1)
	pygame.draw.lines(screen, red, False, [(600,0), (600,1200)], 1)
	pygame.draw.circle(screen, red, (600,600), 550, 1)

	## draw interface foreground
	### interface background bars
	pygame.draw.rect(screen, UI_background_color, (0, 0, pygame_window_width, UI_topBar_height)) 													#top bar
	pygame.draw.rect(screen, UI_background_color, (100, pygame_window_height-UI_bottomBar_height, pygame_window_width, UI_bottomBar_height)) 		#bottom bar
	pygame.draw.rect(screen, UI_background_color, (0, 0, UI_sideBar_left_width, pygame_window_height)) 												#left side bar
	pygame.draw.rect(screen, UI_background_color, (pygame_window_width-UI_sideBar_right_width, 0, UI_sideBar_left_width, pygame_window_height)) 		#right side bar

	### interface buttons



	pygame.display.flip() # redraw pygame window - this must be the last line