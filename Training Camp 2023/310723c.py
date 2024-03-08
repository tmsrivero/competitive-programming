n, m = map(int, input().split())
a = [input() for h in range(n)]

f = 0

for i in range(n - 1):
    for j in range(m - 1):
        t = ""
        t += a[i][j]
        t += a[i][j + 1]
        t += a[i + 1][j]
        t += a[i + 1][j + 1]
        t = ''.join(sorted(t))
        if t == "acef":
            f += 1

print(f)

