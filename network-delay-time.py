import collections
import heapq


class Solution:
    def networkDelayTime(self, times, N, K) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while len(pq) > 0:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))
        return max(dist.values()) if len(dist) == N else -1


if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    sol = Solution()
    print(sol.networkDelayTime(times, N, K))
