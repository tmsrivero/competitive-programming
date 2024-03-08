t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a = sorted(a)
    cont = 0
    for i in range(1, n):
        s = a[i] - a[i-1]
        cont += s
    print(cont)
