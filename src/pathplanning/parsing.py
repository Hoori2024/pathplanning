# /usr/bin/python3
# encoding:utf-8

#from parcellisation import are_segments_secant

"""
    parsing.py (à modifier)
"""

from inspect import trace
import sys

from typing import Tuple, List

Coords = Tuple[float, float]
Edge = Tuple[Coords, Coords]


def are_segments_secant(p_a: Coords, p_b: Coords, p_c: Coords, p_d: Coords) -> Coords:
    """
        Checks if the segments [AB] and [CD] are secant
        Segments are on the form (x, y).
        Returns the coordinates of the intersection, or None if not secant.
    """
    v_i: Tuple[float, float] = (p_b[0] - p_a[0], p_b[1] - p_a[1])
    v_j: Tuple[float, float] = (p_d[0] - p_c[0], p_d[1] - p_c[1])
    f_m: float = -1
    f_k: float = -1
    dist: float = v_i[0] * v_j[1] - v_i[1] * v_j[0]

    if dist != 0:
        f_m = (v_i[0] * p_a[1] - v_i[0] * p_c[1] -
               v_i[1] * p_a[0] + v_i[1] * p_c[0]) / dist
        f_k = (v_j[0] * p_a[1] - v_j[0] * p_c[1] -
               v_j[1] * p_a[0] + v_j[1] * p_c[0]) / dist
    if f_m >= 0 and f_m <= 1 and f_k >= 0 and f_k <= 1:
        return (p_c[0] + f_m * v_j[0], p_c[1] + f_m * v_j[1])
    return None


def fill_list_edges(lines: List[str]):
    """
        Fill List of edges verifing if there are not the same edge in file
        return List of edges as List[Edge]
    """
    polygons: List[Edge] = []

    for line in lines:
        polygon_vertices: List[Coords] = []
        line = line.replace("(", "").replace(" ", "").replace("\n", "")
        for elem in line.split(")"):
            if elem != "":
                coords: List(str) = elem.split(";")
                try:
                    new_vertex: Coords = [float(coords[0]), float(coords[1])]
                    if polygon_vertices.count(new_vertex) > 0:
                        print("Error: the vertices of the polygons are the same")
                        sys.exit(84)
                    polygon_vertices.append(new_vertex)
                except (ValueError, IndexError):
                    sys.exit(84)
        polygons.append(polygon_vertices)
    if len(polygons[0]) < 3:
        print("Not enough vertices")
        sys.exit(84)
    list_edges: List[Edge] = get_list_sides(polygons[0])
    if not check_if_sides_are_not_segments(list_edges):
        print("Error: the sides are segments")
        sys.exit(84)
    for i in polygons[1:]:
        list_edges_i: List[Edge] = get_list_sides(i)
        if not check_if_sides_are_not_segments(list_edges_i):
            print("Error: the sides of a child are segments")
            sys.exit(84)
        if not check_if_child_in_parent(list_edges_i, list_edges):
            print("Error: the child is not in the parent")
            sys.exit(84)
    print(polygons)
    return polygons


def get_list_sides(polygon_vertices: List[Coords]) -> List[Edge]:
    """
        Get List of sides of the polygon
        return List of sides as List[Edge]
    """
    list_sides: List[Edge] = []

    for i, _ in enumerate(polygon_vertices):
        if i == len(polygon_vertices) - 1:
            list_sides.append([polygon_vertices[i], polygon_vertices[0]])
        else:
            list_sides.append([polygon_vertices[i], polygon_vertices[i + 1]])
    return list_sides


def sides_connected(side1: Edge, side2: Edge) -> bool:
    """
        Check if the side is connected to an other side
        return True if they are connected
    """
    vertex1: Coords = side1[0]
    vertex2: Coords = side1[1]
    vertex3: Coords = side2[0]
    vertex4: Coords = side2[1]
    if vertex1[0] == vertex3[0] and vertex1[1] == vertex3[1]\
            or vertex2[0] == vertex3[0] and vertex2[1] == vertex3[1]:
        return True
    if vertex1[0] == vertex4[0] and vertex1[1] == vertex4[1]\
            or vertex2[0] == vertex4[0] and vertex2[1] == vertex4[1]:
        return True
    return False


