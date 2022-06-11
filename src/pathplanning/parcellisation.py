# /usr/bin/python3
# encoding:utf-8

"""
    parcellisation.py
"""

from enum import IntEnum
from typing import List, Tuple
from math import floor, ceil
import sys

from src.pathplanning.parsing import fill_list_edges, are_segments_secant
from src.pathplanning.visualisation import *


Coords = Tuple[float, float]
Edge = Tuple[Coords, Coords]


def parse_input_file(filepath: str) -> List[List[Coords]]:
    """
        (0; 0.2) (0; -1) (3.8; 5) (0; 4)
        (2; 3) (3; 2.9) (2; 4)
        parse the input file and return a list of polygons
    """
    # TODO:
    # - check if every polygon has at least 3 vertices - OK
    # - vérifier qu'un polygone n'ait pas plusieurs sommets confondus - OK
    # - vérifier qu'un polygone n'ait pas des côtés qui se croisent
    # - vérifier que les polygones enfants soient tous dans le polygone parent
    # - vérifier qu'un polygone enfant ne soit pas dans un autre polygone enfant

    # List of polygons (polygon = list of its vertices)
    polygons: List[List[Coords]] = []
    try:
        with open(filepath, "r", encoding="utf8") as file:
            lines: List[str] = file.readlines()
    except (FileNotFoundError):
        print("File not found")
        sys.exit(84)
    if len(lines) == 0:
        print("File is empty")
        sys.exit(84)
    polygons = fill_list_edges(lines)
    return polygons


def list_of_vertices_to_list_of_edges(vertices: List[Coords]) -> List[Edge]:
    """ Converts a list of a polygon's vertices into a list of its vertices. """
    edges = []
    for idx_vertex in range(len(vertices)):
        edges.append(
            (vertices[idx_vertex], vertices[(idx_vertex + 1) % len(vertices)]))
    return edges


# def get_distance_between_segments(segment1, segment2) -> float:
#     """
#         Get the min distance between two segments
#     """
#     return ((segment1[0] - segment2[0]) ** 2 + (segment1[1] - segment2[1]) ** 2) ** 0.5


class Direction(IntEnum):
    """
        class Direction: represents directions that can be taken from a cell
    """
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


    def __str__(self):
        return self.name


    def __repr__(self):
        return self.name


def get_opposite_dir(direction: Direction) -> Direction:
    if direction == Direction.UP:
        return Direction.DOWN
    if direction == Direction.RIGHT:
        return Direction.LEFT
    if direction == Direction.DOWN:
        return Direction.UP
    if direction == Direction.LEFT:
        return Direction.RIGHT


