from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)


def topological_sort_util(v, visited, graph, stack):
    visited[v] = True
    for i in g.graph[v]:
        if visited[i] is False:
            topological_sort_util(i, visited, graph, stack)

    stack.insert(0, v)


def topological_sort(graph):
    visited = [False]*(graph.V)
    stk = []
    for i in range(graph.V):
        if visited[i] is False:
            topological_sort_util(i, visited, graph, stk)

    print(stk)


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    topological_sort(g)
