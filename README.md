# Tree-Data-stucture-to-maze-map
A Python project that generates and visualizes random mazes using Depth-First Search (DFS). Includes both a command-line ASCII representation and an interactive GUI built with tkinter. Entry point is always at (0, 0) and the exit is at the bottom-right corner.

**Features:**

>DFS-based perfect maze generation (10x10 grid by default)

>Terminal output with ASCII maze visualization

>GUI rendering using tkinter with colored start (green) and exit (red) points

>Modular structure for easy extension (e.g., larger mazes or different algorithms)

**Usage:**

>``python3 maze_generator.py``

**Preview:**

CLI: ASCII maze layout

GUI: Interactive maze rendered with walls and colored entry/exit

![example 1](https://github.com/ruenso/Tree-Data-stucture-to-maze-map/blob/main/eg%201.jpg)
![example 2](https://github.com/ruenso/Tree-Data-stucture-to-maze-map/blob/main/eg%202.jpg)

## How It Works

**Maze Generation**

>The maze is generated using the recursive backtracking (DFS) algorithm. Each cell starts with all four walls and the algorithm "knocks down" walls to form a path.

**Data Structure**

.A defaultdict(set) stores open directions from each cell (North=0, East=1, South=2, West=3).

**Visualization**

>*__CLI:__* Walls and spaces drawn with ASCII characters.

>*__GUI:__* Each cell is drawn on a tk.Canvas, showing only walls that remain. Entry is marked green, exit red.

## Getting Started

**Requirements**

**Python 3.x**

**No third-party libraries needed**

## Run

>``python3 cli_nodes.py``

>``python3 maze_generator.py``

## Maze Logic Details

>Each cell knows which directions (N, E, S, W) are open.

>Maze is guaranteed to be solvable due to DFS traversal.

>Grid size is fixed to 10x10, but can be changed in the code:

>``generator = MazeGenerator(size=10)``

## License
>This project is licensed under the GNU General Public License v3.0.
>You are free to use, modify, and distribute this software under the same license.
