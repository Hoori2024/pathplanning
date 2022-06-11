import sys
from typing import List, Tuple

from src.pathplanning.parcellisation import *
from src.pathplanning.visualisation import *

Vertex = Tuple[float, float]


def display_usage_and_exit(exit_code: int) -> None:
    """
        Display usage and exit with the given exit code.
    """

    print(f"USAGE: {sys.argv[0]} parcellisation.py filepath")
    sys.exit(exit_code)


def main() -> int:
    """
        Main function.
    """
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        display_usage_and_exit(84)
    if '-h' in sys.argv or '--help' in sys.argv:
        display_usage_and_exit(0)
    print()
    polyons: List[List[Vertex]] = parse_input_file(sys.argv[1])
    print(polyons)

    f = Field(polyons)
    print()
    print(f)

    f.arrange_cells()
    print()
    print(f)

    #display_field(f)

    sys.exit(0)


if __name__ == "__main__":
    main()