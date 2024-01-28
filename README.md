# Conway's Game of Life
Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

# Features
Random Initialization: Start the simulation with a randomly generated grid.
Manual Setup Mode: Manually set up the initial state of the grid using mouse input.
Interactive Simulation: Pause and resume the simulation at any time.
Mouse Drag Drawing: Add or remove cells by clicking or dragging the mouse in manual setup mode.
How to Run
Ensure you have Python and Pygame installed on your system. You can install Pygame using pip if it's not already installed:

pip install pygame


To run the game, execute the script from your terminal:

python  main.py


# Controls
## Start Screen:
Press R for a random initial grid.
Press M to enter manual setup mode.
## Manual Setup Mode:
Click or click and drag with the mouse to draw live cells.
Press S to start the simulation.
## During Simulation:
Press S to pause and return to setup mode.
Press Esc or close the window to exit the game.
## Rules of the Game
Any live cell with two or three live neighbors survives.
Any dead cell with three live neighbors becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
About
This implementation of Conway's Game of Life was created using Python and Pygame. It's a simple yet powerful demonstration of cellular automata and emergent behavior in complex systems.