def check_if_sides_are_not_segments(sides: List[Edge]) -> bool:
    """
        Check if the sides are not segments
        return True if they are not segments
    """
    #print("SIDES", sides)
    for side in sides:
        for side_2 in sides:
            if not sides_connected(side, side_2) and are_segments_secant(side[0], side[1], side_2[0], side_2[1]) is not None:
                return False
    return True


def get_min_pos_y(polygon: List[Edge]) -> float:
    """
        Get the minimum y of vertices of the polygon
        return minimum y as float
    """
    min_pos_y: float = polygon[0][0][1]
    for edge in polygon:
        for vertex in edge:
            if vertex[1] < min_pos_y:
                min_pos_y = vertex[1]
    return min_pos_y


def get_max_pos_y(polygon: List[Edge]) -> float:
    """
        Get the maximum y of vertices of the polygon
        return maximum y as float
    """
    max_pos_y: float = polygon[0][0][1]
    for edge in polygon:
        for vertex in edge:
            if vertex[1] > max_pos_y:
                max_pos_y = vertex[1]
    return max_pos_y


def get_min_pos_x(polygon: List[Edge]) -> float:
    """
        Get the minimum x of vertices of the polygon
        return minimum x as float
    """
    min_pos_x: float = polygon[0][0][0]
    for edge in polygon:
        for vertex in edge:
            if vertex[0] < min_pos_x:
                min_pos_x = vertex[0]
    return min_pos_x


def get_max_pos_x(polygon: List[Edge]) -> float:
    """
        Get the maximum x of vertices of the polygon
        return maximum x as float
    """
    max_pos_x: float = polygon[0][0][0]
    for edge in polygon:
        for vertex in edge:
            if vertex[0] > max_pos_x:
                max_pos_x = vertex[0]
    return max_pos_x


def count_secant_edge_with_segment(polygon: List[Edge], segment: Tuple[Coords, Coords]):
    """
        Count the number of secant edges with a segment
        return number of secant edges with a segment as int
    """
    count: int = 0

    for edge in polygon:
        if are_segments_secant(segment[0], segment[1], edge[0], edge[1]) is not None:
            count += 1
    return count


def compute_lead_coef(segment):
    """
        compute leading coefficient of a segment
    """
    x = segment[0][0] - segment[1][0]
    if x == 0:
        return None
    return (segment[0][1] - segment[1][1]) / x


def check_if_vertex_in_polygon(polygon: List[Edge], vertex: Coords) -> bool:
    """
        Check if a vertex is in a polygon
        return True if the vertex is in the polygon
    """
    max_pos_x: float = get_max_pos_x(polygon) + 0.5
    max_pos_y: float = get_max_pos_y(polygon) + 0.5

    for edge in polygon:
        if compute_lead_coef((edge[0], vertex)) == compute_lead_coef((vertex, edge[1])) and\
                vertex[0] >= min(edge[0][0], edge[1][0]) and vertex[0] <= max(edge[0][0], edge[1][0]) and\
                vertex[1] >= min(edge[0][1], edge[1][1]) and vertex[1] <= max(edge[0][1], edge[1][1]) or\
                vertex == edge[0] or vertex == edge[1]:
            return None
    if count_secant_edge_with_segment(polygon, (vertex, (vertex[0], max_pos_y))) % 2 == 1 or\
            count_secant_edge_with_segment(polygon, (vertex, (max_pos_x, vertex[1]))) % 2 == 1:
        return True
    return False


def check_if_child_in_parent(child: List[Edge], parent: List[Edge]) -> bool:
    """
        Check if the child is in the parent
        return True if the child is in the parent
    """
    for edge_c in child:
        for vertex in edge_c:
            if not check_if_vertex_in_polygon(parent, vertex):
                return False
    for edge_p in parent:
        for edge_c in child:
            if are_segments_secant(edge_p[0], edge_p[1], edge_c[0], edge_c[1]) is not None:
                return False
    return True
