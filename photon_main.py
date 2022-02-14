# photon_main


# Import Modules **************************************************************************************
#******************************************************************************************************
import pygame  						 # you need to install pygame from https://github.com/pygame/pygame

# user set variables **********************************************************************************
#******************************************************************************************************
program_name = 'My Program Name'



# interface config variables **************************************************************************
#******************************************************************************************************

## window
pygame_window_width = 1200
pygame_window_height = 1200

## fonts
pygame.font.init() 								# you have to call this at the start to use this module.
myfont = pygame.font.SysFont('Arial', 15)		# sets font type and size

##interface colors

background_color = (0,0,0)
UI_background_color = (102, 0, 51)
UI_button_border_color = (153, 0, 76)
UI_button_color = (204, 0, 102)
UI_button_click_color = (255, 0, 127)



# pygame display *************************************************************************************
#*****************************************************************************************************
screen = pygame.display.set_mode((pygame_window_width, pygame_window_height))
pygame.display.set_caption(program_name)


# main game loop *************************************************************************************
#*****************************************************************************************************
running = True
while running == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False