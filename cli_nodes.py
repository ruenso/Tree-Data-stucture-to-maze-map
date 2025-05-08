from collections import defaultdict

class Node:
    def __init__(self, children=None):
        self.children = children if children is not None else []

def build_maze(root):
    # Directions: North, East, South, West represented as 0, 1, 2, 3
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    maze = defaultdict(set)
    visited = set()
    leaves = []
    exit_pos = None

    # Stack elements: (node, current_position, current_direction)
    stack = [(root, (0, 0), 0)]
    visited.add((0, 0))

    while stack:
        node, pos, current_dir = stack.pop()

        # Check if it's a leaf node
        if not node.children:
            leaves.append(pos)
            continue

        # Process children in reverse order to maintain the original order when popping from stack
        for turn, child in reversed(node.children):
            new_dir = current_dir
            if turn == 'left':
                new_dir = (current_dir - 1) % 4
            elif turn == 'right':
                new_dir = (current_dir + 1) % 4
            # else, straight: direction remains the same

            dx, dy = dirs[new_dir]
            new_x = pos[0] + dx
            new_y = pos[1] + dy
            new_pos = (new_x, new_y)

            if new_pos not in visited:
                # Open the wall between current position and new position
                # Current cell opens the new_dir direction
                maze[pos].add(new_dir)
                # New cell opens the opposite direction
                opposite_dir = (new_dir + 2) % 4
                maze[new_pos].add(opposite_dir)
                visited.add(new_pos)
                stack.append((child, new_pos, new_dir))

    # Determine the exit as the last leaf node encountered
    if leaves:
        exit_pos = leaves[-1]

    return maze, exit_pos

# Example usage:
# Constructing a sample tree
root = Node()
node1 = Node()
node2 = Node()
node3 = Node()

root.children = [('straight', node1), ('right', node2)]
node1.children = [('left', node3)]  # node3 is a leaf
node2.children = []  # node2 is a leaf

maze, exit = build_maze(root)
print("Maze walls opened:", maze)
print("Exit position:", exit)
