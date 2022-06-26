def zeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return int(count)


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
