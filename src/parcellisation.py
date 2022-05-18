#/usr/bin/python3
#encoding:utf-8

from enum import Enum

"""
    pathplanning.py (à modifier)
"""

import sys


def display_usage_and_exit(exit_code: int) -> None:
    """
        Display usage and exit with the given exit code.
    """

    print(f"USAGE: {sys.argv[0]} parcellisation.py filepath")
    sys.exit(exit_code)


def parse_input_file(filepath: str) -> list(list(tuple(float))):
    """
        (0; 0.2) (0; -1) (3.8; 5) (0; 4)
        (2; 3) (3; 2.9) (2; 4)
        parse the input file and return a list of segments
    """
    # TODO:
    # - check if every polygon has at least 3 vertices
    # - vérifier qu'un polygone n'ait pas plusieurs sommets confondus
    # - vérifier que les polygones enfants soient tous dans le polygone parent
    # - vérifier qu'un polygone enfant ne soit pas dans un autre polygone enfant

    vertices_polygon: list(list(tuple(float))) = []

    try:
        with open(filepath, "r") as file:
            lines: list(str) = file.readlines()
    except FileNotFoundError:
        print("File not found")
        sys.exit(84)
    for line in lines:
        stock_vertice: list(tuple(float)) = []
        line = line.replace("(", "").replace(" ", "").replace("\n", "")
        for elem in line.split(")"):
            if elem != "":
                elems: list(str) = elem.split(";")
                try:
                    stock_vertice.append((float(elems[0]), float(elems[1])))
                except (ValueError, IndexError):
                    sys.exit(84)
        vertices_polygon.append(stock_vertice)
    print(vertices_polygon)
    for line in lines[1:]:
        print(line)


def are_segments_secant() -> bool: # TODO: J + R
    """
        Check if the segments are secant
    """
    return False


def get_distance_between_segments(segment1: tuple(float), segment2: tuple(float)) -> float:
    """
        Get the distance between two segments
    """
    return ((segment1[0] - segment2[0]) ** 2 + (segment1[1] - segment2[1]) ** 2) ** 0.5


class Field:
    def __init__(self, list_limits):
        """
            list_limits: list of the field's limits (as list of list of segments)
        """
        self.limits = list_limits
        self.min_pos_x = None
        self.max_pos_x = None
        self.min_pos_y = None
        self.max_pos_y = None


class Cell:

    class CellType(Enum):
        COMPLETELY_INSIDE = 0
        CENTER_INSIDE = 1
        CENTER_OUTSIDE = 2
        COMPLETELY_OUTSIDE = 3

        
    def __init__(self, center):
        """ center: the coords of the center """
        self.center = center
        self.vertices = ... #TODO
        self.type = ... # TODO


def main() -> None:
    """
        Main function.
    """
    if len(sys.argv) <= 1 and len(sys.argv) > 2:
        display_usage_and_exit(84)
    if '-h' in sys.argv or '--help' in sys.argv:
        display_usage_and_exit(0)
    parse_input_file(sys.argv[1])


if __name__ == "__main__":
    main()
