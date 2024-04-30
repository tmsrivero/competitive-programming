t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    p = a[0]
    c = 1
    b = list()
    for i in range(1, n):
        if a[i] == p:
            c += 1
        else:
            b.append(c)
            c = 0

    b.append(c)
    b.sort()
    if c == n:
        print(-1)
    else:
        print(b[0])
