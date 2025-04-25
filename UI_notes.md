# UI Design Notes

## Elements

### Buttons

BUTTON TERMINOLOGY GUIDE:

example:
```
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
```

buttons['simulation_modes_button'] = simulation_modes_button

Button Types:
- pushy - a button that activates only while being pressed, releases with mouse click release
- sticky - a button that stays activated when clicked, until clicked again
- Radio Button - a button that is part of a group where only one can be active at a time
- label - a passive text label that can not be interacted with
- indicator - a passive label that can change state
- icon - rendered as a graphical icon instead of text
- repeat - sends repeated activate events if held (like scrolling)
- menu - opens a menu of elements right next to it
- dialog - opens a window of elements in the screen center (or pre-defined location)
- cycle - with each click, it cycles through a list of options


## Interface Formats

### Classic Vertical Sidebar + Top Bar (default)

Sidebar: Tool-specific controls (left or right)
Top bar: Mode/category buttons (change sidebar contents)
Content area: Full screen for canvas/simulation
Used in: CAD, LightWave, old-school Photoshop, etc.

### Ribbon Interface (MS Office / SolidWorks style)

Top ribbon: Tabbed categories with wide button/tool sections
Mini sidebar: Optional for context or properties
Content area: Main interactive zone

### Used in: SolidWorks, AutoCAD modern UI, Office, Visual Studio

Panel Docking / Resizable Panes
Dockable windows/panels: Users can drag & resize panels (properties, log, file browser, etc.)
Main viewport: Stays center or fills space dynamically
Used in: Blender, Unity, Unreal Editor, Qt Creator
