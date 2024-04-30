import math

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        # f = f-1 + f-2
        # f - f-1 = f-2
        # t - s = p
        s = n
        p = i
        ban = True
        for j in range(k-2):
            aux = p
            p = s-aux
            s = aux
            ban &= p <= s
            ban &= min(p, s) >= 0
            if (ban == False):
                break
        if (ban):
            ans += 1
    print(ans)
