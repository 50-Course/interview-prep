# Write a function, undirectedPath that takes in an array
# of edges of an undirected graph, and two nodes, (nodeA, nodeB),
# the function should return a boolean indicating whether or not there exists
# a path between A and B.
from collections import defaultdict, deque
from pprint import pprint


def undirectedPath(edges, start, end):
    graph = build_graph(edges)
    print(graph)


def build_graph(edges):
    G = defaultdict()

    for edge in edges:
        (a, b) = edge
        if a not in G:
            G[a] = []
        if b not in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)
    return G


if __name__ == "__main__":
    edges = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'm'],
    ]
    pprint(undirectedPath(edges, 'j', 'm'), sort_dicts=False, indent=4)
