# /usr/bin/python3
# encoding:utf-8

"""
    Parallel partitioning algorithm
"""

from typing import List

from src.pathplanning.parcellisation import Field as parcel_field


class Field:

    class Partition:

        class Node:

            """
                Node class,
                Node has a type,
                Node has a position,
                Node has a list of links,
            """

            class NodeType(Enum):
                """
                    Node type enum
                    
                """
                ...

            class Link:
                """
                    Link between two nodes, it's called Edge in the paper
                """
                def __init__(self, node1: Node, node2: Node) -> None:
                    self._node1: float = node1
                    self._node2: float = node2

            def __init__(self, x: float, y: float) -> None:
                self._x: float = x
                self._y: float = y
                self._links: List[self.Link] = []
                self._type = ... # TODO

        def __init__(self) -> None:
            self._first_node: Node = None
            self._first_path: List[Node] = []
            self._second_path: List[Node] = []


    def __init__(self, cells: List[List[Cell]]) -> None:
        """
            Initializes the field with the given cells which allow to create nodes and links
        """
        self._partitions: List[self.Partition] = []
