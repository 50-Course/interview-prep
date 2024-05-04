# You are given a 2D maze represented by a matrix of characters. The characters represent different elements in the maze:
# 'S': Starting position (top left corner)
# 'E': Ending position (bottom right corner)
# '#': Wall (impassable)
# '.': Empty space (passable)
# Write a function that takes the maze matrix as input and returns True if there exists a path from the starting position
# ('S') to the ending position ('E') using only the allowed movements (up, down, left, and right), and False otherwise.


def explore(maze, row, col, visited) -> bool:
    visited.add((row, col))
    if maze[row][col] == "E":
        return True
    # Explore all possible directions (neighbors)
    # Up, Down, Left, Right
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dr, col + dc
        if (
            0 <= new_row < len(maze)
            and 0 <= new_col < len(maze[0])
            and maze[new_row][new_col] != "#"
            and (new_row, new_col) not in visited
        ):
            if explore(maze, new_row, new_col, visited):
                return True
    return False


def solve_maze(maze) -> bool:
    seen = set()
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                if explore(maze, row, col, seen):
                    return True
    # No path in our maze
    return False


if __name__ == "__main__":
    maze = [
        ["S", "#", "#"],
        ["#", ".", "."],
        ["E", ".", "#"],
    ]

    print(solve_maze(maze))
