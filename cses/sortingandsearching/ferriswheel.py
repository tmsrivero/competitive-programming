n, x = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
i = 0
j = len(p)-1
ans = 0
while i <= j:
    if (p[i] + p[j]) <= x:
        i += 1
        j -= 1
        ans += 1
    elif (p[i] + p[j]) > x:
        j -= 1
        ans += 1
print(ans)
