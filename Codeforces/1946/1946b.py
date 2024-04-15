t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    s = 0
    for j in range(k):
        for i in range(len(a)):
            s += a[i]
        a[0] = s
        a = sorted(a)

    r = 0
    for i in range(len(a)):
        r += a[i]

    print(r)
