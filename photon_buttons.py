### All UI buttons for the Photon3 GUI
# #******************************************************************************************************
# #******************************************************************************************************

import photon_ui as pui  # Import the UI module


"""
button types
pushy           - a button that activates only while being pressed, releases with mouse click release
sticky          - a button that stays activated when clicked, until clicked again
Radio Button    - a button that is part of a group where only one can be active at a time
label           - a passive text label that can not be interacted with
indicator       - a passive label that can change state
icon            - rendered as a graphical icon instead of text
repeat          - sends repeated activate events if held (like scrolling)
menu            - opens a menu of elements right next to it
dialog          - opens a window of elements in the screen center (or pre-defined location)
cycle           - with each click, it cycles through a list of options
"""


"""
## Simulation Modes button
simulation_modes_button = {}
simulation_modes_button['name'] = "simulation_modes_button"
simulation_modes_button['origin'] = (pgv.UI_sideBar_width, 0)
simulation_modes_button['width'] = pgv.UI_sideBar_width
simulation_modes_button['height'] = pgv.UI_sideBar_height
simulation_modes_button['font'] = MainFont
simulation_modes_button['textAlign'] = 'center'                     # left, center, right
simulation_modes_button['label'] = "Simulation Modes:"
simulation_modes_button['type'] = 'pushy'                           # pushy, sticky, selector, label, indicator
simulation_modes_button['status'] = 'unselected'                    # for iterating through button states this is the selected button
simulation_modes_button['active'] = True                            # the button is currently active and available to be clicked on
simulation_modes_button['enabled'] = True                           # the value or activity this button enables is calculated
simulation_modes_button['display'] = True                           # the button is visible or not visible
simulation_modes_button['master_group'] = None                      # the group this button is a child of, None if no parent
simulation_modes_button['peer_group'] = 'main'                      # group of mutually exclusive buttons (e.g., radio group)
simulation_modes_button['child_group'] = 'simulation_modes'         # the group this button activates
simulation_modes_button['tooltip'] = SimulationHelp                 # hover-over content
simulation_modes_button['callback'] = None                          # function to call on click
simulation_modes_button['hovered'] = False                          # True when mouse is over
simulation_modes_button['pressed'] = False                          # True when mouse button is held down
simulation_modes_button['toggle_state'] = False                     # For toggles: True if toggled on
simulation_modes_button['icon'] = None                              # optional image/icon
simulation_modes_button['theme'] = None                             # dict with color/styling overrides
simulation_modes_button['z_order'] = 0                              # draw order priority
simulation_modes_button['hotkey'] = None                            # keybinding (e.g., pygame.K_m)
simulation_modes_button['interaction_rect_override'] = None         # manually override clickable area
simulation_modes_button['button_style'] = "primary"                # select the button display from a group of styles (e.g. rounded corners, bold outlines, etc)
"""

"""
creating a button:
## Simulation Modes button
simulation_modes_button = {}
simulation_modes_button['name'] = "simulation_modes_button"
simulation_modes_button['origin'] = (pgv.UI_sideBar_width, 0)
simulation_modes_button['width'] = pgv.UI_sideBar_width
simulation_modes_button['label'] = " Mode : "
simulation_modes_button['type'] = 'pushy'
simulation_modes_button['status'] = 'unselected'
simulation_modes_button['active'] = True
simulation_modes_button['display'] = True
simulation_modes_button['master_group'] = None
simulation_modes_button['peer_group'] = 'main'
simulation_modes_button['child_group'] = 'simulation_modes'
simulation_modes_button['region'] = 'topBar'
buttons_topbar['simulation_modes_button'] = simulation_modes_button
"""

buttons_sidebar = {}  # Dictionary to hold sidebar buttons
buttons_topbar = {}  # Dictionary to hold top bar buttons
buttons_bottombar = {}  # Dictionary to hold bottom bar buttons

# #******************************************************************************************************
#  buttons side bar *************************************************************************************
# #******************************************************************************************************


