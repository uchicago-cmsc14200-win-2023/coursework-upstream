"""
CMSC 14200, Winter 2023
Homework #2

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

from cell import Cell

# Characters for representing mazes as strings
WALL = "#"
CELL = "·"
PATH = " "
TRAIL = "o"
CURN = "^"
CURE = ">"
CURS = "v"
CURW = "<"


class Maze:
    """
    A class for representing mazes
    """

    def __init__(self, height, width, seed=None):
        raise NotImplementedError("todo: Maze constructor")

    def to_string(self, cursor, trail):
        """
        Returns a string representation of the maze

        Parameters:
            cursor : tuple[Cell, str]
            trail : list[Cell]

        Returns: str
        """
        raise NotImplementedError("todo: Maze.to_string")

    def __str__(self):
        raise NotImplementedError("todo: Maze.__str__")

    def _random_dfs(self, start, visited):
        """
        Uses DFS to generate a random maze.

        Parameters:
            start : Cell
            visited : set[Cell]

        Returns: (does not return a value)
        """
        raise NotImplementedError("todo: Maze._random_dfs")

    def directions_to_trail(self, dir_string):
        """
        Takes a direction string, and produces the list of Cell objects
        that would be visited following those directions. If the
        directions are not valid, returns None.

        Always starts at Cell (0,0)

        Parameters:
            dir_string : str

        Returns: list[Cell] or None
        """
        raise NotImplementedError("todo: Maze.directions_to_trail")

    def solve_lefthand(self):
        """
        Uses the left-hand algorithm to find a path from the
        entrance of the maze to its exit.

        Parameters: None

        Returns: str
        """
        raise NotImplementedError("todo: Maze.solve_lefthand")

    def animate(self, delay):
        """
        Display an animation of the left-hand algorithm

        Parameters:
            delay : float

        Returns: (does not return a value)
        """
        raise NotImplementedError("todo: Maze.animate")
