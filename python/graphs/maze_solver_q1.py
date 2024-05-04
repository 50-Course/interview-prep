# You are given a 2D maze represented by a matrix of characters. The characters represent different elements in the maze:
# 'S': Starting position (top left corner)
# 'E': Ending position (bottom right corner)
# '#': Wall (impassable)
# '.': Empty space (passable)
# Write a function that takes the maze matrix as input and returns True if there exists a path from the starting position
# ('S') to the ending position ('E') using only the allowed movements (up, down, left, and right), and False otherwise.


if __name__ == '__main__':


    maze = [
          ['S', '.', '#'],
          ['.', '#', '.'],
          ['E', '.', '.'],
    ]

    print(solve_maze(maze))