class Field:
    """
        class Field: (à modifier)
    """

    class Cell:
        """
            class Cell: cell of the field, expect position of the center of the cell
        """

        class CellType(IntEnum):
            """
                class CellType: cell type defined by the position on the map and the position of the field's edges
            """
            COMPLETLY_INSIDE = 0
            CENTER_INSIDE = 1
            CENTER_OUTSIDE = 2
            COMPLETLY_OUTSIDE = 3
            CENTER_ON_EDGE = 4


            def __str__(self):
                return self.name


            def __repr__(self):
                return self.name


        def __init__(self, center):
            """ center: the coordinates of the center """
            self.center: Coords = center
            self.vertices: List[Coords] = []
            self.type = self.CellType.COMPLETLY_INSIDE

            # Determining the cell's vertices /!\ clockwise from top-left /!\
            # (important for determining the edges and their directions)
            self.vertices.append((center[0] - 0.5, center[1] + 0.5))
            self.vertices.append((center[0] + 0.5, center[1] + 0.5))
            self.vertices.append((center[0] + 0.5, center[1] - 0.5))
            self.vertices.append((center[0] - 0.5, center[1] - 0.5))

            # Determining its edges and their directions:
            self.edges: List[Tuple[Direction, Edge]] = []
            edge_list = list_of_vertices_to_list_of_edges(self.vertices)
            for idx, edge in enumerate(edge_list):
                self.edges.append((idx, edge))


        def __str__(self):
            string = f"Cell("
            string += f'center: {self.center}, '
            string += f'vertices: {self.vertices}, '
            string += f'type: {self.type.name}'
            string += ')'
            return string


        def __repr__(self):
            return str(self)


        def set_type(self, type):
            """
                Set the type of the cell
            """
            self.type = type


        def get_edge_for_direction(self, direction: Direction) -> Edge:
            for edge in self.edges:
                if edge[0] == direction or edge[0] == int(direction):
                    return edge
            return None


    def __init__(self, polygons: List[List[Coords]]):
        """
            polygons: list of the field's polygons (polygon = list of vertices)
        """
        self.edges: List[Edge] = []
        for polygon in polygons:
            new_edges = list_of_vertices_to_list_of_edges(polygon)
            self.edges += new_edges

        self.min_pos_x = floor(self.edges[0][0][0])
        self.max_pos_x = ceil(self.edges[0][0][0])
        self.min_pos_y = floor(self.edges[0][0][1])
        self.max_pos_y = ceil(self.edges[0][0][1])
        self.cells: List[List[self.Cell]] = []

        for j in self.edges:
            for i in j:
                if i[0] < floor(self.min_pos_x):
                    self.min_pos_x = floor(i[0])
                elif i[0] > ceil(self.max_pos_x):
                    self.max_pos_x = ceil(i[0])
                if i[1] < floor(self.min_pos_y):
                    self.min_pos_y = floor(i[1])
                elif i[1] > ceil(self.max_pos_y):
                    self.max_pos_y = ceil(i[1])

        for i in range(self.min_pos_x, self.max_pos_x):
            line = []
            for j in range(self.min_pos_y, self.max_pos_y):
                line.append(self.Cell((i + 0.5, j + 0.5)))
            self.cells.append(line)

        self.refresh_cells_types()


    def __str__(self):
        string = f"Edges: {self.edges}\n"
        string += "Cells:\n"
        for line in self.cells:
            for cell in line:
                string += (str(cell) + '\n')
            string += '---\n'
        return string


    def __repr__(self):
        string = f"edges: {self.edges}\n"
        string += "field:\n"
        for line in self.cells:
            for cell in line:
                string += (repr(cell) + '\n')
            string += '---\n'
        return string


    def refresh_cells_types(self):
        """
            actualize types of every cells
        """
        for line in self.cells:
            for cell in line:
                if self.is_cell_center_in(cell) == True:
                    if self.is_cell_on_edge(cell) == True:
                        cell.set_type(cell.CellType.CENTER_INSIDE)
                    else:
                        cell.set_type(cell.CellType.COMPLETLY_INSIDE)
                elif self.is_cell_center_in(cell) == False:
                    if self.is_cell_on_edge(cell) == True:
                        cell.set_type(cell.CellType.CENTER_OUTSIDE)
                    else:
                        cell.set_type(cell.CellType.COMPLETLY_OUTSIDE)
                else:
                    cell.set_type(cell.CellType.CENTER_ON_EDGE)


    def is_cell_center_in(self, cell):
        """
            check if a cell center is in or out of the edges
        """
        for i in self.edges:
            if self.compute_lead_coef((i[0], cell.center)) == self.compute_lead_coef((cell.center, i[1])) and cell.center[0] >= min(i[0][0], i[1][0]) and cell.center[0] <= max(i[0][0], i[1][0]) and cell.center[1] >= min(i[0][1], i[1][1]) and cell.center[1] <= max(i[0][1], i[1][1]) or cell.center == i[0] or cell.center == i[1]:
                return None
        if self.count_secant_edge_with_segment((cell.center, (cell.center[0], self.max_pos_y))) % 2 == 1 or self.count_secant_edge_with_segment((cell.center, (self.max_pos_x, cell.center[1]))) % 2 == 1:
            return True
        return False


    def count_secant_edge_with_segment(self, segment):
        """
            count the number of edges secants with a segment
        """
        count = 0
        for i in self.edges:
            if are_segments_secant(segment[0], segment[1], i[0], i[1]) != None:
                count += 1
        return count


    def compute_lead_coef(self, segment):
        """
            compute leading coefficient of a segment
        """
        x = segment[0][0] - segment[1][0]
        if x == 0:
            return None
        return (segment[0][1] - segment[1][1]) / x


    def is_cell_on_edge(self, cell):
        """
            check if a cell is on a edge of the field
        """
        for i in range(4):
            for j in self.edges:
                pos = are_segments_secant(
                    cell.vertices[i], cell.vertices[(i + 1) % 4], j[0], j[1])
                coef_dir_a = self.compute_lead_coef(
                    (cell.vertices[i], cell.vertices[(i + 1) % 4]))
                coef_dir_b = self.compute_lead_coef((j[0], j[1]))
                if pos != None and coef_dir_a != coef_dir_b and pos != cell.vertices[i] and pos != cell.vertices[(i + 1) % 4] and pos != j[0] and pos != j[1]:
                    return True
        return False


    def arrange_cells(self):
        """
            Filters and shifts the cells so the field contains only cells with
            their center inside of it.
        """

        for line_nb, line in enumerate(self.cells):
            for col_nb, cell in enumerate(line):
                # We only shift `CENTER_OUTSIDE` cells
                if cell.type != self.Cell.CellType.CENTER_OUTSIDE:
                    continue

                # Determining which directions we could shift (only towards surrounding
                # cells that are `CENTER_INSIDE`,`CENTER_ON_EDGE`  and `COMPLETELY_INSIDE`)
                surrounding_cells: List[Tuple[Direction, self.Cell]] = self.get_surrounding_cells(line_nb, col_nb)
                shift_ok_cells: List[Tuple[Direction, self.Cell]] = list(filter(lambda sur_cell:
                    sur_cell[1].type == self.Cell.CellType.COMPLETLY_INSIDE
                    or sur_cell[1].type == self.Cell.CellType.CENTER_INSIDE
                    or sur_cell[1].type == self.Cell.CellType.CENTER_ON_EDGE, surrounding_cells))

                shift_directions = [shift_ok_cell[0] for shift_ok_cell in shift_ok_cells]
                shift_directions_vert = list(filter(lambda dir: dir == Direction.UP
                    or dir == Direction.DOWN, shift_directions))
                shift_directions_hor = list(filter(lambda dir: dir == Direction.LEFT
                    or dir == Direction.RIGHT, shift_directions))

                # Getting the points of intersection with the field's edges:
                pt_intersect: List[Tuple[Direction, Coords]] = self.get_pt_intersect_for_cell(cell)
                pt_inter_vert: List[Tuple[Direction, Coords]] = list(filter(lambda pt:
                    pt[0] % 2 == 0, pt_intersect))
                pt_inter_hor: List[Tuple[Direction, Coords]] = list(filter(lambda pt:
                    pt[0] % 2 == 1, pt_intersect))

                # Determining the shift vector:
                shift_dist_horizontal: float = self.get_shift_value(cell, pt_inter_vert,
                    shift_directions_hor)
                shift_dist_vertical: float = self.get_shift_value(cell, pt_inter_hor,
                    shift_directions_vert)
                vector: Coords = (shift_dist_horizontal, shift_dist_vertical)

                # print()
                # print(cell)
                # print(pt_inter_vert, shift_directions_hor)
                # print(pt_inter_hor, shift_directions_vert)
                # print(f"shift vector: {vector}")

                # Shifting the cell:
                self.shift_cell(line_nb, col_nb, vector)

        self.refresh_cells_types()


    def get_shift_value(self, cell: Cell, pts_intersection: List[Tuple[Direction, Coords]],
        shift_directions: List[Direction]) -> float:
        """
            Returns which distance the cell should be shifted for one direction
            (horizontal of vertical). Returns 0 if no shift is needed.
            `pts_intersection`: the points of intersection that trigger the need to shift
            the `cell` in one of the given `shift_directions`.
            The given parameters must correspond to only one direction (horizontal of vertical).
            e.g: if the points of intersections are vertical, the shift directions must be
            horizontal.
        """
        if len(pts_intersection) > 0 and len(shift_directions) > 0:

            # Any direction is good, so we take the first available one:
            shift_dir = shift_directions[0]

            # We calculate the distances between the pts of intersection and the vertices
            # of the edge opposite to the shift direction, and choose the smallest one:
            distances = []
            for pt in pts_intersection:
                opposite_direction = get_opposite_dir(shift_dir)
                opposite_edge = cell.get_edge_for_direction(opposite_direction)
                for vertex in opposite_edge[1]:
                    distances.append(self.get_distance_between_points(pt[1], vertex))

            if len(distances) == 0:
                return 0
            shift_value = min(distances)

            # If the shift direction is DOWN or RIGHT, the value is negative:
            if shift_dir > 1:
                shift_value *= -1

            return shift_value

        else:
            return 0


    def get_distance_between_points(self, point1: Coords, point2: Coords) -> float:
        """ Returns the distance between the two points. """
        pt1_x, pt1_y = point1
        pt2_x, pt2_y = point2

        return ((pt2_x - pt1_x) ** 2 + (pt2_y - pt1_y) ** 2) ** 0.5


    def shift_cell(self, line_nb: int, col_nb: int, vector: Coords) -> None:
        """ Shifts the cell's coordinates by `vector` """
        cell: self.Cell = self.cells[line_nb][col_nb]
        new_center: Coords = (cell.center[0] + vector[0], cell.center[1] + vector[1])
        cell.center = new_center


    def get_surrounding_cells(self, line_nb: int, col_nb: int) -> List[Tuple[Direction, Cell]]:
        """
            Returns a list of tuples containing info on the cells surrounding the cell
            with the given indexes, in the following directions: up, right, down, left.
            The info includes the direction and the cell.
        """

        # The field's cells are listed from left to right and top to bottom.
        # For a field represented in a grid whose origin is on the bottom-left corner:
        # - a line of self.cells is a column on a field. self.cells[0] is the left-most column
        # - a column of self.cells is a line on a field. self.cells[0][0] is the bottom-left cell
        
        surrounding_cells = []
        if line_nb > 0:
            surrounding_cells.append((
                Direction.LEFT, (self.cells[line_nb - 1][col_nb])))
        if line_nb < len(self.cells) - 1:
            surrounding_cells.append((
                Direction.RIGHT, (self.cells[line_nb + 1][col_nb])))
        if col_nb > 0:
            surrounding_cells.append((
                Direction.DOWN, (self.cells[line_nb][col_nb - 1])))
        if col_nb < len(self.cells[0]) - 1:
            surrounding_cells.append((
                Direction.UP, (self.cells[line_nb][col_nb + 1])))
        return surrounding_cells


    def get_pt_intersect_for_cell(self, cell: Cell) -> List[Tuple[Direction, Coords]]:
        """
            Returns a list of tuples containing info on the points of intersection
            of the field's edges and the given cell's edges.
            The info includes the direction and the coordinates of the point.
        """

        pt_intersect_list = []
        for (direction, cell_edge) in cell.edges:

            for field_edge in self.edges:

                pt_intersect = are_segments_secant(
                    cell_edge[0], cell_edge[1], field_edge[0], field_edge[1])

                # Ignore the intersection point if it's on one of the cell's vertices:
                pt_is_on_vertex = False
                for cell_vertex in cell.vertices:
                    if cell_vertex == pt_intersect:
                        pt_is_on_vertex = True
                        continue

                if pt_intersect is not None and not pt_is_on_vertex:
                    pt_intersect_list.append((direction, pt_intersect))

        return pt_intersect_list
