def circular_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    start = 0

    while True:
        path.append(circular_array[start])
        start = (start + m - 1) % n
        if start == 0:
            break

    return ''.join(map(str, path))


print(circular_path(int(input()), int(input())))
