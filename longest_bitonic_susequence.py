def longest_bitonic_subsequence(arr) -> int:
    n = len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    lds = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] < arr[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    res = lis[0] + lds[0] - 1
    for i in range(1, n):
        res = max(lis[i] + lds[i] - 1, res)
    return res


if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(longest_bitonic_subsequence(arr))
