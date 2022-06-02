#/usr/bin/python3
#encoding:utf-8

"""
    parsing.py (à modifier)
"""

import sys

from typing import Tuple, List


Coords = Tuple[float, float]


def fill_list_vertices(lines):
    """
        Fill list of vertices verifing if there are not the same vertices in file
    """
    vertices_polygon: list(list(Coords)) = []
    for line in lines:
        stock_vertice: list(Coords) = []
        line = line.replace("(", "").replace(" ", "").replace("\n", "")
        for elem in line.split(")"):
            if elem != "":
                elems: list(str) = elem.split(";")
                try:
                    if stock_vertice.count((float(elems[0]), float(elems[1]))) > 0:
                        print("Error: the vertices of the polygons are the same")
                        sys.exit(84)
                    stock_vertice.append((float(elems[0]), float(elems[1])))
                except (ValueError, IndexError):
                    sys.exit(84)
        vertices_polygon.append(stock_vertice)
    return vertices_polygon


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
