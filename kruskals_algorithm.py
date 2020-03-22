class Solution:
    def krusals(self, edges) -> int:
        graph = []
        vertices = set()
        for u, v, w in edges:
            graph.append([u, v, w])
            vertices.add(u)
            vertices.add(v)
        graph = sorted(graph, key=lambda x: x[2])
        print(graph)
        detected = []
        result = []
        for edge in graph:
            u, v, w = edge
            if u not in detected or v not in detected:
                result.append([u, v, w])
                detected.append(u)
                detected.append(v)
        return result


if __name__ == '__main__':
    edges = [[0, 1, 10],
             [0, 2, 6],
             [0, 3, 5],
             [1, 3, 15],
             [2, 3, 4]]
    sol = Solution()
    print(sol.krusals(edges))
