def check(h, a):
    ans = 0
    for i in range(len(a)):
        ans += max(0, h-a[i])
    return ans


t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 1
    e = 10e9
    ans = 1
    while s <= e:
        mid = s+(e-s)//2
        r = check(mid, a)
        if r <= x:
            ans = mid
            s = mid+1
        else:
            e = mid-1
    print(int(ans))
