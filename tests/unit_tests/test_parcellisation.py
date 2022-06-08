import sys
# import os
# sys.path.append('../../src/')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(1, '../../src/')
from pathplanning.parcellisation import *

class TestParcellisation():
    def test_parse_input_file(self):
        ...


    def test_list_of_vertices_to_list_of_edges(self):
        ...


    def test_are_segments_secant(self):
        ...


    def test_get_distance_between_segments(self):
        ...


    def test_refresh_cells_types(self):
        ...


    def test_is_cell_center_in(self):
        ...


    def test_count_secant_edge_with_segment(self):
        ...


    def test_is_cell_on_edge(self):
        ...


    def test_arrange_cells(self):
        ...


    def test_surrounding_cells(self):
        ...


    def test_get_pt_intersect_for_cell(self):
        ...


    def test_str_direction(self):
        direction_up = Direction.UP
        direction_right = Direction.RIGHT
        direction_down = Direction.DOWN
        direction_left = Direction.LEFT

        assert str(direction_up) == "UP"
        assert str(direction_right) == "RIGHT"
        assert str(direction_down) == "DOWN"
        assert str(direction_left) == "LEFT"


    def test_repr_direction(self):
        direction_up = Direction.UP
        direction_right = Direction.RIGHT
        direction_down = Direction.DOWN
        direction_left = Direction.LEFT

        assert repr(direction_up) == "UP"
        assert repr(direction_right) == "RIGHT"
        assert repr(direction_down) == "DOWN"
        assert repr(direction_left) == "LEFT"

