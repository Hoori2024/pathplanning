# /usr/bin/python3
# encoding:utf-8

"""
    parcellisation.py
"""

from enum import Enum
from typing import List, Tuple
from math import floor, ceil
import sys

from src.pathplanning.parsing import fill_list_edges, are_segments_secant


Vertex = Tuple[float, float]
Edge = Tuple[Vertex, Vertex]



def parse_input_file(filepath: str) -> List[List[Vertex]]:
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
    polygons: List[List[Vertex]] = []
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

    if len(polygons[0]) < 3:
        print("Not enough vertices")
        sys.exit(84)
    return polygons


def list_of_vertices_to_list_of_edges(vertices: List[Vertex]) -> List[Edge]:
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


class Direction(Enum):
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


class Field:
    """
        class Field: (à modifier)
    """

    class Cell:
        """
            class Cell: cell of the field, expect position of the center of the cell
        """

        class CellType(Enum):
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
            self.center: Vertex = center
            self.vertices: List[Vertex] = []
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
            string += f'type: {self.type}'
            string += ')'
            return string


        def __repr__(self):
            return str(self)


        def set_type(self, type):
            """
                Set the type of the cell
            """
            self.type = type


    def __init__(self, polygons: List[List[Vertex]]):
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
        self.cells = []

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
                coef_dir_a = self.compute_lead_coef((cell.vertices[i], cell.vertices[(i + 1) % 4]))
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

                # Determining which directions we could shift (only towards
                # `CENTER_INSIDE` and `COMPLETELY_INSIDE` cells)
                surrounding_cells = self.get_surrounding_cells(line_nb, col_nb)
                shift_ok_cells = filter(lambda cell: cell[1].type == self.Cell.CellType.COMPLETLY_INSIDE
                                        or cell.type == self.Cell.CellType.CENTER_INSIDE, surrounding_cells)

                # Getting the points of intersection with the field's edges:
                pt_intersect = self.get_pt_intersect_for_cell(cell)

                # Shifting the cell vertically if needed:

                # Shifting the cell horizontally if needed:

        # Removing the cells completely outside:
        new_cells_list = []
        for line in self.cells:
            filtered_line = filter(
                lambda cell: cell.type != self.Cell.CellType.COMPLETLY_OUTSIDE, line)
            new_cells_list.append(filtered_line)
        self.cells = new_cells_list


    def get_surrounding_cells(self, line_nb: int, col_nb: int) -> List[Tuple[Direction, Cell]]:
        """
            Returns a list of tuples containing info on the cells surrounding the cell
            with the given indexes, in the following directions: up, right, down, left.
            The info includes the direction and the cell.
        """
        surrounding_cells = []
        if line_nb > 0:
            surrounding_cells.append((
                Direction.UP, (self.cells[line_nb - 1][col_nb])))
        if line_nb < len(self.cells) - 1:
            surrounding_cells.append((
                Direction.DOWN, (self.cells[line_nb + 1][col_nb])))
        if col_nb > 0:
            surrounding_cells.append((
                Direction.LEFT, (self.cells[line_nb][col_nb - 1])))
        if col_nb < len(self.cells[0]) - 1:
            surrounding_cells.append((
                Direction.RIGHT, (self.cells[line_nb][col_nb + 1])))
        return surrounding_cells


    def get_pt_intersect_for_cell(self, cell: Cell) -> List[Tuple[Direction, Vertex]]:
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
                if pt_intersect is not None:
                    pt_intersect_list.append((direction, pt_intersect))
        return pt_intersect_list
