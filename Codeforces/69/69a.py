t = int(input())
cx = 0
cy = 0
cz = 0
for _ in range(t):
    x, y, z = map(int, input().split())
    cx += x
    cy += y
    cz += z

if cx == 0 and cy == 0 and cz == 0:
    print("YES")
else:
    print("NO")
