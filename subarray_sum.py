def subarray_sum(arr, sum) -> int:
    current_sum = arr[0]
    n = len(arr)
    start = 0
    for i in range(1, n):
        print(start, current_sum)
        if current_sum == sum:
            return start+1, i
        elif current_sum > sum:
            while current_sum > sum and current_sum >= 0:
                current_sum -= arr[start]
                start += 1
            if current_sum == sum:
                return start+1, i
        else:
            current_sum += arr[i]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = 15
    print(subarray_sum(arr, s))
