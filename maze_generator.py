import tkinter as tk
import random
from collections import defaultdict

class MazeGenerator:
    def __init__(self, size=10):
        self.size = size
        self.maze = defaultdict(set)
        self.exit_pos = (size-1, size-1)
        
    def maze_grid(self):
        # Initialize grid with all walls
        grid = [[{'n': True, 'e': True, 's': True, 'w': True} 
               for _ in range(self.size)] for _ in range(self.size)]
        
        # DFS algorithm for maze generation
        stack = [(0, 0)]
        visited = set()
        visited.add((0, 0))

        while stack:
            x, y = stack.pop()
            neighbors = []

            # Find unvisited neighbors
            if x > 0 and (x-1, y) not in visited:  # West
                neighbors.append(('w', x-1, y))
            if x < self.size-1 and (x+1, y) not in visited:  # East
                neighbors.append(('e', x+1, y))
            if y > 0 and (x, y-1) not in visited:  # North
                neighbors.append(('n', x, y-1))
            if y < self.size-1 and (x, y+1) not in visited:  # South
                neighbors.append(('s', x, y+1))

            if neighbors:
                stack.append((x, y))
                direction, nx, ny = random.choice(neighbors)
                
                # Remove walls between current and next cell
                if direction == 'n':
                    grid[y][x]['n'] = False
                    grid[ny][nx]['s'] = False
                elif direction == 's':
                    grid[y][x]['s'] = False
                    grid[ny][nx]['n'] = False
                elif direction == 'e':
                    grid[y][x]['e'] = False
                    grid[ny][nx]['w'] = False
                elif direction == 'w':
                    grid[y][x]['w'] = False
                    grid[ny][nx]['e'] = False
                
                visited.add((nx, ny))
                stack.append((nx, ny))

        # Convert to maze format
        dir_map = {'n': 0, 'e': 1, 's': 2, 'w': 3}
        for y in range(self.size):
            for x in range(self.size):
                cell = grid[y][x]
                open_dirs = []
                for d, code in dir_map.items():
                    if not cell[d]:
                        open_dirs.append(code)
                self.maze[(x, y)] = set(open_dirs)

        return self.maze, self.exit_pos

def print_cli_maze(maze, exit_pos, size=10):
    print("\nCLI Maze Representation (10x10):")
    print(f"Entry: (0, 0), Exit: {exit_pos}\n")
    
    # Top border
    print("+" + "---+" * size)
    
    for y in range(size):
        # Vertical walls
        row = ["|"]
        for x in range(size):
            cell = maze.get((x, y), set())
            # Check if cell is exit
            marker = " E " if (x, y) == exit_pos else "   "
            # Check east wall
            east_wall = " " if 1 in cell else "|"
            row.append(f"{marker}{east_wall}")
        
        print(''.join(row))
        
        # Horizontal walls
        bottom = ["+"]
        for x in range(size):
            cell = maze.get((x, y), set())
            south_wall = "   " if 2 in cell else "---"
            bottom.append(f"{south_wall}+")
        print(''.join(bottom))

class MazeVisualizer(tk.Tk):
    def __init__(self, maze_data, exit_pos, size=10):
        super().__init__()
        self.title("10x10 Maze Visualizer")
        self.maze = maze_data
        self.exit = exit_pos
        self.size = size
        self.cell_size = 40
        
        # Create canvas
        self.canvas = tk.Canvas(self, 
                              width=self.size*self.cell_size + 20,
                              height=self.size*self.cell_size + 20,
                              bg='white')
        self.canvas.pack(padx=10, pady=10)
        
        self.draw_maze()

    def draw_maze(self):
        for (x, y), walls in self.maze.items():
            canvas_x = x * self.cell_size
            canvas_y = y * self.cell_size

            # Draw walls
            if 0 not in walls:  # North
                self.canvas.create_line(canvas_x, canvas_y, 
                                      canvas_x + self.cell_size, canvas_y)
            if 1 not in walls:  # East
                self.canvas.create_line(canvas_x + self.cell_size, canvas_y, 
                                      canvas_x + self.cell_size, canvas_y + self.cell_size)
            if 2 not in walls:  # South
                self.canvas.create_line(canvas_x, canvas_y + self.cell_size, 
                                      canvas_x + self.cell_size, canvas_y + self.cell_size)
            if 3 not in walls:  # West
                self.canvas.create_line(canvas_x, canvas_y, 
                                      canvas_x, canvas_y + self.cell_size)

            # Mark entry and exit
            if (x, y) == (0, 0):
                self.canvas.create_oval(
                    canvas_x + 5, canvas_y + 5,
                    canvas_x + self.cell_size - 5, canvas_y + self.cell_size - 5,
                    fill='green', outline=''
                )
            if (x, y) == self.exit:
                self.canvas.create_oval(
                    canvas_x + 5, canvas_y + 5,
                    canvas_x + self.cell_size - 5, canvas_y + self.cell_size - 5,
                    fill='red', outline=''
                )

if __name__ == "__main__":
    # Generate 10x10 maze
    generator = MazeGenerator(size=10)
    maze_data, exit_pos = generator.maze_grid()
    
    # CLI output
    print_cli_maze(maze_data, exit_pos)
    
    # GUI output
    app = MazeVisualizer(maze_data, exit_pos)
    app.mainloop()