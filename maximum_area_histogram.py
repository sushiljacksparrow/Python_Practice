# https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
def maximum_area_histogram(arr) -> int:

    stk = []
    index, res, n = 0, 0, len(arr)
    while index < n:
        if not stk or arr[stk[-1]] <= arr[index]:
            stk.append(index)
            index += 1
        else:
            t = stk.pop()
            area = arr[t]*((index - stk[-1] - 1) if stk else index)
            res = max(area, res)

    while stk:
        t = stk.pop()
        area = arr[t]*((index - stk[-1] - 1) if stk else index)
        res = max(area, res)

    return res


if __name__ == '__main__':
    hist = [6, 2, 5, 4, 5, 1, 6]
    print(maximum_area_histogram(hist))
