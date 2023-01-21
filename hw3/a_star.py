"""
CMSC 14200, Winter 2023
Homework #3

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math
import graph
import minheap
from util import haversine


def build_path(gr, start, end):
    """
    Returns the path between the specified vertices in the graph

    Parameters:
        gr : Graph
        start : Vertex : the starting vertex
        end   : Vertex : the final destination

    Returns: list[str] : the shortest path identified between these vertices
    """
    raise NotImplementedError("todo: build_path")


def a_star(gr, start, end):
    """
    Finds a shortest path between the specified vertices in the graph
    using A* Search

    Parameters:
        gr : Graph
        start : Vertex : the starting vertex
        end   : Vertex : the final destination

    Returns: tuple[float, list[str], set[Vertex]] or None : None if no path
        exists, otherwise, a tuple of shortest path distance, the vertices
        along the path, and the set of vertices visited during the computation
    """
    raise NotImplementedError("todo: a_star")
