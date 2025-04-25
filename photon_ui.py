#******************************************************************************************************
# import modules     **********************************************************************************
#******************************************************************************************************

import pygame


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
UI_button_text_color = (255, 255, 0)  # yellow

# yellow RGB color
# yellow = (255, 255, 0)
# red = (255, 0, 0)
# green = (0, 255, 0)   
# blue = (0, 0, 255)
# darkBlue = (0, 0, 128)    
# white = (255, 255, 255)

# UI Dimensions
UI_topBar_height = 24
UI_bottomBar_height = 24
UI_sideBar_left_width = 124
UI_sideBar_right_width = 24

# Fonts
#font_name = "Arial"
#font_size = 15

pygame.font.init() 						    		# you have to call this at the start to use this module.
FontButton = pygame.font.SysFont('Arial', 15)		# sets font type and size


#******************************************************************************************************
# UI Logic and Drawing Functions **********************************************************************
#******************************************************************************************************




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



#******************************************************************************************************
# Define an indivudual button    **********************************************************************
#******************************************************************************************************

"""
pygame.Rect(x, y, width, height, 1)
    x, y: The top-left corner of the rectangle.
    width, height: The dimensions of the rectangle.
    The rectangle is drawn from the top-left corner (x, y) to the bottom-right corner (x + width, y + height).
"""


def draw_example_button(screen, x, y, width, height, text):

    # draw background of button
    pygame.draw.rect(screen, UI_button_color, (0, UI_topBar_height, UI_sideBar_left_width, 20))  # Button background

    # draw outline of button
    pygame.draw.rect(screen, UI_button_border_color, (0, UI_topBar_height, UI_sideBar_left_width, 20), 3)  # Button border

    # draw text on button
    text_surface = FontButton.render(text, True, (UI_button_text_color))            # Render the text surface
    text_rect = text_surface.get_rect(center=(UI_sideBar_left_width / 2, UI_topBar_height + 10))     # Center the text within the button

    screen.blit(text_surface, text_rect)                                            # Draw the text


def draw_buttons(screen, buttons):
    """
    Draws buttons from a dictionary of button attributes.

    Args:
        screen: The Pygame surface to draw on.
        buttons: A dictionary of buttons, where each button is a dictionary of attributes.
    """
    for button_name, button in buttons.items():
        # Extract button attributes
        x, y = button['origin']
        width = button['width']
        height = button['height']
        label = button['label']
        font = button.get('font') or FontButton  # Default to FontButton if font is None
        text_align = button.get('textAlign', 'center')  # Default to center alignment

        # Draw button background
        pygame.draw.rect(screen, UI_button_color, (x, y, width, height))

        # Draw button border
        pygame.draw.rect(screen, UI_button_border_color, (x, y, width, height), 2)

        # Render the label text
        text_surface = font.render(label, True, UI_button_text_color)
        if text_align == 'center':
            text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
        elif text_align == 'left':
            text_rect = text_surface.get_rect(midleft=(x + 5, y + height // 2))  # 5px padding from the left
        elif text_align == 'right':
            text_rect = text_surface.get_rect(midright=(x + width - 5, y + height // 2))  # 5px padding from the right
        else:
            raise ValueError(f"Invalid text alignment: {text_align}")

        # Draw the label text
        screen.blit(text_surface, text_rect)


def handle_mouse_events(event, buttons, window_width, window_height):
    """
    Handles mouse events and checks for button interactions.

    Args:
        event: The Pygame event object.
        buttons: A dictionary of buttons to check for interactions.
        window_width: Width of the window.
        window_height: Height of the window.
    """
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
        mouse_pos = pygame.mouse.get_pos()

        # Check if the click is within a UI bar
        region = get_ui_bar_region(mouse_pos, window_width, window_height)
        if region:
            print(f"Mouse clicked in {region} bar at {mouse_pos}")

            # Check for button intersections
            for button_name, button in buttons.items():
                button_rect = pygame.Rect(button['origin'][0], button['origin'][1], button['width'], button['height'])
                if button_rect.collidepoint(mouse_pos):
                    print(f"Button '{button_name}' clicked!")
                    if button['callback']:
                        button['callback']()  # Call the button's callback function
                    return
        else:
            print(f"Mouse clicked outside UI bars at {mouse_pos}")


def get_ui_bar_region(mouse_pos, window_width, window_height):
    """
    Determines if the mouse click is within a UI bar (top, bottom, left, or right).

    Args:
        mouse_pos: Tuple (x, y) of the mouse position.
        window_width: Width of the window.
        window_height: Height of the window.

    Returns:
        A string indicating the region ('top', 'bottom', 'left', 'right') or None if not in a UI bar.
    """
    x, y = mouse_pos

    if 0 <= y <= UI_topBar_height:  # Top bar
        return 'top'
    elif window_height - UI_bottomBar_height <= y <= window_height:  # Bottom bar
        return 'bottom'
    elif 0 <= x <= UI_sideBar_left_width:  # Left sidebar
        return 'left'
    elif window_width - UI_sideBar_right_width <= x <= window_width:  # Right sidebar
        return 'right'
    return None