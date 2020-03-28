def jumping_numbers(current, target):
    if current > target:
        return

    print(current)
    last_digit = current % 10
    if last_digit + 1 <= 9:
        jumping_numbers(current * 10 + last_digit + 1, target)
    if last_digit - 1 >= 0:
        jumping_numbers(current * 10 + last_digit - 1, target)


if __name__ == '__main__':
    for i in range(11):
        jumping_numbers(i, 50)
