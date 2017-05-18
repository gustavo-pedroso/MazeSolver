from maze import Maze
from graph import Graph
from bfs_solver import BFSSolver

input_maze = 'first_maze.png'

maze = Maze("images/"+input_maze)
maze.print()
g = Graph(maze)
#g.print_graph_nodes()
g.print_graph_stats()
bfs_solver = BFSSolver()
maze.solution = bfs_solver.solve(g)
maze.print_solution()
maze.solution_to_image("solution_"+input_maze)
