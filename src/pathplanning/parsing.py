# /usr/bin/python3
# encoding:utf-8

from parcellisation import are_segments_secant

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


def get_list_sides(polygon_vertices):
    """
        Get list of sides of the polygon
    """
    list_sides: list(list(Vertex)) = []
    for i in range(len(polygon_vertices)):
        if i == len(polygon_vertices) - 1:
            list_sides.append([polygon_vertices[i], polygon_vertices[0]])
        else:
            list_sides.append([polygon_vertices[i], polygon_vertices[i + 1]])
    return list_sides


def sides_connected(side1, side2):
    """
        Check if the side is connected to an other side
    """
    vertex1: Vertex = side1[0]
    vertex2: Vertex = side1[1]
    vertex3: Vertex = side2[0]
    vertex4: Vertex = side2[1]
    if vertex1[0] == vertex3[0] and vertex1[1] == vertex3[1]\
            or vertex2[0] == vertex3[0] and vertex2[1] == vertex3[1]\
            or vertex1[0] == vertex4[0] and vertex1[1] == vertex4[1]\
            or vertex2[0] == vertex4[0] and vertex2[1] == vertex4[1]:
        return True
    return False


def check_if_sides_are_not_segments(sides):
    """
        Check if the sides are not segments
        Return True if they are not segments
    """
    for idx in range(len(sides)):
        if idx == len(sides) - 1:
            if not sides_connected(sides[idx], sides[0]) and are_segments_secant(sides[idx], sides[0]) != None:
                return False
        else:
            if not sides_connected(sides[idx], sides[idx + 1]) and are_segments_secant(sides[idx], sides[idx + 1]) != None:
                return False
    return True


def check_if_vertices_in_polygon(vertices_polygon, vertice):  # TODO: S
    """
        Check if the vertice is in the polygon
    """
    list(vertices_polygon)
    list(vertice)
    return False


def check_if_child_in_parent(child, parent):  # TODO: S
    """
        Check if the child is in the parent
    """
    list(child)
    list(parent)
    return False
