#/usr/bin/python3
#encoding:utf-8

"""
    pathplanning.py (à modifier)
"""

from enum import Enum
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


def are_segments_secant(A, B, C, D) -> (float, float):
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
    def __init__(self, list_limits):
        """
            list_limits: list of the field's limits (as list of list of segments)
        """
        self.limits = list_limits
        self.min_pos_x = None
        self.max_pos_x = None
        self.min_pos_y = None
        self.max_pos_y = None

    def __str__(self):
        return f"Field: {self.limits}"

    def __repr__(self):
        return f"Field: {self.limits}"


class Cell:
    """
        class Cell: (à modifier)
    """

    class CellType(Enum):
        """
            class CellType: (à modifier)
        """
        COMPLETELY_INSIDE = 0
        CENTER_INSIDE = 1
        CENTER_OUTSIDE = 2
        COMPLETELY_OUTSIDE = 3

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name


    def __init__(self, center):
        """ center: the coords of the center """
        self.center = center
        self.vertices = ... #TODO
        self.type = ... # TODO

    def __str__(self):
        return f"Cell({self.center})"

    def __repr__(self):
        return f"Cell({self.center})"


def main() -> None:
    """
        Main function.
    """
    if len(sys.argv) <= 1 and len(sys.argv) > 2:
        display_usage_and_exit(84)
    if '-h' in sys.argv or '--help' in sys.argv:
        display_usage_and_exit(0)
    print(parse_input_file(sys.argv[1]))


if __name__ == "__main__":
    main()
