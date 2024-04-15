t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    i = 0
    c = 0
    m = n
    while m > 0:
        m -= (n - a[i])
        if m >= 0:
            c += 1
        i += 1
    print(c)
