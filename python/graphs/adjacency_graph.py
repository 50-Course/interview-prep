from collections import deque
from dataclasses import dataclass
from typing import List

from node import TreeNode as Node


@dataclass
class Graph:
    matrix: List[List[int]]

    def __init__(self, vertices: int) -> None:
        self.matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.size = vertices

    def add_edge(self, start: Node, end: Node) ->  None:
        self.matrix[start.value][end.value] = 1
        self.matrix[end.value][start.value] = 1

    def print_edges(self):
        for i in range(self.size):
            print(self.matrix[i])

    def build_graph(self, start: Node, m: int, n: int) -> None:
        """
        An alternative constructor for the __init__() constructor
        that takes a dimension mxn to build the graph
        """
        self.matrix = [[0 for _ in range(n)] for  _ in range(m)]
        self.matrix[0][1] = 1
        self.matrix[1][0] = 1

        queue = deque([start])
        visited = {False for _ in range(len(self.matrix))}
        print(visited)

        for i in range(len(self.matrix)):
            print(self.matrix[i])

        while queue:
            current = queue.popleft()

            for neighbor in self.matrix[current.value]:
                if neighbor not in visited:
                    # visited[current][neighbor] = True

                    print(neighbor)
                queue.append(Node(neighbor))




        print(len(self.matrix))
        




if __name__ == "__main__":
    graph = Graph(5)
    node1 = Node(0)
    node2 = Node(1)
    node3 = Node(2)
    node4 = Node(3)
    node5 = Node(4)

    graph.add_edge(node1, node2)
    graph.add_edge(node1, node3)
    graph.add_edge(node2, node4)
    graph.add_edge(node2, node5)

    graph.print_edges()
    
    print('----------------------------')
    graph.build_graph(node1, 3, 3)
