from dataclasses import dataclass
from typing import List

from node import TreeNode as Node


class WeightedGraph:

    def __init__(self, size: int) -> None:
        self.size =  size
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, start: Node, end: Node) -> None:
        # We want to stay within contrainst always
        if start.value < 0 or start.value >= self.size or end.value < 0 or end.value >= self.size:
            return
        # Directed grap
        # there exisit a path from route A to route B
        # self.matrix[start.value][end.value] = start.weight
        # self.matrix[end.value][start.value] = end.weight



    def dfs(self, node: Node)-> Node | None:
        pass
        
    def bfs(self, node: Node)-> Node | None:
        pass
    
    def print_graph(self) -> None:
        for i in self.matrix:
            print(i)

if __name__ == "__main__":
    graph = WeightedGraph(5)
    graph.add_edge(Node(0, 10), Node(1, 20))
    graph.add_edge(Node(1, 20), Node(2, 30))
    graph.add_edge(Node(2, 30), Node(3, 40))
    graph.add_edge(Node(3, 40), Node(4, 50))
    graph.print_graph()
