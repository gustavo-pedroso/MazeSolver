from maze import Maze
from graph import Graph
from bfs_solver import BFSSolver
from dfs_solver import DFSSolver
from dijsktra_solver import DijkstraSolver

input_maze = 'fourth_maze.png'

maze = Maze("images/"+input_maze)
# maze.print()
g = Graph(maze)
# g.print_graph_nodes()
# g.print_graph_stats()
bfs_solver = BFSSolver()
dfs_solver = DFSSolver()
dijkstra_solver = DijkstraSolver()
maze.solution = dijkstra_solver.solve(g)
maze.print_solution()
maze.solution_to_image("solution_"+input_maze)
