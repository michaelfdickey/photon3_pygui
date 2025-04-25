# Photon3 Pygui

## Overview
Photon3 Pygui is a Pygame-based graphical user interface application designed for interactive visualizations. This project serves as a foundation for building custom UI elements and functionalities using Pygame.

## Project Structure
The project consists of the following files:

- **photon_main.py**: The main entry point of the application. It initializes Pygame, sets up the display, and contains the main game loop that handles events and draws the UI elements.
  
- **photon_ui.py**: This module encapsulates all UI elements and related drawing functions for the Pygame application. It exports functions for drawing the background, interface bars, and buttons.
  
- **p_customizations.py**: Contains custom configurations for the UI, such as window size and program name. This file is imported by `photon_main.py` to set up the application.

## Setup Instructions
1. Ensure you have Python installed on your system.
2. Install Pygame by running the following command:
   ```
   pip install pygame
   ```
3. Clone the repository or download the project files to your local machine.

## Usage
1. Navigate to the project directory in your terminal.
2. Run the application using the following command:
   ```
   python photon_main.py
   ```
3. Interact with the UI elements as designed.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.