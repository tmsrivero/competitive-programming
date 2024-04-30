n, d = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
l = 0
for i in range(2, n):
    while a[i] - a[l] > d:
        l += 1
    ans += (i - l) * (i - l - 1) // 2

print(ans)
