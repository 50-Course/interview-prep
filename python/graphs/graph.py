from collections import defaultdict, deque
from dataclasses import dataclass
from inspect import _empty
from typing import List, Optional

from node import TreeNode as Node


@dataclass
class Graph:
    edges: dict[int, List[Node]]
    
    def __init__(self, node: Node) -> None:
        self.root = node
        self.edges = defaultdict(list)
   
    def bfs(self, node: Node) -> Node | None:
        queue = deque([node])
        visited = set()

        while queue:
            current_node = queue.popleft()
            visited.add(current_node.value)

            if current_node.value == node.value:
                return current_node
            
            # check for all the neighboring nodes
            # and backtrack if we have visited it
            for neighbor in self.edges[current_node.value]:
                if neighbor not in visited:
                    visited.add(neighbor)
                queue.append(Node(value=neighbor.value))
        return None

    def dfs(self, node: Node) -> Node | None:
        stack = [node];
        visited = set()

        while stack: 
            current = stack.pop()
            visited.add(current)

            if (current.value == node):
                return current
            
            for neighbor in self.edges[current.value]:
                if neighbor not in visited:
                    visited.add(neighbor)
                stack.append(Node(node.value))
        return None
