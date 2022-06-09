import sys
# import os
# sys.path.append('../../src/')
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#sys.path.insert(1, '../../src/')

from src.pathplanning.parcellisation import *

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
        polygons = [[(0.0, 0.0), (0.0, 10.0), (10.0, 7.0), (10.0, 0.0)], [(4.0, 5.0), (4.0, 6.0), (5.0, 5.0)]]
        f = Field(polygons)
        res = "[[Cell(center: (0.5, 0.5), vertices: [(0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 1.5), vertices: [(0.0, 2.0), (1.0, 2.0), (1.0, 1.0), (0.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 2.5), vertices: [(0.0, 3.0), (1.0, 3.0), (1.0, 2.0), (0.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 3.5), vertices: [(0.0, 4.0), (1.0, 4.0), (1.0, 3.0), (0.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 4.5), vertices: [(0.0, 5.0), (1.0, 5.0), (1.0, 4.0), (0.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 5.5), vertices: [(0.0, 6.0), (1.0, 6.0), (1.0, 5.0), (0.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 6.5), vertices: [(0.0, 7.0), (1.0, 7.0), (1.0, 6.0), (0.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 7.5), vertices: [(0.0, 8.0), (1.0, 8.0), (1.0, 7.0), (0.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 8.5), vertices: [(0.0, 9.0), (1.0, 9.0), (1.0, 8.0), (0.0, 8.0)], type: COMPLETLY_INSIDE), Cell(center: (0.5, 9.5), vertices: [(0.0, 10.0), (1.0, 10.0), (1.0, 9.0), (0.0, 9.0)], type: CENTER_INSIDE)], [Cell(center: (1.5, 0.5), vertices: [(1.0, 1.0), (2.0, 1.0), (2.0, 0.0), (1.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 1.5), vertices: [(1.0, 2.0), (2.0, 2.0), (2.0, 1.0), (1.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 2.5), vertices: [(1.0, 3.0), (2.0, 3.0), (2.0, 2.0), (1.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 3.5), vertices: [(1.0, 4.0), (2.0, 4.0), (2.0, 3.0), (1.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 4.5), vertices: [(1.0, 5.0), (2.0, 5.0), (2.0, 4.0), (1.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 5.5), vertices: [(1.0, 6.0), (2.0, 6.0), (2.0, 5.0), (1.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 6.5), vertices: [(1.0, 7.0), (2.0, 7.0), (2.0, 6.0), (1.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 7.5), vertices: [(1.0, 8.0), (2.0, 8.0), (2.0, 7.0), (1.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 8.5), vertices: [(1.0, 9.0), (2.0, 9.0), (2.0, 8.0), (1.0, 8.0)], type: COMPLETLY_INSIDE), Cell(center: (1.5, 9.5), vertices: [(1.0, 10.0), (2.0, 10.0), (2.0, 9.0), (1.0, 9.0)], type: CENTER_INSIDE)], [Cell(center: (2.5, 0.5), vertices: [(2.0, 1.0), (3.0, 1.0), (3.0, 0.0), (2.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 1.5), vertices: [(2.0, 2.0), (3.0, 2.0), (3.0, 1.0), (2.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 2.5), vertices: [(2.0, 3.0), (3.0, 3.0), (3.0, 2.0), (2.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 3.5), vertices: [(2.0, 4.0), (3.0, 4.0), (3.0, 3.0), (2.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 4.5), vertices: [(2.0, 5.0), (3.0, 5.0), (3.0, 4.0), (2.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 5.5), vertices: [(2.0, 6.0), (3.0, 6.0), (3.0, 5.0), (2.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 6.5), vertices: [(2.0, 7.0), (3.0, 7.0), (3.0, 6.0), (2.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 7.5), vertices: [(2.0, 8.0), (3.0, 8.0), (3.0, 7.0), (2.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 8.5), vertices: [(2.0, 9.0), (3.0, 9.0), (3.0, 8.0), (2.0, 8.0)], type: COMPLETLY_INSIDE), Cell(center: (2.5, 9.5), vertices: [(2.0, 10.0), (3.0, 10.0), (3.0, 9.0), (2.0, 9.0)], type: CENTER_OUTSIDE)], [Cell(center: (3.5, 0.5), vertices: [(3.0, 1.0), (4.0, 1.0), (4.0, 0.0), (3.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 1.5), vertices: [(3.0, 2.0), (4.0, 2.0), (4.0, 1.0), (3.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 2.5), vertices: [(3.0, 3.0), (4.0, 3.0), (4.0, 2.0), (3.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 3.5), vertices: [(3.0, 4.0), (4.0, 4.0), (4.0, 3.0), (3.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 4.5), vertices: [(3.0, 5.0), (4.0, 5.0), (4.0, 4.0), (3.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 5.5), vertices: [(3.0, 6.0), (4.0, 6.0), (4.0, 5.0), (3.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 6.5), vertices: [(3.0, 7.0), (4.0, 7.0), (4.0, 6.0), (3.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 7.5), vertices: [(3.0, 8.0), (4.0, 8.0), (4.0, 7.0), (3.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (3.5, 8.5), vertices: [(3.0, 9.0), (4.0, 9.0), (4.0, 8.0), (3.0, 8.0)], type: CENTER_INSIDE), Cell(center: (3.5, 9.5), vertices: [(3.0, 10.0), (4.0, 10.0), (4.0, 9.0), (3.0, 9.0)], type: CENTER_OUTSIDE)], [Cell(center: (4.5, 0.5), vertices: [(4.0, 1.0), (5.0, 1.0), (5.0, 0.0), (4.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 1.5), vertices: [(4.0, 2.0), (5.0, 2.0), (5.0, 1.0), (4.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 2.5), vertices: [(4.0, 3.0), (5.0, 3.0), (5.0, 2.0), (4.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 3.5), vertices: [(4.0, 4.0), (5.0, 4.0), (5.0, 3.0), (4.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 4.5), vertices: [(4.0, 5.0), (5.0, 5.0), (5.0, 4.0), (4.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 5.5), vertices: [(4.0, 6.0), (5.0, 6.0), (5.0, 5.0), (4.0, 5.0)], type: CENTER_ON_EDGE), Cell(center: (4.5, 6.5), vertices: [(4.0, 7.0), (5.0, 7.0), (5.0, 6.0), (4.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 7.5), vertices: [(4.0, 8.0), (5.0, 8.0), (5.0, 7.0), (4.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (4.5, 8.5), vertices: [(4.0, 9.0), (5.0, 9.0), (5.0, 8.0), (4.0, 8.0)], type: CENTER_INSIDE), Cell(center: (4.5, 9.5), vertices: [(4.0, 10.0), (5.0, 10.0), (5.0, 9.0), (4.0, 9.0)], type: COMPLETLY_OUTSIDE)], [Cell(center: (5.5, 0.5), vertices: [(5.0, 1.0), (6.0, 1.0), (6.0, 0.0), (5.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 1.5), vertices: [(5.0, 2.0), (6.0, 2.0), (6.0, 1.0), (5.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 2.5), vertices: [(5.0, 3.0), (6.0, 3.0), (6.0, 2.0), (5.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 3.5), vertices: [(5.0, 4.0), (6.0, 4.0), (6.0, 3.0), (5.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 4.5), vertices: [(5.0, 5.0), (6.0, 5.0), (6.0, 4.0), (5.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 5.5), vertices: [(5.0, 6.0), (6.0, 6.0), (6.0, 5.0), (5.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 6.5), vertices: [(5.0, 7.0), (6.0, 7.0), (6.0, 6.0), (5.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 7.5), vertices: [(5.0, 8.0), (6.0, 8.0), (6.0, 7.0), (5.0, 7.0)], type: COMPLETLY_INSIDE), Cell(center: (5.5, 8.5), vertices: [(5.0, 9.0), (6.0, 9.0), (6.0, 8.0), (5.0, 8.0)], type: CENTER_OUTSIDE), Cell(center: (5.5, 9.5), vertices: [(5.0, 10.0), (6.0, 10.0), (6.0, 9.0), (5.0, 9.0)], type: COMPLETLY_OUTSIDE)], [Cell(center: (6.5, 0.5), vertices: [(6.0, 1.0), (7.0, 1.0), (7.0, 0.0), (6.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 1.5), vertices: [(6.0, 2.0), (7.0, 2.0), (7.0, 1.0), (6.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 2.5), vertices: [(6.0, 3.0), (7.0, 3.0), (7.0, 2.0), (6.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 3.5), vertices: [(6.0, 4.0), (7.0, 4.0), (7.0, 3.0), (6.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 4.5), vertices: [(6.0, 5.0), (7.0, 5.0), (7.0, 4.0), (6.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 5.5), vertices: [(6.0, 6.0), (7.0, 6.0), (7.0, 5.0), (6.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 6.5), vertices: [(6.0, 7.0), (7.0, 7.0), (7.0, 6.0), (6.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (6.5, 7.5), vertices: [(6.0, 8.0), (7.0, 8.0), (7.0, 7.0), (6.0, 7.0)], type: CENTER_INSIDE), Cell(center: (6.5, 8.5), vertices: [(6.0, 9.0), (7.0, 9.0), (7.0, 8.0), (6.0, 8.0)], type: CENTER_OUTSIDE), Cell(center: (6.5, 9.5), vertices: [(6.0, 10.0), (7.0, 10.0), (7.0, 9.0), (6.0, 9.0)], type: COMPLETLY_OUTSIDE)], [Cell(center: (7.5, 0.5), vertices: [(7.0, 1.0), (8.0, 1.0), (8.0, 0.0), (7.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 1.5), vertices: [(7.0, 2.0), (8.0, 2.0), (8.0, 1.0), (7.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 2.5), vertices: [(7.0, 3.0), (8.0, 3.0), (8.0, 2.0), (7.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 3.5), vertices: [(7.0, 4.0), (8.0, 4.0), (8.0, 3.0), (7.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 4.5), vertices: [(7.0, 5.0), (8.0, 5.0), (8.0, 4.0), (7.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 5.5), vertices: [(7.0, 6.0), (8.0, 6.0), (8.0, 5.0), (7.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 6.5), vertices: [(7.0, 7.0), (8.0, 7.0), (8.0, 6.0), (7.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (7.5, 7.5), vertices: [(7.0, 8.0), (8.0, 8.0), (8.0, 7.0), (7.0, 7.0)], type: CENTER_INSIDE), Cell(center: (7.5, 8.5), vertices: [(7.0, 9.0), (8.0, 9.0), (8.0, 8.0), (7.0, 8.0)], type: COMPLETLY_OUTSIDE), Cell(center: (7.5, 9.5), vertices: [(7.0, 10.0), (8.0, 10.0), (8.0, 9.0), (7.0, 9.0)], type: COMPLETLY_OUTSIDE)], [Cell(center: (8.5, 0.5), vertices: [(8.0, 1.0), (9.0, 1.0), (9.0, 0.0), (8.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 1.5), vertices: [(8.0, 2.0), (9.0, 2.0), (9.0, 1.0), (8.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 2.5), vertices: [(8.0, 3.0), (9.0, 3.0), (9.0, 2.0), (8.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 3.5), vertices: [(8.0, 4.0), (9.0, 4.0), (9.0, 3.0), (8.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 4.5), vertices: [(8.0, 5.0), (9.0, 5.0), (9.0, 4.0), (8.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 5.5), vertices: [(8.0, 6.0), (9.0, 6.0), (9.0, 5.0), (8.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 6.5), vertices: [(8.0, 7.0), (9.0, 7.0), (9.0, 6.0), (8.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (8.5, 7.5), vertices: [(8.0, 8.0), (9.0, 8.0), (9.0, 7.0), (8.0, 7.0)], type: CENTER_OUTSIDE), Cell(center: (8.5, 8.5), vertices: [(8.0, 9.0), (9.0, 9.0), (9.0, 8.0), (8.0, 8.0)], type: COMPLETLY_OUTSIDE), Cell(center: (8.5, 9.5), vertices: [(8.0, 10.0), (9.0, 10.0), (9.0, 9.0), (8.0, 9.0)], type: COMPLETLY_OUTSIDE)], [Cell(center: (9.5, 0.5), vertices: [(9.0, 1.0), (10.0, 1.0), (10.0, 0.0), (9.0, 0.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 1.5), vertices: [(9.0, 2.0), (10.0, 2.0), (10.0, 1.0), (9.0, 1.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 2.5), vertices: [(9.0, 3.0), (10.0, 3.0), (10.0, 2.0), (9.0, 2.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 3.5), vertices: [(9.0, 4.0), (10.0, 4.0), (10.0, 3.0), (9.0, 3.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 4.5), vertices: [(9.0, 5.0), (10.0, 5.0), (10.0, 4.0), (9.0, 4.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 5.5), vertices: [(9.0, 6.0), (10.0, 6.0), (10.0, 5.0), (9.0, 5.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 6.5), vertices: [(9.0, 7.0), (10.0, 7.0), (10.0, 6.0), (9.0, 6.0)], type: COMPLETLY_INSIDE), Cell(center: (9.5, 7.5), vertices: [(9.0, 8.0), (10.0, 8.0), (10.0, 7.0), (9.0, 7.0)], type: CENTER_OUTSIDE), Cell(center: (9.5, 8.5), vertices: [(9.0, 9.0), (10.0, 9.0), (10.0, 8.0), (9.0, 8.0)], type: COMPLETLY_OUTSIDE), Cell(center: (9.5, 9.5), vertices: [(9.0, 10.0), (10.0, 10.0), (10.0, 9.0), (9.0, 9.0)], type: COMPLETLY_OUTSIDE)]]"

        assert str(f.cells) == res

    def test_is_cell_center_in(self):
        polygons = [[(0.0, 0.0), (0.0, 10.0), (10.0, 7.0), (10.0, 0.0)], [(4.0, 5.0), (4.0, 6.0), (5.0, 5.0)]]
        f = Field(polygons)
        cell_in = f.Cell((2, 2))
        cell_out = f.Cell((100, 100))
        cell_on_edge = f.Cell((0, 5))

        assert f.is_cell_center_in(cell_in) == True
        assert f.is_cell_center_in(cell_out) == False
        assert f.is_cell_center_in(cell_on_edge) == None


    def test_count_secant_edge_with_segment(self):
        polygons = [[(0.0, 0.0), (0.0, 10.0), (10.0, 7.0), (10.0, 0.0)], [(4.0, 5.0), (4.0, 6.0), (5.0, 5.0)]]
        f = Field(polygons)
        segment_a = ((-10, 5),(100, 5))
        segment_b = ((0.5, 0.5),(2, 2))

        assert f.count_secant_edge_with_segment(segment_a) == 4
        assert f.count_secant_edge_with_segment(segment_b) == 0


    def test_compute_lead_coef(self):
        polygons = [[(0.0, 0.0), (0.0, 10.0), (10.0, 7.0), (10.0, 0.0)], [(4.0, 5.0), (4.0, 6.0), (5.0, 5.0)]]
        f = Field(polygons)
        segment_a = ((0,0), (10, 0))
        segment_b = ((0, 0), (10, 10))
        segment_c = ((0, 0), (0, 10))

        assert f.compute_lead_coef(segment_a) == 0
        assert f.compute_lead_coef(segment_b) == 1
        assert f.compute_lead_coef(segment_c) == None

    def test_is_cell_on_edge(self):
        polygons = [[(0.0, 0.0), (0.0, 10.0), (10.0, 7.0), (10.0, 0.0)], [(4.0, 5.0), (4.0, 6.0), (5.0, 5.0)]]
        f = Field(polygons)
        cell_on_edge = f.Cell((0.2, 0.2))
        cell_not_on_edge = f.Cell((1.5, 1.5))

        assert f.is_cell_on_edge(cell_on_edge) == True
        assert f.is_cell_on_edge(cell_not_on_edge) == False


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

