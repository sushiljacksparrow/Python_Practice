def smallest_divisible(N: int, K: int) -> int:
    rem = N % K
    if rem == 0:
        return N
    return N - rem


def largest_divisble(N, K) -> int:
    rem = (N + K) % K
    if rem == 0:
        return N
    return N + K - rem


def sum_divisible(A, B, K) -> int:
    smallest = smallest_divisible(A, K)
    largest = largest_divisble(B, K)

    if smallest < A:
        smallest += K

    if largest > B:
        largest -= K

    n = int((B/K) + (A - 1)/K)

    print(smallest, largest, n)
    return n * (smallest + largest)/2


if __name__ == '__main__':
    print(sum_divisible(6, 15, 3))
