import math


def altura(N):

    n = 1 + 8*N
    h = (-1 + math.sqrt(n)) / 2
    return int(h)


t = int(input())
for _ in range(t):
    N = int(input())
    print(altura(N))
