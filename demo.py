from maze import Maze
from bfs_solver import BFSSolver

input_maze = "first_maze.png"

maze = Maze("images/"+input_maze)
print("Simple maze representation:")
maze.print()
g = maze.maze_to_graph()

print("Graph representation:")
g.print()
g.connect()
print("Graph Connections:")
g.print_conn()

solver = BFSSolver(g)
print("BFS Solution:")
maze.solution = solver.solve()

maze.print_solution()
maze.solution_to_image("solution_"+input_maze)