# first dictionary button
dictionary_button = {}
dictionary_button['name'] = "dictionary_button"
dictionary_button['origin'] = (0, 70)                               # Position below the "Example Button"
dictionary_button['width'] = pui.UI_sideBar_left_width               # Width of the button
dictionary_button['height'] = 20
dictionary_button['font'] = None                                    # Use default font
dictionary_button['textAlign'] = 'center'                           # Text alignment: left, center, right
dictionary_button['label'] = "Dictionary Button"
dictionary_button['type'] = 'pushy'                                 # Button type: pushy, sticky, selector, etc.
dictionary_button['status'] = 'unselected'                          # Button state
dictionary_button['active'] = True                                  # Button is active and clickable
dictionary_button['enabled'] = True                                 # Button is enabled meaning it can be clicked
dictionary_button['display'] = True                                 # Button is visible
dictionary_button['master_group'] = None                            # Parent group, if any
dictionary_button['peer_group'] = 'sidebar'                         # Group of mutually exclusive buttons
dictionary_button['child_group'] = None                             # Group activated by this button
dictionary_button['tooltip'] = None                                 # Tooltip text (optional)
dictionary_button['callback'] = None                                # Function to call on click
dictionary_button['hovered'] = False                                # True when mouse is over the button
dictionary_button['pressed'] = False                                # True when mouse button is held down
dictionary_button['toggle_state'] = False                           # For toggles: True if toggled on
dictionary_button['icon'] = None                                    # Optional image/icon
dictionary_button['theme'] = None                                   # Dict with color/styling overrides
dictionary_button['z_order'] = 0                                    # Draw order priority
dictionary_button['hotkey'] = None                                  # Keybinding (e.g., pygame.K_m)
dictionary_button['interaction_rect_override'] = None               # Override clickable area
dictionary_button['button_style'] = "primary"                       # Button style (e.g., rounded corners)
# Add the button to the sidebar group
buttons_sidebar['dictionary_button'] = dictionary_button

# 2nd dictionary button
dictionary_2_button = {}
dictionary_2_button['name'] = "dictionary_2_button"
dictionary_2_button['origin'] = (0, 90)                               # Position below the "Example Button"
dictionary_2_button['width'] = pui.UI_sideBar_left_width               # Width of the button
dictionary_2_button['height'] = 20
dictionary_2_button['font'] = None                                    # Use default font
dictionary_2_button['textAlign'] = 'center'                           # Text alignment: left, center, right
dictionary_2_button['label'] = "Dictionary Button 2"
dictionary_2_button['type'] = 'sticky'                               # Button type: pushy, sticky, selector, etc.
dictionary_2_button['status'] = 'unselected'                          # Button state
dictionary_2_button['active'] = True                                  # Button is active and clickable
dictionary_2_button['enabled'] = True                                 # Button is enabled meaning it can be clicked
dictionary_2_button['display'] = True                                 # Button is visible
dictionary_2_button['master_group'] = None                            # Parent group, if any
dictionary_2_button['peer_group'] = 'sidebar'                         # Group of mutually exclusive buttons
dictionary_2_button['child_group'] = None                             # Group activated by this button
dictionary_2_button['tooltip'] = None                                 # Tooltip text (optional)
dictionary_2_button['callback'] = None                                # Function to call on click
dictionary_2_button['hovered'] = False                                # True when mouse is over the button
dictionary_2_button['pressed'] = False                                # True when mouse button is held down
dictionary_2_button['toggle_state'] = False                           # For toggles: True if toggled on
dictionary_2_button['icon'] = None                                    # Optional image/icon
dictionary_2_button['theme'] = None                                   # Dict with color/styling overrides
dictionary_2_button['z_order'] = 0                                    # Draw order priority
dictionary_2_button['hotkey'] = None                                  # Keybinding (e.g., pygame.K_m)
dictionary_2_button['interaction_rect_override'] = None               # Override clickable area
dictionary_2_button['button_style'] = "primary"                       # Button style (e.g., rounded corners)
# Add the button to the sidebar group
buttons_sidebar['dictionary_2_button'] = dictionary_2_button


# Sticky button 1
button_sticky_1 = {}
button_sticky_1['name'] = "button_sticky_1"
button_sticky_1['origin'] = (0, 110)                                # Position below the "Example Button"
button_sticky_1['width'] = pui.UI_sideBar_left_width               # Width of the button
button_sticky_1['height'] = 20
button_sticky_1['font'] = None                                     # Use default font
button_sticky_1['textAlign'] = 'center'                            # Text alignment: left, center, right
button_sticky_1['label'] = "Sticky Button 1"
button_sticky_1['type'] = 'sticky'                                 # Button type: pushy, sticky, selector, etc.
button_sticky_1['status'] = 'unselected'                           # Button state
button_sticky_1['active'] = True                                   # Button is active and clickable
button_sticky_1['enabled'] = True                                  # Button is enabled meaning it can be clicked
button_sticky_1['display'] = True                                  # Button is visible
button_sticky_1['master_group'] = None                             # Parent group, if any
button_sticky_1['peer_group'] = 'sidebar'                          # Group of mutually exclusive buttons
button_sticky_1['child_group'] = None                              # Group activated by this button
button_sticky_1['tooltip'] = None                                  # Tooltip text (optional)
button_sticky_1['callback'] = None                                 # Function to call on click
button_sticky_1['hovered'] = False                                 # True when mouse is over the button
button_sticky_1['pressed'] = False                                 # True when mouse button is held down
button_sticky_1['toggle_state'] = False                            # For toggles: True if toggled on
button_sticky_1['icon'] = None                                     # Optional image/icon
button_sticky_1['theme'] = None                                    # Dict with color/styling overrides
button_sticky_1['z_order'] = 0                                     # Draw order priority
button_sticky_1['hotkey'] = None                                   # Keybinding (e.g., pygame.K_m)
button_sticky_1['interaction_rect_override'] = None                # Override clickable area
button_sticky_1['button_style'] = "primary"                        # Button style (e.g., rounded corners)
# Add the button to the sidebar group
buttons_sidebar['button_sticky_1'] = button_sticky_1



