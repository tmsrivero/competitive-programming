t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 1, 10**18
    while l <= r:
        mid = (l + r) // 2
        s = mid
        for i in range(len(a)-1):
            s += min(mid, a[i + 1] - a[i])
        if s < h:
            l = mid + 1
        else:
            r = mid - 1
    print(r + 1)
