n, k = map(int, input().split())
r = 240 - k
c = 0
for i in range(n):
    r -= 5*(i+1)
    if r >= 0:
        c += 1
print(c)
