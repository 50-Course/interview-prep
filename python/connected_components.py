# Write a function that takes a in the adjanency list of an
# undirected graph, The function should return the num of
# connected componenets in the graph
def connected_graphs(graph):
    pass

if __name__ = '__main__':
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
