# https://www.geeksforgeeks.org/length-of-the-longest-valid-substring/
def maximum_valid_paranthesis(arr) -> int:
    n = len(arr)
    stk = []
    stk.append(-1)
    res = 0

    for i in range(n):
        if arr[i] == '(':
            stk.append(i)
        else:
            stk.pop()
            if len(stk) != 0:
                res = max(res, i - stk[len(stk) - 1])
            else:
                stk.append(i)
    return res


if __name__ == '__main__':
    arr = '((()()'
    print(maximum_valid_paranthesis(arr))
