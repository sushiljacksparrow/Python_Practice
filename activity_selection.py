# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
class Solution:
    def activitySelection(self, start_times, end_times) -> list:
        graph = []
        for start, end in zip(start_times, end_times):
            graph.append([start, end, end - start])

        # sort the graph by finishing times
        graph = sorted(graph, key=lambda x: x[1])
        result = [graph[0]]
        current_end_time = graph[0][1]
        index = 1
        print(graph)
        while index < len(graph):
            if graph[index][1] <= current_end_time:
                index = index + 1
            else:
                result.append(graph[index])
                current_end_time = graph[index][1]
                index = index + 1
        return result


if __name__ == '__main__':
    start_time = [1, 3, 0, 5, 8, 5]
    end_time = [2, 4, 6, 7, 9, 9]
    sol = Solution()
    print(sol.activitySelection(start_time, end_time))
