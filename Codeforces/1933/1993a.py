t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for j in range(n):
        if a[j] < 0:
            a[j] = a[j]*-1
        c += a[j]

    print(c)
