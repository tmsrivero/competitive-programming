n = int(input())
t = list(map(int, input().split()))
c = []
c = 1
a = 1
ans = 0
for i in range(1, len(t)):
    if t[i] == t[i-1]:
        c += 1
    else:
        a = c
        c = 1
    d = min(a, c)
    ans = max(d, ans)
print(ans*2)
