def backpack(backpack_size, weigths, values, n):
    if n == 0 or backpack_size == 0:
        return 0

    if weigths[n - 1] > backpack_size:
        return backpack(backpack_size, weigths, values, n - 1)

    return max(values[n - 1] + backpack(backpack_size - weigths[n - 1], weigths, values, n - 1)
               , backpack(backpack_size, weigths, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weigths = [10, 20, 30]
    backpack_size = 50
    n = len(values)

    answer = backpack(backpack_size, weigths, values, n)
    print(answer)
