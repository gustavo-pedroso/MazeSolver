from maze import Maze
from bfs_solver import BFSSolver

maze = Maze("images/first_maze.png")
print("Simple maze representation:")
maze.print()
g = maze.maze_to_graph()
print("Graph representation:")
g.print()
g.connect()
print("Graph Connections")
g.print_conn()

solver = BFSSolver(g)
solver.solve()