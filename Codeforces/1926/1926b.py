def find_shape(grid):
    n = len(grid)
    top, left = n, n
    bottom, right = 0, 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                top = min(top, i)
                bottom = max(bottom, i)
                left = min(left, j)
                right = max(right, j)

    width = right - left + 1
    height = bottom - top + 1

    if width == height:
        return "SQUARE"
    else:
        return "TRIANGLE"


t = int(input())
for _ in range(t):
    n = int(input())
    grid = [input() for _ in range(n)]
    print(find_shape(grid))
