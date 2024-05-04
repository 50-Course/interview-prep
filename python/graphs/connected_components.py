from collections import deque

# Write a function that takes a in the adjanency list of an
# undirected graph, The function should return the num of
# connected componenets in the graph
def connected_components_count(graph):
    """
    Iterative approach in finding the connted components of an 
    undirected graph using BFS
    """
    visited = set()
    count = 0
    queue = deque([])

    def bfs(node):
        """
        Takes in a starting node and iterate through the graph
        """
        pass


def connected_components_count_recursive(graph):
    """
    Recursie approch to using BFS in ounting connted components

    Takes in an undirected graph, and returns the count of the conncted
    nodes
    """
    count = 0
    visited = set()
    queue = deque([])

    def bfs(node):
        """
        Takes in a starting node and iterate through the graph
        """
        queue.append(node)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                bfs(neighbor)

    for node in graph:
        if node not in visited:
            bfs(node)
            count +=1
    return count




def connected_graphs(graph):
    count = 0
    stack = []
    visited = set()

    for node in graph:
        if node not in visited:
            stack.append(node)
            visited.add(node)

            while stack:
                current = stack.pop()

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
            count += 1
    return count

def connected_graphs_recursive(graph) -> int:
    """
    Recursive approach to figuring out the number of connected components in
    an undirected graph - using DFS.

    Returns:
        The number of connected components in the graph
    """
    count = 0
    visited = set()

    def dfs(node):
        """
        Actual implementation of a recursive dfs

        Takes in the starting node (a point in the graph) and walks the graph
        """
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count +=1
    return count





if __name__ == '__main__':
    graph = {
        0: [0, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }
    print(connected_graphs(graph))
    print('======================')
    print(connected_graphs_recursive(graph))
    print('======================')
    print(connected_components_count(graph))
