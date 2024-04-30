def query(l, r, p):
    return p[r] - (p[l - 1] if l > 0 else 0)


def solve():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    p = [a[0]]
    for i in range(1, n):
        p.append(p[-1] + a[i])

    ans = float('inf')

    for i in range(n):
        l, r, pos = i, n - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if query(i, mid, p) <= s:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        if pos == -1 or query(i, pos, p) != s:
            continue
        ans = min(ans, n - (pos - i + 1))

    print(ans if ans != float('inf') else -1)


t = int(input())
for _ in range(t):
    solve()
