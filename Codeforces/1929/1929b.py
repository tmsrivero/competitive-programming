import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    # k diagonals w 1 colored cell
    # 4n-2 diagonals
    num = math.ceil(k/2)
    if (k == ((4*n)-2)):
        num += 1

    print(num)
