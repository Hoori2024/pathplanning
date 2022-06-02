#/usr/bin/python3
#encoding:utf-8

"""
    parsing.py (à modifier)
"""

import sys

from typing import Tuple, List


Vertex = Tuple[float, float]


def fill_list_edges(lines):
    """
        Fill list of edges verifing if there are not the same edge in file
    """
    polygons: list(list(Vertex)) = []
    for line in lines:
        polygon_vertices: list(Vertex) = []
        line = line.replace("(", "").replace(" ", "").replace("\n", "")
        for elem in line.split(")"):
            if elem != "":
                coords: list(str) = elem.split(";")
                try:
                    new_vertex: Vertex = (float(coords[0]), float(coords[1]))
                    if polygon_vertices.count(new_vertex) > 0:
                        print("Error: the vertices of the polygons are the same")
                        sys.exit(84)
                    polygon_vertices.append(new_vertex)
                except (ValueError, IndexError):
                    sys.exit(84)
        polygons.append(polygon_vertices)
    return polygons


def check_if_vertices_in_polygon(vertices_polygon, vertice): # TODO: S
    """
        Check if the vertice is in the polygon
    """
    list(vertices_polygon)
    list(vertice)
    return False


def check_if_child_in_parent(child, parent): # TODO: S
    """
        Check if the child is in the parent
    """
    list(child)
    list(parent)
    return False
