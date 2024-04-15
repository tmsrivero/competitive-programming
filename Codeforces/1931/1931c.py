t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    x = a[0]
    m = n
    i = 0
    for i in range(n):
        if a[i] == x:
            m -= 1
        else:
            break
    if (m != 0):
        for i in range(n-1, 0, -1):
            if a[i] == x:
                m -= 1
            else:
                break

    x = a[n-1]
    k = n
    i = 0
    for i in range(n):
        if a[i] == x:
            k -= 1
        else:
            break
    if (k != 0):
        for i in range(n-1, 0, -1):
            if a[i] == x:
                k -= 1
            else:
                break

    print(min(k, m))
