import argparse
import pathlib

from maziez.graphs.solver import solve_all
from maziez.models.maze import Maze
from maziez.view.renderer import SVGRenderer

def main() -> None:
    maze = Maze.load(parse_path())
    solutions = solve_all(maze)
    if solutions:
        renderer = SVGRenderer()
        for solution in solutions:
            renderer.render(maze, solution).preview()
    else:
        print("No solution found")

def parse_path() -> pathlib.Path:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=pathlib.Path)
    return parser.parse_args().path

if __name__ == "__main__":
    main()
