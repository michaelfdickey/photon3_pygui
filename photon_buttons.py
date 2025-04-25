### All UI buttons for the Photon3 GUI
# #******************************************************************************************************
# #******************************************************************************************************

import photon_ui as pui  # Import the UI module



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
dictionary_button['origin'] = (0, 100)                               # Position below the "Example Button"
dictionary_button['width'] = pui.UI_sideBar_left_width                   # Width of the button
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