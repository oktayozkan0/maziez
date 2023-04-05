import networkx as nx

from maziez.graphs.converter import make_graph
from maziez.models.maze import Maze
from maziez.models.solution import Solution

def solve(maze: Maze) -> Solution | None:
    try:
        return Solution(
            squares=tuple(
                nx.shortest_path(
                    make_graph(maze),
                    source=maze.entrance,
                    target=maze.exit,
                    weight="weight",
                )
            )
        )
    except nx.NetworkXException:
        return None

def solve_all(maze: Maze) -> list[Solution]:
    try:
        return [
            Solution(squares=tuple(path))
            for path in nx.all_shortest_paths(
                make_graph(maze),
                source=maze.entrance,
                target=maze.exit,
                weight="weight",
            )
        ]
    except nx.NetworkXException:
        return []
