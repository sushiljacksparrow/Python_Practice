class Solution:
    def boxStackingMaxHeight(self, boxes) -> int:
        n = len(boxes)
        all_boxes = [[0, 0, 0] for _ in range(n*3)]

        index = 0
        for i in range(n):
            all_boxes[index] = [boxes[i][0], max(
                boxes[i][1], boxes[i][2]), min(boxes[i][1], boxes[i][2])]
            index += 1
            all_boxes[index] = [boxes[i][1], max(
                boxes[i][0], boxes[i][2]), min(boxes[i][0], boxes[i][2])]
            index += 1
            all_boxes[index] = [boxes[i][2], max(
                boxes[i][0], boxes[i][1]), min(boxes[i][0], boxes[i][1])]
            index += 1

        n *= 3
        all_boxes = sorted(all_boxes, key=lambda x: x[1]*x[2], reverse=True)

        for i in range(len(all_boxes)):
            print(all_boxes[i])

        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = all_boxes[i][0]

        for i in range(1, n):
            for j in range(i):
                if all_boxes[i][1] < all_boxes[j][1] and all_boxes[i][2] < all_boxes[j][2]:
                    if dp[i] < dp[j] + all_boxes[i][0]:
                        dp[i] = dp[j] + all_boxes[i][0]

        return max(dp)


if __name__ == '__main__':
    boxes = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
    sol = Solution()
    print(sol.boxStackingMaxHeight(boxes))
