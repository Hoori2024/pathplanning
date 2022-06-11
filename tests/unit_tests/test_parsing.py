from unittest import TestCase
from src.pathplanning.parsing import *

class TestParsing():
    def test_fill_list_edges(self):
        lines = ['(0;0) (0;10) (10;7) (10;0)\n', '(4;5)(4;6)(5;5)\n']
        lines_same_vertices = ['(0;0) (0;0) (10;7) (10;0)\n', '(4;5)(4;6)(5;5)\n']
        lines_value_error = ['(0;0) (0;10) (10;a) (10;0)\n', '(4;5)(4;6)(5;5)\n']
        lines_less_vertices = ['(0;0) (0;10) \n']
        lines_sides_segment = ['(0;0) (0;10) (10;0) (10;7)\n']
        lines_child_segment = ['(0;0) (0;10) (10;7) (10;0)\n', '(4;5)(5;5)(4;6)(5;6)\n']
        lines_child_out_of_parent = ['(0;0) (0;10) (10;7) (10;0)\n', '(40;50)(40;60)(50;60)(50;50)\n']
        lines_secant_with_parent = ['(0;0) (4;0) (4;3) (3;3) (3;2) (1;2)(1;3)(0;3)\n', '(0.5;1)(3.5;1)(3.5;2.5)(0.5;2.5)\n']
        lines_confond_parent = ['(0;0) (0;10) (10;7) (10;0)\n', '(0;5)(4;8.8)(5;5)\n']
        expected = [[[0.0, 0.0], [0.0, 10.0], [10.0, 7.0], [10.0, 0.0]], [[4.0, 5.0], [4.0, 6.0], [5.0, 5.0]]]
        expected_pos = [[[5.0, 5.0], [0.0, 10.0], [10.0, 7.0], [10.0, 0.0]], [[4.0, 5.0], [4.0, 6.0], [5.0, 5.0]]]
        assert fill_list_edges(lines) == expected
        assert get_min_pos_x(expected_pos) == 0.0
        assert get_max_pos_x(expected_pos) == 10.0
        assert get_min_pos_y(expected_pos) == 0.0
        assert get_max_pos_y(expected_pos) == 10.0

        TestCase().assertRaises(SystemExit, fill_list_edges, lines_same_vertices)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_value_error)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_less_vertices)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_sides_segment)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_child_segment)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_child_out_of_parent)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_secant_with_parent)
        TestCase().assertRaises(SystemExit, fill_list_edges, lines_confond_parent)
