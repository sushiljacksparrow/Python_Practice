#
import sys


def maximum_index(arr, n) -> int:

    l_min = [0]*n
    r_max = [0]*n

    l_min[0] = arr[0]
    for i in range(1, n):
        l_min[i] = min(l_min[i-1], arr[i])

    r_max[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        r_max[i] = max(arr[i], r_max[i+1])

    i, j = 0, 0
    max_diff = -1
    while j < n and i < n:
        if (l_min[i] < r_max[j]):
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1
    return max_diff + 1


if __name__ == '__main__':
    test = int(input())
    for x in range(test):
        n = input()
        input = input()
        arr = input.split(' ')
        print(maximum_index(arr, int(n)))
