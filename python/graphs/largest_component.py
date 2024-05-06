# Write a function that takes in the adjacency list of an
# undirected graph.
# The function should return the size of the largest connected
# component in the graph

def largest_component(graph):
    """
    Returns:
        The size of the larrgest connected component
    in the given graph.
    """

    # Input processing

    # mark the current node as visited
    # For each vertex (or node) in our graph.adj[current]
    # if vertex is not yet visited
    # run a recursive call on this vertex()
    #
    # Output processing
    # Do some output processing
    # return the output

    largest = 0
    visited = set()

    # get our start node essentially,
    # each keyed value and explore their neighbors
    # once exploration is done, increment the size
    # and return the size
    for node in graph:
        size = explore(graph, node, visited)
        if size > largest:
            largest = size
    return largest


def explore(graph, current, visited):
    if current in visited:
        return 0

    size = 1
    visited.add(current)

    for neighbor in graph[int(current)]:
        size += explore(graph, neighbor, visited)
    return size


if __name__ == '__main__':
    graph = {
        0: ['8', '1', '5'],
        1: ['0'],
        5: ['0', '8'],
        8: ['0', '5'],
        2: ['3', '4'],
        3: ['2', '4'],
        4: ['3', '2']
    }
    print(largest_component(graph))

