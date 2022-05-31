#/usr/bin/python3
#encoding:utf-8

"""
    pathplanning.py
"""

from enum import Enum
from typing import Tuple
from math import floor, ceil
import sys

from parsing import fill_list_vertices


def display_usage_and_exit(exit_code: int) -> None:
    """
        Display usage and exit with the given exit code.
    """

    print(f"USAGE: {sys.argv[0]} parcellisation.py filepath")
    sys.exit(exit_code)


def parse_input_file(filepath: str):
    """
        (0; 0.2) (0; -1) (3.8; 5) (0; 4)
        (2; 3) (3; 2.9) (2; 4)
        parse the input file and return a list of segments
    """
    # TODO:
    # - check if every polygon has at least 3 vertices - OK
    # - vérifier qu'un polygone n'ait pas plusieurs sommets confondus - OK
    # - vérifier que les polygones enfants soient tous dans le polygone parent
    # - vérifier qu'un polygone enfant ne soit pas dans un autre polygone enfant

    vertices_polygon: list(list(tuple(float))) = []
    try:
        with open(filepath, "r", encoding="utf8") as file:
            lines: list(str) = file.readlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit(84)
    vertices_polygon = fill_list_vertices(lines)

    if len(vertices_polygon[0]) < 3:
        print("Not enough vertices")
        sys.exit(84)
    return vertices_polygon


def are_segments_secant(A, B, C, D) -> Tuple[float, float]:
    """
        Check if the segments [AB] and [CD] are secant
        Segments are on the form (x, y)
        Return None if not secant
    """
    I = (B[0] - A[0], B[1] - A[1])
    J = (D[0] - C[0], D[1] - C[1])
    m = -1
    k = -1
    d = I[0] * J[1] - I[1] * J[0]

    if d != 0:
        m = (I[0] * A[1] - I[0] * C[1] - I[1] * A[0] + I[1] * C[0]) / d
        k = (J[0] * A[1] - J[0] * C[1] - J[1] * A[0] + J[1] * C[0]) / d
    if m >= 0 and m <= 1 and k >= 0 and k <= 1:
        return (C[0] + m * J[0], C[1] + m * J[1])
    return None


def get_distance_between_segments(segment1, segment2) -> float:
    """
        Get the distance between two segments
    """
    return ((segment1[0] - segment2[0]) ** 2 + (segment1[1] - segment2[1]) ** 2) ** 0.5


class Field:
    """
        class Field: (à modifier)
    """

    def __init__(self, list_edges):
        """
            list_edges: list of the field's edges (as list of lists of segments)
        """
        self.edges = []
        for i in list_edges:
            for j in range(len(i)):
                self.edges.append((i[j], i[(j + 1) % len(i)]))

        self.min_pos_x = floor(self.edges[0][0][0])
        self.max_pos_x = ceil(self.edges[0][0][0])
        self.min_pos_y = floor(self.edges[0][0][1])
        self.max_pos_y = ceil(self.edges[0][0][1])
        self.field = []

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
            for j in range(self.min_pos_y, self.max_pos_y):
                self.field.append(self.Cell((i + 0.5, j + 0.5)))

        self.refresh_type()


    def __str__(self):
        string = f"Edges: {self.edges}\n"
        string += "Cells:\n"
        for cell in self.field:
            string += (str(cell) + '\n')
        return string


    def __repr__(self):
        string = f"edges: {self.edges}\n"
        string += "field:\n"
        for cell in self.field:
            string += (repr(cell) + '\n')
        return string


    def refresh_type(self):
        """
            actualize types of every cells
        """
        for i in self.field:
            if self.is_cell_in(i) == True:
                if self.is_cell_on_edge(i) == True:
                    i.set_type(i.CellType.CENTER_INSIDE)
                else:
                    i.set_type(i.CellType.COMPLETLY_INSIDE)
            else:
                if self.is_cell_on_edge(i) == True:
                    i.set_type(i.CellType.CENTER_OUTSIDE)
                else:
                    i.set_type(i.CellType.COMPLETLY_OUTSIDE)


    def is_cell_in(self, cell):
        """
            check if a cell center is in or out of the edges
        """
        if self.count_secant_edge_with_segment((cell.center, (cell.center[0], self.max_pos_y))) % 2 == 1:
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


    def is_cell_on_edge(self, cell):
        """
            check if a cell is on a edge of the field
        """
        for i in range(4):
            for j in self.edges:
                if are_segments_secant(cell.vertices[i], cell.vertices[(i + 1) % 4], j[0], j[1]) != None:
                    return True
        return False


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

            def __str__(self):
                return self.name

            def __repr__(self):
                return self.name


        def __init__(self, center):
            """ center: the coordinates of the center """
            self.center = center
            self.vertices = []
            self.type = self.CellType.COMPLETLY_INSIDE

            for i in range(2):
                for j in range(2):
                    self.vertices.append((center[0] - 0.5 + i, center[1] - 0.5 + j))


        def __str__(self):
            return f"Cell({self.center})"
        def __repr__(self):
            return f"Cell({self.center})"


        def set_type(self, type):
            self.type = type


def main() -> int:
    """
        Main function.
    """
    if len(sys.argv) <= 1 and len(sys.argv) > 2:
        display_usage_and_exit(84)
    if '-h' in sys.argv or '--help' in sys.argv:
        display_usage_and_exit(0)
    print(parse_input_file(sys.argv[1]))

    f = Field(parse_input_file(sys.argv[1]))
    print(f)

    sys.exit(0)


if __name__ == "__main__":
    main()
