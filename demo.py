from maze import Maze

maze = Maze("images/first_maze.png")
print("Simple maze representation:")
maze.print()
g = maze.maze_to_graph()
print("Graph representation:")
g.print()