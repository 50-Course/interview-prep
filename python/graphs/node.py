from typing import Optional, Protocol


class TreeNode:

    def __init__(self, value: int, weight: Optional[int] = None):
        self.value = value
        self.weight = weight

    def __repr__(self) -> str:
        return f'Node {self.value}'