# Pushy button 1
button_pushy_1 = {}
button_pushy_1['name'] = "button_pushy_1"
button_pushy_1['origin'] = (0, 130)                                # Position (adjusted if needed)
button_pushy_1['width'] = pui.UI_sideBar_left_width               # Width of the button
button_pushy_1['height'] = 20
button_pushy_1['font'] = None                                     # Use default font
button_pushy_1['textAlign'] = 'center'                            # Text alignment: left, center, right
button_pushy_1['label'] = "Pushy Button 1"
button_pushy_1['type'] = 'pushy'                                  # Button type: pushy, sticky, selector, etc.
button_pushy_1['status'] = 'unselected'                           # Button state
button_pushy_1['active'] = True                                   # Button is active and clickable
button_pushy_1['enabled'] = True                                  # Button is enabled meaning it can be clicked
button_pushy_1['display'] = True                                  # Button is visible
button_pushy_1['master_group'] = None                             # Parent group, if any
button_pushy_1['peer_group'] = 'sidebar'                          # Group of mutually exclusive buttons
button_pushy_1['child_group'] = None                              # Group activated by this button
button_pushy_1['tooltip'] = None                                  # Tooltip text (optional)
button_pushy_1['callback'] = None                                 # Function to call on click
button_pushy_1['hovered'] = False                                 # True when mouse is over the button
button_pushy_1['pressed'] = False                                 # True when mouse button is held down
button_pushy_1['toggle_state'] = False                            # For toggles: True if toggled on
button_pushy_1['icon'] = None                                     # Optional image/icon
button_pushy_1['theme'] = None                                    # Dict with color/styling overrides
button_pushy_1['z_order'] = 0                                     # Draw order priority
button_pushy_1['hotkey'] = None                                   # Keybinding (e.g., pygame.K_m)
button_pushy_1['interaction_rect_override'] = None                # Override clickable area
button_pushy_1['button_style'] = "primary"                        # Button style (e.g., rounded corners)
# Add the button to the sidebar group
buttons_sidebar['button_pushy_1'] = button_pushy_1


# Sticky button 2
button_sticky_2 = {}
button_sticky_2['name'] = "button_sticky_2"
button_sticky_2['origin'] = (0, 170)                              # Position (adjusted below sticky_1)
button_sticky_2['width'] = pui.UI_sideBar_left_width               # Width of the button
button_sticky_2['height'] = 20
button_sticky_2['font'] = None                                     # Use default font
button_sticky_2['textAlign'] = 'left'                               # Text alignment: left, center, right
button_sticky_2['label'] = "Sticky Button 2"
button_sticky_2['type'] = 'sticky'                                 # Button type: pushy, sticky, selector, etc.
button_sticky_2['status'] = 'unselected'                           # Button state
button_sticky_2['active'] = True                                   # Button is active and clickable
button_sticky_2['enabled'] = True                                  # Button is enabled meaning it can be clicked
button_sticky_2['display'] = True                                  # Button is visible
button_sticky_2['master_group'] = None                             # Parent group, if any
button_sticky_2['peer_group'] = 'sidebar'                          # Group of mutually exclusive buttons
button_sticky_2['child_group'] = None                              # Group activated by this button
button_sticky_2['tooltip'] = None                                  # Tooltip text (optional)
button_sticky_2['callback'] = None                                 # Function to call on click
button_sticky_2['hovered'] = False                                 # True when mouse is over the button
button_sticky_2['pressed'] = False                                 # True when mouse button is held down
button_sticky_2['toggle_state'] = False                            # For toggles: True if toggled on
button_sticky_2['icon'] = None                                     # Optional image/icon
button_sticky_2['theme'] = None                                    # Dict with color/styling overrides
button_sticky_2['z_order'] = 0                                     # Draw order priority
button_sticky_2['hotkey'] = None                                   # Keybinding (e.g., pygame.K_m)
button_sticky_2['interaction_rect_override'] = None                # Override clickable area
button_sticky_2['button_style'] = "primary"                        # Button style (e.g., rounded corners)
# Add the button to the sidebar group
buttons_sidebar['button_sticky_2'] = button_sticky_2
