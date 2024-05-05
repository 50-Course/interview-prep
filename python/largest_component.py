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

    size = 0
    visited = set()

    # get our start node essentially,
    # each keyed value and explore their neighbors
    # once exploration is done, increment the size
    # and return the size
    for node in graph:
        if node not in visited:
            if explore(graph, node, visited):
                size += 1
    return size


def explore(graph, current, visited):
    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            explore(graph, neighbor, visited)
            visited.add(neighbor)


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

