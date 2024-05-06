# Write a function, shortest_path, that takes in an array of 
# edges for an undirected graph, and two nodes, (nodeA, nodeB).
# The function should return the length as the number of edges,
# not the number of nodes. if there is no path it should return -1

def shortest_path(edges):
    return -1


if __name__ == '__main__':
    edges = [
        ['w', 'x'],
        ['w', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v'],
    ]
    print(shortest_path(edges))

