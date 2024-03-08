n = int(input())
c = []
for i in range(n):
    a, b = map(int, input().split())
    c.append((a, b))

c.sort(key=lambda x: (x[1], x[0]), reverse=True)

points = c[0][0]
t = c[0][1]
for i in range(1, n):
    if i <= t:
        points += c[i][0]
        t += c[i][1]

print(points)